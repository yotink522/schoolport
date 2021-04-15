from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from allauth.account.forms import SignupForm, LoginForm
from django import forms
from .models import User

User = get_user_model()

class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class MyCustomLoginForm(LoginForm):
    # class Meta:
    #     fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        try:
            if 'instance' in kwargs:
                self.id = kwargs['instance'].id
        except Exception:
            self.id = None
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)


class MyCustomSignupForm(SignupForm):
    name = forms.CharField(label='Full Name', max_length=255)
    username = forms.CharField(label='UserID', max_length=255)
    email = forms.EmailField(max_length=255)
    phone_number = forms.CharField(label='Phone Number', max_length=20)
    #gender = forms.ChoiceField(label='Gender', choices=User.GENDER_CHOICES)

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'phone_number')

    def __init__(self, *args, **kwargs):
        try:
            if 'instance' in kwargs:
                self.id = kwargs['instance'].id
        except Exception:
            self.id = None
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        
        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'form-control mytext'})
            

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user