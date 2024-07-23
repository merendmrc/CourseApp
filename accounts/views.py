from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserLoginForm


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
        name = req.POST["name"]
        last_name = req.POST["last_name"]
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        repassword = req.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username = username).exists():
                return render(req, template_name= "accounts/register.html", context={"error":"Kullanıcı adı kullanılamıyor, Farklı bir kullanıcı adı deneyiniz."})
            else:
                if User.objects.filter(email= email):
                    return render(req, template_name= "accounts/register.html", context={"error":"Email kullanılamıyor, Farklı bir email deneyiniz."})
                else:
                    user = User(first_name= name, last_name= last_name, username= username, email= email)
                    user.set_password(password)
                    user.save()
                    messages.success(req, "Kaydınız tamamlandı. Giriş yapabilirsiniz..")
                    return redirect("user_login")
        else:
            return render(req, template_name= "accounts/register.html", context={"error":"Şifreler eşleşmiyor."})
    else:
        return render(req, template_name= "accounts/register.html")

def user_logout(req):
    logout(req)
    messages.warning(req, "Başarıyla çıkış yaptınız.")
    return redirect("index")