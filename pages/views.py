from django.shortcuts import render
from django.http import HttpResponse


def header(request):
    return render(
        request,
        'pages/index.html',
        {
            'header': 'Графический дизайнер Анастасия Радионова',
            'content': 'Тут будут блоки с работами и рисунками'
        }
    )


def content(request):
    return render(
        request,
        'pages/index.html',
        {
            'content': 'Тут будут блоки с работами',
        }
    )


def aboutpage(request):
    return render(
        request,
        'pages/index.html',
        {
            'aboutpage': 'Тут будет страница о авторе'
        }

    )
