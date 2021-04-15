from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

# Create your views here.
class DashboardView(View):
    template_name = "app_dashboard/index.html"
    def get(self, request):
        context = {
            'sidebar':'dashboard',
            'navbar':'none',
        }
        return render(request, self.template_name, context)
        #return render(request, self.template_name, {'sidebar_select':'dashboard'})

