from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name='courses_details'),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),   
    path('kategori/<str:category_name>', views.getCoursesByCategoryName, name='courses_by_category_id'),
]
