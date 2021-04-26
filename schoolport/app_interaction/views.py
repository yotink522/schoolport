from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
class App_InteractionIndexView(View):
    template_name = "app_interaction/index.html"
    data = dict()

    def get(self, request):
        context = {
            'sidebar':'app_interaction',
            'navbar':'',
        }
        
        self.data['html_index'] = render_to_string(self.template_name, {})
        return JsonResponse(self.data)

