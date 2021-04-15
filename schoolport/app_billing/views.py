from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

# Create your views here.
class BillingCenter_Index_View(View):
    template_name = "app_billing/index.html"
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'releasefee',
        }
        return render(request, self.template_name, context)

class BillingCenter_ChargeManagement_View(View):
    template_name = "app_billing/chargemgt.html"
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'chargemgt',
        }
        return render(request, self.template_name, context)

