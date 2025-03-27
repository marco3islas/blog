from django.template import context
from django.views import generic
from django.shortcuts import render
from . models import Article
from . forms import ApplicationForm

def index(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})

def about(request):
    return render(request, "about.html")

def galeria(request):
    images = Article.objects.exclude(image="").order_by('-fecha')
    return render(request, "galeria.html", {"imagenes": images})

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


