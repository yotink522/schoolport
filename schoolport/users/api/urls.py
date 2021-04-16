from django.urls import path
from schoolport.users.api.views import (
    registration_view,
    userinfo_view,
)

from rest_framework.authtoken.views import obtain_auth_token

app_name = "api_users"

urlpatterns = [
    path('register', registration_view, name="api_user_register"),
    path('login', obtain_auth_token, name="api_user_login"),
    path('userinfo', userinfo_view, name="api_user_info" ),
]

