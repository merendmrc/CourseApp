from datetime import date
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse

db = {
    "courses" : [
        {
            "title":"javascript kursu",
            "description":"javascript kurs aciklamasi",
            "imageUrl":"https://assets-btkakademi-gov-tr.akamaized.net/api/gallery/51/b4ecb192-1e71-428d-8f40-a4eb05862bdb/78.jpg?t=1641991152632",  
            "slug":"javascript-kursu",
            "date":date(2023,11,14),
            "is_active":True,
            "is_updated":False,
        },
        {
            "title":"python kursu",
            "description":"python kurs aciklamasi",
            "imageUrl":"https://assets-btkakademi-gov-tr.akamaized.net/api/gallery/51/799d49f3-287b-444a-adc8-e73afc4ceed8/76_0x220.jpg?t=1640260383870",  
            "slug":"python-kursu",
            "date":date(2023,5,12),
            "is_active":True,
            "is_updated":True,
        },
        {
            "title":"mobil programlama kursu",
            "description":"C# kurs aciklamasi",
            "imageUrl":"https://assets-btkakademi-gov-tr.akamaized.net/api/gallery/51/10aff21b-0c0b-4bc4-b68c-dfda1ac33cb4/94.jpg?t=1640262259134",  
            "slug":"mobil-programlama-kursu",
            "date":date(2024,2,6),
            "is_active":False,
            "is_updated":False,
        }
    ],
    "categories": [
        {"id":1, "name":"programlama","slug":"programlama"},
        {"id":2, "name":"web gelistirme","slug":"web gelistirme"},
        {"id":3, "name":"mobil uygulamalar","slug":"mobil uygulamalar"},]
}

def index(req):
    courses = [course for course in db["courses"] if course["is_active"]]
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