# Generated by Django 5.0.6 on 2024-07-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_category_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
