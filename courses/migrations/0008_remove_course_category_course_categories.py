# Generated by Django 5.0.6 on 2024-07-08 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_category_alter_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(to='courses.category'),
        ),
    ]