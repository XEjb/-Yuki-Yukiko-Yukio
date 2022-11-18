from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "Инфа", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Фидбэк", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'}
        ]


def index(request):
    posts = Yukiko.objects.all()
    cats = Category.objects.all()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'yukiko/index.html', context=context)


def about(request):
    return render(request, 'yukiko/about.html', {'menu': menu, 'title': 'Инфа'})


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse("Фидбэк")


def login(request):
    return HttpResponse('Вход')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(requset, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def show_category(request, cat_id):
    posts = Yukiko.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'yukiko/index.html', context=context)
