from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')


def bom(request):
    return render(request, 'blog/serte.html')