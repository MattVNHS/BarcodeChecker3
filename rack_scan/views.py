from multiprocessing import context

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView
from rack_scan.forms import ExtractSheetForm
from django.http import Http404
from rack_scan import dp5_client
from rack_scan.combine import combine, extractsheet
from shire.models import DNA_EXTRACTSHEET_DET
from django.db import transaction
from django.utils import timezone
from shire.models import DNA_EXTRACTS

class FFPESelectView(LoginRequiredMixin, FormView):
    template_name = "rack_scan/extract_select.html"
    form_class = ExtractSheetForm

    def form_valid(self, form):
        return redirect("ffpe_rack_scan", extract_sheet=form.cleaned_data["ExtractSheet"])


class FFPERackScanView(LoginRequiredMixin, View):
    template_name = "rack_scan/ffpe_scan.html"
    form_class = ExtractSheetForm

    def get_sheet(self, extract_sheet):
        rows = (DNA_EXTRACTSHEET_DET.objects
                    .filter(EXTRACTSHEET=extract_sheet).order_by("POSITION"))
        if not rows:
            raise Http404("Extract sheet not found")
        return rows

    def get(self, request, extract_sheet):
        rows = self.get_sheet(extract_sheet)
        return render(request, self.template_name,
                      {"extract_sheet": extract_sheet, "rows": rows})

    def post(self, request, extract_sheet):
        sheet = self.get_sheet(extract_sheet)
        context = {"extract_sheet": extract_sheet, "sheet": sheet}
        try:
            scan = dp5_client.scan()
        except dp5_client.DP5Error as e:
            context["error"] = str(e)
        else:
            context["scan"] = scan
            context["rows"] = extractsheet(extract_sheet, scan)
            #context["problems"] = [r for r in context["rows"] if r["problem"]]
            context["rack_mismatch"] = (sheet[0].RACK_BARCODE
                                        and sheet[0].RACK_BARCODE != scan.get("containerBarcode"))
            request.session[f"ffpe_scan_{extract_sheet}"] = {
                "rack_barcode": scan.get("containerBarcode"),
                "extraction_method": context["rows"][0].EXTRACTION_METHOD,
                    "rows": [{"position": r.POSITION, "labno": r.LABNO, "tube":r.TUBE, "barcode": r.TUBE_BARCODE} for r in context["rows"]],
        }
        return render(request, self.template_name, context)

class FFPEUploadView(LoginRequiredMixin, View):
    template_name = "rack_scan/ffpe_upload.html"
    def get(self, request, extract_sheet):
        return render(request, self.template_name,{"extract_sheet": extract_sheet})

    def post(self, request, extract_sheet):
        data = request.session.pop(f"ffpe_scan_{extract_sheet}", None)
        print(data)
        if data is None:
            messages.error(request, "No scan found. Scan the rack again before uploading.")
            return redirect("ffpe_rack_scan", extract_sheet=extract_sheet)

        now = timezone.now()
        with transaction.atomic(using="Shire_Data"):
            for row in data["rows"]:
                updated = (DNA_EXTRACTS.objects
                           .filter(LABNO=row["labno"], TUBE=row["tube"])
                           .update(TUBE_BARCODE=row["barcode"],
                                   UPDATEDBY=request.user.username[:10],
                                   UPDATEDDATE=now,
                                   UPDATEDTIME=now))
                if updated != 1:
                    raise ValueError(f"Expected 1 row for {row['labno']}/{row['tube']}, updated {updated}")

        messages.success(request, f"Scan for {extract_sheet} uploaded.")
        return redirect("ffpe_upload", extract_sheet=extract_sheet)



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