from django.urls import path
from schoolport.app_dashboard import views

from django.contrib.auth.decorators import login_required

app_name = "app_dashboard"
urlpatterns = [
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard-view'),
    #path('dashboard/', views.DashboardView.as_view(), name='dashboard-view'),
]
