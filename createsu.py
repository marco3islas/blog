import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()


username = os.environ.get("DJANGO_SU_NAME", "marco_dev_admin")
email = os.environ.get("DJANGO_SU_EMAIL", "marco3islas@gmail.com")
password = os.environ.get("DJANGO_SU_PASSWORD", "proyectos2025")


if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Super usuario creado.")
else:
    print("El superusuario ya existe")
