from django.shortcuts import render


def index(request):
    return render(request, 'my_app/static_example.html', {})