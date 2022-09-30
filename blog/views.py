from django.shortcuts import render

from blog.models import post, categoria
# Create your views here.

def blog(request):

    posts=post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def Categorias(request, categoria_id):

    kategoria=categoria.objects.get(id=categoria_id)
    posts=post.objects.filter(categorias=kategoria)
    return render(request, "blog/categoria.html", {'kategoria':Categorias, 'posts':posts})