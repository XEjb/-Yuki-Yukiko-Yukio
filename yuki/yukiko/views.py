from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    return render(request, 'yukiko/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'yukiko/about.html', {'title': 'О сайте'})


def categories(request, yukio):
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{yukio}</p>')


def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
