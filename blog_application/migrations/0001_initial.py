# Generated by Django 5.1.3 on 2024-11-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Titulo')),
                ('subtitle', models.CharField(blank=True, max_length=100, verbose_name='Subtitulo')),
                ('resumen', models.CharField(max_length=130, verbose_name='Resumen')),
                ('article', models.TextField()),
                ('author', models.CharField(max_length=20, verbose_name='Autor')),
                ('fecha', models.DateField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
    ]
