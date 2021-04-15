from django.urls import path
from schoolport.app_interaction import views

from django.contrib.auth.decorators import login_required

app_name = "app_interaction"
urlpatterns = [
    path('interaction/', login_required(views.App_InteractionIndexView.as_view()), name='interaction-index'),
]

