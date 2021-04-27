from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
class BillingCenter_Index_View(View):
    template_name = "app_billing/index.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            print(context)
            return render(request, "base_admin.html", context)
        



class BillingCenter_ChargeManagement_View(View):
    template_name = "app_billing/chargemgt.html"
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'chargemgt',
        }
        return render(request, self.template_name, context)

