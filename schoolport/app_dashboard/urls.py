from django.urls import path
from schoolport.app_dashboard import views

from django.contrib.auth.decorators import login_required

app_name = "app_dashboard"
urlpatterns = [
    path('main/', login_required(views.DashboardMainView.as_view()), name='dashboard-main-view'),
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard-view'),
    #path('dashboard/', views.DashboardView.as_view(), name='dashboard-view'),
]
