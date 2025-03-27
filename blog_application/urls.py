from django.conf import settings
from django.urls import path, include
from .import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path("article/<int:pk>/", views.ArticleDetail.as_view(), name='article_detail'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
