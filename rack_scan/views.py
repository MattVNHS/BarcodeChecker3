import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class FFPEUploadView(LoginRequiredMixin, View):
    template_name = "ffpe_scan/ffpe_scan.html"

    def get(self, request):
        # Just show the page with the Scan button
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

class RackScanView(LoginRequiredMixin, View):
    template_name = "rack_scan/scan.html"

    def get(self, request):
        # Just show the page with the Scan button
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