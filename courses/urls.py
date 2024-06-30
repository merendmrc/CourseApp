from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('list', views.kurslar),
    path('details', views.detaylar),
    path('programlama', views.programlama),
    path('mobil-uygulamalar', views.mobiluygulamalar),
]
