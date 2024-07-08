from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name='courses_details'),
    path('kategori/<str:slug>', views.getCoursesByCategoryName, name='courses_by_category_id'),
]
