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
            return render(request, "base_admin.html", context)
        
# Register Student View
class BillingCenter_RegisterStudent_View(View):
    template_name = "app_billing/registerstudent.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'registerstudent',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Index View
class BillingCenter_CoursesFee_View(View):
    template_name = "app_billing/courses_fee.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfee',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Edit View
class BillingCenter_CoursesFeeEdit_View(View):
    template_name = "app_billing/courses_fee_edit.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfeeedit',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)

# Courses and Fee Edit View
class BillingCenter_CoursesFeeGeneralEdit_View(View):
    template_name = "app_billing/courses_fee_generaledit.html"
    data = dict()
    
    def get(self, request):
        context = {
            'sidebar':'billingcenter',
            'navbar':'',
            'appname': 'coursesfeegeneraledit',
        }

        if request.is_ajax():
            self.data['html_index'] = render_to_string(self.template_name, {})
            return JsonResponse(self.data)
        else:
            return render(request, "base_admin.html", context)
