from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from .models import Course,Category, UploadImage
from django.core.paginator import Paginator
from django.db.models import Q
from courses.forms import CreateCourseForm, EditCourseForm, UploadForm
from random import randint
from os import path

def index(req):
    courses = Course.objects.filter(is_home = 1).order_by("-is_active")
    categories = Category.objects.all()

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'courses': courses
    })

def tum(req):
    courses = Course.objects.all().order_by("-is_active")
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
   
    if req.method == "POST":
        form = CreateCourseForm(req.POST, req.FILES)
        
        if form.is_valid():
            form.save()
    else:
        form = CreateCourseForm()
    return render(req, template_name="courses/create_course.html",context={"form":form})

def course_list(req):
    courses = Course.objects.all()
    return render(req, template_name="courses/course_list.html", context={
        "courses": courses
    })

def course_edit(req, id):
    course = get_object_or_404(Course, pk=id)
    if req.method == "POST":
        form = EditCourseForm(req.POST, req.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = EditCourseForm(instance=course)
    return render(req, template_name="courses/course_edit.html", context={
        "form":form 
    })

def course_delete(req, id):
    course = get_object_or_404(Course, pk=id)
    if req.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(req, template_name="courses/course_delete.html", context={"course":course})

def upload(req):
    if req.method == "POST":
        uploaded_image = req.FILES["image"]
        form = UploadForm(req.POST, req.FILES)

        if form.is_valid():
            model = UploadImage(image= req.FILES["image"])
            model.save()
    else:
        form = UploadForm()
    return render(req, template_name="courses/upload.html", context={"form":form})
