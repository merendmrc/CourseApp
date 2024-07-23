from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.forms import forms

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("ğ"):
            raise forms.ValidationError("Bu kullanıcı adı ile giriş yapamazsınız")


