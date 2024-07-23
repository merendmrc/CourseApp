from django.shortcuts import redirect, render
from django.http import HttpResponse



def index(req):
    return redirect("index")

def contact(req):
    return render(req, template_name="pages/contact.html")

def about(req):
    return render(req, template_name="pages/about.html")


