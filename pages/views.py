from django.shortcuts import render
from django.http import HttpResponse



def my_first_simple_view(request):
    return render(
        request,
        'pages/index.html',
    {
        'header' : 'Intel',
    }
    )
