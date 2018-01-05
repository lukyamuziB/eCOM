from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import contactsForm, registerForm, loginForm


def index(request):
    context = {
        'title': 'Hello customer'
    }
    return render(request, "index.html", context)

def contact(request):
    forms = contactsForm(request.POST or None)
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


def register(request):
    forms = registerForm(request.POST  or None)
    context = {
        'title':'Register here',
        'form':forms
    }
    if forms.is_valid():
        print(forms.cleaned_data)
        print(forms.cleaned_data.get('name'))
    else:    
        print("soo")
    return render(request, "auth/register.html", context)


def login(request):
    forms = loginForm(request.POST or None)
    context = {
        'title':'Log in here',
        'form':forms
    }
    if forms.is_valid():
        username = forms.cleaned_data.get('username')
        password = forms.cleaned_data.get('password')
        user = authenticate(request, username = username, password = password)
        print(user)
        if user is not None:
            login(request, user)
            print('successful')
            return redirect('/login')
        else:
            print('error')
    return render(request, "auth/login.html", context)
