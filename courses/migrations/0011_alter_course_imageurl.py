# Generated by Django 5.0.6 on 2024-07-16 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_uploadimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='imageUrl',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]