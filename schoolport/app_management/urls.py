from django.urls import path
from schoolport.app_management import views

from django.contrib.auth.decorators import login_required

app_name = "app_management"
urlpatterns = [
    path('management/', login_required(views.App_ManagementIndexView.as_view()), name='management-index'),
    path('management/managestudent', login_required(views.App_Management_ManageStudentView.as_view()), name='management-manage-student'),
    path('management/manageclass', login_required(views.App_Management_ManageClassView.as_view()), name='management-manage-class'),
]

