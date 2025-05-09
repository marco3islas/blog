from django.template import context
from django.views import generic
from django.shortcuts import render
from . models import Article
from . forms import ApplicationForm
from random import choice

def index(request):
    articles = Article.objects.all()
    random_article = choice(articles) if articles else None
    context = {
        'articles': articles,
        'random_article': random_article
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def galeria(request):
    images = Article.objects.exclude(image="").order_by('-fecha')
    return render(request, "galeria.html", {"imagenes": images})

def derecha_component(request):
    images = [
        'images/un_anuncio_sobre_zapatos_deportivos3.webp',
        'images/ranas_blackjack.webp',
        'images/cafeteria.webp',
        'images/project_automator.webp',
        'images/images_convert.webp'
    ]
    return render(request, "derecha_component.html", {"imagenes":images})

def contacto(request):
    if request.method == "Post":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Success")
    else:
        form = ApplicationForm()
    return render(request, "contacto.html", {"form": form})

class ArticleDetail(generic.DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"


