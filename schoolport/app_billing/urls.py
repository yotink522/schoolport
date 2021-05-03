from django.urls import path
from schoolport.app_billing import views

from django.contrib.auth.decorators import login_required

app_name = "app_billing"
urlpatterns = [
    path('billingcenter/', login_required(views.BillingCenter_Index_View.as_view()), name='billingcenter-index'),
    path('billingcenter/registerstudent', login_required(views.BillingCenter_RegisterStudent_View.as_view()), name='billingcenter-register-student'),
    path('billingcenter/coursesfee', login_required(views.BillingCenter_CoursesFee_View.as_view()), name='billingcenter-courses-fee'),
    path('billingcenter/coursesfee_edit', login_required(views.BillingCenter_CoursesFeeEdit_View.as_view()), name='billingcenter-courses-fee-edit'),
    path('billingcenter/coursesfee_general_edit', login_required(views.BillingCenter_CoursesFeeGeneralEdit_View.as_view()), name='billingcenter-courses-fee-general-edit'),
]

