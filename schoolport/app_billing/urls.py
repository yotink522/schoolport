from django.urls import path
from schoolport.app_billing import views

from django.contrib.auth.decorators import login_required

app_name = "app_billing"
urlpatterns = [
    path('billingcenter/', login_required(views.BillingCenter_Index_View.as_view()), name='billingcenter-index'),
    #path('billingcenter/chargemgt/', login_required(views.BillingCenter_ChargeManagement_View.as_view()), name='billingcenter-chargemgt'),
]

