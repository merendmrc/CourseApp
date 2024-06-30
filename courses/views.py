from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def kurslar(req):
    return HttpResponse("kurslar")

def detaylar(req):
    return HttpResponse("detaylar burada gozukecek")

def programlama(req):
    return HttpResponse("programlama kurslari burada gozukecek")

def mobiluygulamalar(req):
    return HttpResponse("mobil uygulama kurslari burada gozukecek")