from django.urls import path
from schoolport.app_studying import views

from django.contrib.auth.decorators import login_required

app_name = "app_studying"
urlpatterns = [
    path('studying/', login_required(views.App_StudyingIndexView.as_view()), name='studying-index'),
]

