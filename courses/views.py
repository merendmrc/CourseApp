from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse

data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web gelistirme kategorisine ait kurslar",
    "mobil":"mobil gelistirme kategorisine ait kurslar"
}


def kurslar(req):
    category_list = list(data.keys())
    list_items = ""
    for category in category_list:
        redirect_url = reverse('courses_by_category_id',args=[category])
        list_items += f"""
        <li>
        <a href="{redirect_url}">
        {category}
        </a>
        </li>"""

        html_content = f"<h1>Kurs Kategorileri</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html_content)

def detaylar(req, kurs_adi):
    return HttpResponse(f"{kurs_adi} DETAY SAYFASI gozukecek")

def getCoursesByCategoryName(req, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlis kategori secimi")
    
def getCoursesByCategoryId(req, category_id):

    category_list = list(data.keys())
    if(category_id> len(category_list)):
        return HttpResponseNotFound("YANLIS KATEGORI SECIMI")
    category_name = category_list[category_id - 1]

    redirect_url = reverse('courses_by_category_id',args=[category_name])

    return redirect(redirect_url)