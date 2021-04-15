from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

# Create your views here.
class App_InteractionIndexView(View):
    template_name = "app_interaction/index.html"
    def get(self, request):
        context = {
            'sidebar':'app_interaction',
            'navbar':'',
        }
        return render(request, self.template_name, context)

