from django.shortcuts import render
from django.http import HttpResponse


def index(req):
    return render(req, template_name="pages/index.html")

def contact(req):
    return render(req, template_name="pages/contact.html")

def about(req):
    return render(req, template_name="pages/about.html")


