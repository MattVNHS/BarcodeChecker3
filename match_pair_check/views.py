from match_pair_check.forms import *
from match_all_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.forms.models import inlineformset_factory
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class Match_pair_checkCreateView(CreateView):
    model = Check
    fields = ["worksheet",]
    template_name = 'match_all_check/match_all_check.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['total_forms'] = int(self.request.POST['barcode_set-TOTAL_FORMS'])
            data['barcodes'] = PairCheckFormset(self.request.POST)
        else:
             data["barcodes"] = inlineformset_factory(Check, Barcode, formset=BaseInlineCheckFormSet, can_delete_extra=False,
                                                      form=BarcodePairForm, extra=self.kwargs['barcode_count'],)
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
             messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data(form=form, formset=barcodes))

    def form_valid(self, form):
        context = self.get_context_data()
        barcodes = context['barcodes']
        barcodes_entered = [True for x in barcodes if x.has_changed()]
        if len(barcodes_entered) % 2 != 0:
            messages.warning(self.request, 'Cannot have an odd number of barcodes entered')
            return self.form_invalid(form)
            # barcodes.errors.append('Check Failed - Barcodes do not match')

        self.object = form.save(commit=False)
        self.object.user, self.object.barcode_count = self.request.user, context['total_forms']
        self.object.save()
        if barcodes.is_valid():
            barcodes.instance = self.object
            barcodes.save()
            for x in range(len(barcodes)):
                if x % 2 == 0:
                    barcodes[x].instance.comparisonId = barcodes[x + 1].instance.pk
                else:
                    barcodes[x].instance.comparisonId = barcodes[x - 1].instance.pk
            barcodes.save()

            for x in range(0,len(barcodes),2):
                barcode_1 = barcodes[x].instance
                try:
                    barcode_2 = Barcode.objects.get(pk=barcode_1.comparisonId)
                except ObjectDoesNotExist:
                    break
                if barcode_1.barcode != barcode_2.barcode:
                    barcodes.errors.append('Check Failed - Barcodes do not match')
                    break

            for error in barcodes.errors:
                messages.warning(self.request, error)
            if "Check Failed - Barcodes do not match" not in barcodes.errors:
                messages.success(self.request, 'Check Passed')
                self.object.check_pass = True
                self.object.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

