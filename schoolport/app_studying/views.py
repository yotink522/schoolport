from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin

# Create your views here.
class App_StudyingIndexView(View):
    template_name = "app_studying/index.html"
    def get(self, request):
        context = {
            'sidebar':'app_studying',
            'navbar':'',
        }
        return render(request, self.template_name, context)

