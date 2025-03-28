# Generated by Django 5.1.3 on 2024-12-30 18:19

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
