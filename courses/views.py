from datetime import date
from django.shortcuts import get_object_or_404, render,redirect
from .models import Course,Category, UploadImage
from django.core.paginator import Paginator
from django.db.models import Q
from courses.forms import CreateCourseForm, EditCourseForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

def is_super(user):
    return user.is_superuser

def index(req):
    courses = Course.objects.filter(is_home = 1).order_by("-is_active")
    categories = Category.objects.all()
 
    paginator = Paginator(courses, 10)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)
    
    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'page_obj': page_obj,
        'course_count':len(courses)
    })

def tum(req):
    courses = Course.objects.all().order_by("-is_active")
    categories = Category.objects.all()

    paginator = Paginator(courses, 10)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(req, template_name="courses/index.html", context={
        'categories': categories,
        'page_obj': page_obj,
        'course_count':len(courses)        
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
    courses = Course.objects.filter(categories__slug=slug).order_by("-is_active")
    categories = Category.objects.all()

    paginator = Paginator(courses, 10)
    page = req.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(req, template_name="courses/list.html", context={
        "page_obj" : page_obj,
        "categories" : categories,
        "selected_category_id" : Category.objects.get(slug=slug).id,
        'course_count':len(courses)
    })

@user_passes_test(is_super)
def create_course(req):
    if req.method == "POST":
        form = CreateCourseForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(req, "Kurs başarıyla eklendi!")
            return redirect("courses_details", form.cleaned_data.get("slug"))
    else:
        form = CreateCourseForm()
    return render(req, template_name="courses/create_course.html",context={"form":form})

def course_list(req):
    courses = Course.objects.all()
    return render(req, template_name="courses/course_list.html", context={
        "courses": courses
    })

@user_passes_test(is_super)
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

@user_passes_test(is_super)
def course_delete(req, id):
    course = get_object_or_404(Course, pk=id)
    if req.method == "POST":
        course.delete()
        return redirect("course_list")
    return render(req, template_name="courses/course_delete.html", context={"course":course})