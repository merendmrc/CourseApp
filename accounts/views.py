from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def user_login(req):
    if req.user.is_authenticated:
        return redirect("index")
    
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = authenticate(req, username= username, password= password)
        
        if user is not None:
            login(req, user)
            return redirect("index")
        else:
            return render(req, template_name="accounts/login.html", context={"error":"username veya parola yanlis"})
    else:
        return render(req, template_name="accounts/login.html")

def user_register(req):
    if req.method == "POST":
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
                    user = User(username= username, email= email, password= password)
                    user.save()
                    print(username)
                    print(password)
                    return redirect("user_login")
        else:
            return render(req, template_name= "accounts/register.html", context={"error":"Şifreler eşleşmiyor."})
    else:
        return render(req, template_name= "accounts/register.html")

def user_logout(req):
    logout(req)
    return redirect("index")