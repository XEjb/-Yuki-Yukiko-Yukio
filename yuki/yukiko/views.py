from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .forms import *
from .models import *

menu = [{'title': "Инфа", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Фидбэк", 'url_name': 'contact'},
        {'title': "Вход", 'url_name': 'login'}
        ]


def index(request):
    posts = Yukiko.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'yukiko/index.html', context=context)


def about(request):
    return render(request, 'yukiko/about.html', {'menu': menu, 'title': 'Инфа'})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    return render(request, 'yukiko/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse("Фидбэк")


def login(request):
    return HttpResponse('Вход')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Yukiko, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'yukiko/post.html', context=context)


def show_category(request, cat_id):
    posts = Yukiko.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'yukiko/index.html', context=context)
