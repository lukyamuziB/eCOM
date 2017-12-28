from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Hello customer'
    }
    return render(request, "index.html", context)

def contact(request):
    context = {
        'title': 'this is our contacts page'
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        'title': 'this is our info page'
    }
    return render(request, "index.html", context)



