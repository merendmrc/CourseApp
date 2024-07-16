from django import forms
from .models import Course

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("__all__")
        labels = {
            "title":"Kurs başlığı",
            "description":"Kurs açıklaması",
            "is_active":"Kurs aktif mi",
            "is_home":"Anasayfa'da gösterilecek mi",
            "slug":"Slug",
            "categories":"Kategori",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }

        error_messages = {
    "title": {
        "required": "Başlık kısmı boş geçilemez!",
        "max_length": "Maximum 50 karakter girebilirsiniz."
    },
    "description": {
        "required": "Açıklama kısmı boş geçilemez!",
        "max_length": "Maximum 500 karakter girebilirsiniz."
    },
    "slug": {
        "required": "Slug kısmı boş geçilemez!",
        "max_length": "Maximum 50 karakter girebilirsiniz."
    },
    "categories": {
        "required": "Kategori seçilmelidir!"
    },
}


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("__all__")
        labels = {
            "title":"Kurs başlığı",
            "description":"Kurs açıklaması",
            "is_active":"Kurs aktif mi",
            "is_home":"Anasayfa'da gösterilecek mi",
            "slug":"Slug",
            "categories":"Kategori",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "categories": forms.SelectMultiple(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }

        error_messages = {
    "title": {
        "required": "Başlık kısmı boş geçilemez!",
        "max_length": "Maximum 50 karakter girebilirsiniz."
    },
    "description": {
        "required": "Açıklama kısmı boş geçilemez!",
        "max_length": "Maximum 500 karakter girebilirsiniz."
    },
    "slug": {
        "required": "Slug kısmı boş geçilemez!",
        "max_length": "Maximum 50 karakter girebilirsiniz."
    },
    "categories": {
        "required": "Kategori seçilmelidir!"
    },
}

class UploadForm(forms.Form):
    image = forms.ImageField()