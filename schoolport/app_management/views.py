from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.template.loader import render_to_string
from django.http import JsonResponse

# Create your views here.
class App_ManagementIndexView(View):
    template_name = "app_management/index.html"
    data = dict()
    def get(self, request):
        context = {
            'sidebar':'app_management',
            'navbar':'',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)


class App_Management_ManageStudentView(View):
    template_name = "app_management/managestudent.html"
    data = dict()
    def get(self, request):
        context = {
            'sidebar':'app_management',
            'navbar':'',
            'appname': 'managestudent',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

class App_Management_ManageClassView(View):
    template_name = "app_management/manage_class.html"
    data = dict()
    def get(self, request):
        context = {
            'sidebar':'app_management',
            'navbar':'',
            'appname': 'manageclass',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

