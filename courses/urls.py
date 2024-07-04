from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('<kurs_adi>', views.detaylar),
    path('kategori/<int:category_id>', views.getCoursesByCategoryId),   
    path('kategori/<str:category_name>', views.getCoursesByCategoryName, name='courses_by_category_id'),
]
