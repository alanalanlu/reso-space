from django.shortcuts import render
from .forms import userForm
from django.http import HttpResponse
from .models import *
# Create your views here.


def UserForm(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            lang = form.cleaned_data['languages']
            newuser = User(name=name, email=email, languages=lang).save()
            print(name, email, lang)
            print(type(name))
            return HttpResponse('recieved')
    return HttpResponse('Not recieved')


def Signup(request):
    context = {}
    return render(request, "signup.html", context)
