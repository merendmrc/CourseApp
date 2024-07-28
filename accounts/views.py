from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import UserLoginForm, NewUserForm, ChangePasswordForm


def user_login(req):
    if req.user.is_authenticated:
        return redirect("index")
    
    if req.method == "POST":
        form = UserLoginForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(req, username= username, password= password)

            if user is not None:
                login(req, user)
                nextUrl = req.GET.get("next",None)  
                if nextUrl is None:
                    return redirect("index")
                else:
                    return redirect(nextUrl)
            else:
                form = UserLoginForm()
                return render(req, template_name="accounts/login.html", context={"form":form})
        else:
            return render(req, template_name="accounts/login.html", context={"form":form})
    else:
        form = UserLoginForm()
        return render(req, template_name="accounts/login.html", context={"form":form})

def user_register(req):
    if req.method == "POST":
        form = NewUserForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect("user_login")
        
        else:
            return render(req, template_name="accounts/register.html", context={"form":form})

    else:
        form = NewUserForm()
        return render(req, template_name="accounts/register.html", context={"form":form})

def user_logout(req):
    logout(req)
    messages.warning(req, "Başarıyla çıkış yaptınız.")
    return redirect("index")

def change_password(req):
    if req.method == "POST":
        form = PasswordChangeForm(req.user, req.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req, user)
            messages.success(req, "parola başarıyla güncellendi.")
            return redirect("change_password")
        else:
            return render (req, template_name="accounts/change_password.html", context={"form":form} )
    form = ChangePasswordForm(req.user)
    return render (req, template_name="accounts/change_password.html", context={"form":form})
