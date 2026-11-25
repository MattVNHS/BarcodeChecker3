from multiprocessing import context

import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from rack_scan.forms import ExtractSheetForm
from django.http import Http404
from rack_scan import dp5_client
from rack_scan.combine import combine, extractsheet
from shire.models import DNA_EXTRACTSHEET_DET

class FFPESelectView(LoginRequiredMixin, FormView):
    template_name = "rack_scan/extract_select.html"
    form_class = ExtractSheetForm

    def form_valid(self, form):
        return redirect("ffpe_rack_scan", extract_sheet=form.cleaned_data["ExtractSheet"])


class FFPERackScanView(LoginRequiredMixin, View):
    template_name = "rack_scan/ffpe_scan.html"

    def get_sheet(self, extract_sheet):
        rows = list(DNA_EXTRACTSHEET_DET.objects
                    .filter(EXTRACTSHEET=extract_sheet).order_by("POSITION"))
        if not rows:
            raise Http404("Extract sheet not found")
        return rows

    def get(self, request, extract_sheet):
        sheet = self.get_sheet(extract_sheet)
        return render(request, self.template_name,
                      {"extract_sheet": extract_sheet, "sheet": sheet})

    def post(self, request, extract_sheet):
        sheet = self.get_sheet(extract_sheet)
        context = {"extract_sheet": extract_sheet, "sheet": sheet}
        try:
            scan = dp5_client.scan()
        except dp5_client.DP5Error as e:
            context["error"] = str(e)
        else:
            context["scan"] = scan
            context["rows"] = combine(sheet, scan)
            print(extractsheet(sheet, scan))
            context["problems"] = [r for r in context["rows"] if r["problem"]]
            context["rack_mismatch"] = (sheet[0].RACK_BARCODE
                                        and sheet[0].RACK_BARCODE != scan.get("containerBarcode"))
        return render(request, self.template_name, context)

class RackScanView(LoginRequiredMixin, View):
    template_name = "rack_scan/scan.html"

    def get(self, request):


        return render(request, self.template_name)

    def post(self, request):
        context = {"scanned": True}
        url = f"{settings.DP5_URL.rstrip('/')}/dp5/remote/v1/scan"

        try:
            response = requests.post(
                url,
                params={"container_uid": settings.DP5_CONTAINER_UID},
                timeout=settings.DP5_TIMEOUT,
            )
        except requests.RequestException as e:
            # No HTTP response at all: DP5 not running, wrong URL, timeout...
            context["connection_error"] = f"{type(e).__name__}: {e}"
            return render(request, self.template_name, context)

        context["status_code"] = response.status_code

        try:
            data = response.json()
        except ValueError:
            # Response wasn't JSON (e.g. an HTML error page)
            data = {}
            context["raw_text"] = response.text[:2000]

        # Images come back as huge base64 strings; drop them so the debug output stays readable
        for key in ("rawImage", "annotatedImage", "linearReaderImage", "demoImage"):
            data.pop(key, None)
        context["data"] = data

        if response.status_code == 200:
            context["tubes"] = sorted(
                data.get("tubeBarcode", []),
                key=lambda t: (t.get("row", 0), t.get("column", 0)),
            )

        return render(request, self.template_name, context)