from django.shortcuts import render
from django.http import HttpResponse

def iletisim(req):
    return HttpResponse("merendmrcc@gmail.com")

def hakkimizda(req):
    return HttpResponse("hakkimizda")

def home(req):
    return HttpResponse("anasayfa")

