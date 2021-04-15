from django.urls import path
from schoolport.app_attendance import views

from django.contrib.auth.decorators import login_required

app_name = "app_attendance"
urlpatterns = [
    path('attendance/', login_required(views.App_AttendanceIndexView.as_view()), name='attendance-index'),
    #path('billingcenter/chargemgt/', login_required(views.BillingCenter_ChargeManagement_View.as_view()), name='billingcenter-chargemgt'),
]

