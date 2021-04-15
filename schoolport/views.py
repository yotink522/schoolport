from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class HomeView(View):
    '''
    View for redirect to reasons page
    '''
    template_name="pages/home.html"

    def get(self, request):
        return render(request, self.template_name, {})

