from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')


def third_page(request):
    return render(request, 'infra_app/third_page.html')
