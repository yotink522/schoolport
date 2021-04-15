from typing import Any

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.conf import settings
from django.http import HttpRequest
from django.forms import ValidationError

class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
    
    def get_login_redirect_url(self, request):
        path = "/dashboard/"
        return path

    # def clean_username(self, username):
    #     if len(username) > 3:
    #         raise ValidationError('Error')
    #     return DefaultAccountAdapter.clean_username(self, username)

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)
