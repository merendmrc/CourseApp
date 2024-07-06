from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from .models import Course

db = {
    "courses" : [
        {
            "title":"javascript kursu",
            "description":"javascript kurs aciklamasi",
            "imageUrl":"js.jpg",  
            "slug":"javascript-kursu",
            "date":date(2023,11,14),
            "is_active":True,
            "is_updated":False,
        },
        {
            "title":"python kursu",
            "description":"Python programlama dilini öğrenmek ve bu alanda yetkinlik kazanmak isteyenler için hazırlanan Python Programlama Kursu, hem başlangıç seviyesindeki hem de ileri düzeydeki katılımcılara yönelik kapsamlı bir eğitim sunmaktadır. Bu kurs, Python'un temellerinden başlayarak, ileri seviye konulara kadar geniş bir yelpazede bilgi ve beceri kazandırmayı amaçlamaktadır.",
            "imageUrl":"python.png",  
            "slug":"python-kursu",
            "date":date(2023,5,12),
            "is_active":True,
            "is_updated":True,
        },
        {
            "title":"mobil programlama kursu",
            "description":"mobil programlama kurs aciklamasi",
            "imageUrl":"react.jpg",  
            "slug":"mobil-programlama-kursu",
            "date":date(2024,2,6),
            "is_active":False,
            "is_updated":False,
        }
    ],
    "categories": [
        {"id":1, "name":"programlama","slug":"programlama"},
        {"id":2, "name":"web gelistirme","slug":"web-gelistirme"},
        {"id":3, "name":"mobil uygulamalar","slug":"mobil-uygulamalar"},]
}

def index(req):
    courses = Course.objects.filter(is_active=1)
    categories = db["categories"]

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'courses':courses
    })

def detaylar(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} DETAY SAYFASI gozukecek")

def getCoursesByCategoryName(req, category_name):
    try:
        category_text = db[category_name]
        return render(req, template_name='courses/courses.html', context={
            'category_name':category_name,
            'category_text':category_text
        })
    except:
        return HttpResponseNotFound("yanlis kategori secimi")
    
def getCoursesByCategoryId(req, category_id):

    category_list = list(data.keys())
    if(category_id> len(category_list)):
        return HttpResponseNotFound("YANLIS KATEGORI SECIMI")
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category_id',args=[category_name])

    return redirect(redirect_url)