from django.urls import path
from schoolport.app_management import views

from django.contrib.auth.decorators import login_required

app_name = "app_management"
urlpatterns = [
    path('management/', login_required(views.App_ManagementIndexView.as_view()), name='management-index'),
]

