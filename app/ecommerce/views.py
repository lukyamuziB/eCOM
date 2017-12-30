from django.shortcuts import render
from django.http import HttpResponse

from .forms import contactsForm


def index(request):
    context = {
        'title': 'Hello customer'
    }
    return render(request, "index.html", context)

def contact(request):
    forms = contactsForm()
    context = {
        'title': 'this is our contacts page',
        'form': forms
    }
    return render(request, "contacts/contacts.html", context)

def about(request):
    context = {
        'title': 'this is our info page'
    }
    return render(request, "index.html", context)
