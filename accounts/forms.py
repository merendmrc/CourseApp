from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms import widgets
from django.forms import forms
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
    
    def confirm_login_allowed(self, user):
        if user.username.startswith("ğ"):
            raise forms.ValidationError("Bu kullanıcı adı ile giriş yapamazsınız")

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email")

    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["first_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget = widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email = email).exists():
            self.add_error("email","email daha önce alınmış")

        return email

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, user: AbstractBaseUser | None, *args, **kwargs) -> None:
        super().__init__(user, *args, **kwargs)
        self.fields["old_password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password1"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["new_password2"].widget = widgets.PasswordInput(attrs={"class":"form-control"})