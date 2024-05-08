from match_pair_check.forms import *
from match_all_check.models import *
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class MatchPairCheckView(CreateView):
    model = MatchPairCheck
    fields = ["worksheet",]
    template_name = 'match_all_check/match_all_check.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['barcodes'] = postFormset(self.request.POST)
        else:
            data["barcodes"] = getFormset(self.kwargs['barcode_count'])
        return data

    def form_invalid(self, form):
        barcodes = self.get_context_data()['barcodes']
        messages.warning(self.request, form.errors)
        for error in barcodes.errors:
            messages.warning(self.request, error)
        return self.render_to_response(self.get_context_data())

    def form_valid(self, form):
        barcodes = self.get_context_data()['barcodes']
        barcodes_entered = [True for x in barcodes if x.has_changed()]
        if len(barcodes_entered) % 2 != 0:
            messages.warning(self.request, 'Cannot have an odd number of barcodes entered')
            return self.form_invalid(form)

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if barcodes.is_valid():
            barcodes.instance = self.object
            barcodes.save()
            # assign comparisonId's to barcode instances.
            # if x % 2 == 0: then x is a multiple of 2 (or is 0)
            # therefore its comparisonId should be the next barcodes pk. This is reversed if x % 2 == 0: is False
            # barcodes[0].comparisonId should be barcodes[1] and barcodes[1].comparisonId should be barcodes[0]
            # there is probably a better way of doing this....
            for x in range(len(barcodes)):
                if x % 2 == 0:
                    barcodes[x].instance.comparisonId = barcodes[x + 1].instance
                else:
                    barcodes[x].instance.comparisonId = barcodes[x - 1].instance
            barcodes.save()

            for error in barcodes.errors:
                messages.warning(self.request, error)

            if self.object.checkPassFail():
                messages.success(self.request, 'Check Passed')
            else:
                messages.warning(self.request, 'Check Failed - Barcodes do not match')

        else:
            return self.form_invalid(form)
        return super().form_valid(form)

