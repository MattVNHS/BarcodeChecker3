from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from django.apps import apps
from itertools import chain
from operator import attrgetter
from mysite.settings import INSTALLED_APPS
from base_check.models import Check, SampleBarcode
from match_all_check.models import MatchAllBarcode


class AuditView(ListView):
    template_name = 'audit/base_audit.html'

    def get_check_apps(self):
        check_apps = []
        for app in INSTALLED_APPS:
            if app.endswith("_check"):
                check_apps.append(app)
        return check_apps


    def get_check_subclasses(self, abstract_class):
        result = []
        for app in self.get_check_apps():
            for model in apps.get_app_config(app).get_models():
                if issubclass(model, Check) and model is not abstract_class:
                    result.append(model)
        return result

    def get_check_subclasses(self, abstract_class):
        result = []
        for app in self.get_check_apps():
            for model in apps.get_app_config(app).get_models():
                if issubclass(model, Check) and model is not abstract_class:
                    result.append(model)
        return result

    def get_queryset(self):
        query = self.request.GET.get("q")

        queryset_list = []
        for check_type in self.get_check_subclasses(self):
            queryset = check_type.objects.filter(
                Q(worksheet__worksheet_number__icontains=query)
                | Q(user__username__icontains=query)
                | Q(barcodes__in=query)
            )
            queryset_list.append(queryset)

        # Do I create a second search for barcodes? Or incorporate barcodes in the check search?
        # Create a hyperlink on audit page to individual check details?

        # lookup related names and FK's

        combined_queryset = list(chain(*queryset_list))
        ordered_queryset = sorted(combined_queryset, key=attrgetter('dateTime_check'), reverse=True)
        return ordered_queryset
