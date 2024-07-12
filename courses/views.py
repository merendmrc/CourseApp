from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from .models import Course,Category
from django.core.paginator import Paginator
from django.db.models import Q

def index(req):
    courses = Course.objects.filter(is_home = 1)
    categories = Category.objects.all()

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'courses': courses
    })

def search(req):
    if "q" in req.GET and req.GET["q"] != "":
        q = req.GET["q"]
        courses = Course.objects.filter(Q(title__contains= q) | Q(description__contains= q)).order_by("is_active")
        categories = Category.objects.all()
    else:
        return redirect("/kurslar") 

    return render(req, template_name="courses/search.html", context={
        "courses" : courses,
        "categories" : categories,
    })

def details(req, slug):
    course = get_object_or_404(Course, slug=slug)
    context ={
        'course': course
    }
    return render(req, template_name="courses/details.html", context=context)


def getCoursesByCategoryName(req, slug):
    kurslar = Course.objects.filter(categories__slug=slug).order_by("is_active")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(req, template_name="courses/list.html", context={
        "page_obj" : page_obj,
        "categories" : kategoriler,
        "selected_category_id" : Category.objects.get(slug=slug).id
    })


def create_course(req):
    return render(req, template_name="courses/create_course.html")