from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from allauth.account.views import SignupView

User = get_user_model()

# class AccountSignupView(SignupView):
#     template_name = "account/signup.html"

#     # You can also override some other methods of SignupView
#     # Like below:
#     # def form_valid(self, form):
#     #     ...
#     #
#     # def get_context_data(self, **kwargs):
#     #     ...
#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         return HttpResponseRedirect(reverse('dashboard:dashboard-view'))

# account_signup_view = AccountSignupView.as_view()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        #return reverse("users:detail", kwargs={"username": self.request.user.username})
        #return reverse("dashboard:dashboard-view", kwargs={"userinfo": self.request.user})
        return reverse("app_dashboard:dashboard-view")


user_redirect_view = UserRedirectView.as_view()


