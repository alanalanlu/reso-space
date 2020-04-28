from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from .models import *
# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # check whether it's valid:
        print(form)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            lang = form.cleaned_data['languages']
            print(name, email, lang)
            newuser = User(name=name, email=email)
            newuser.save()
            print(newuser)
            for i in range(len(lang)):
                skill=Skills.objects.get(languages=lang[i])
                print(newuser)
                skill.save()
                skill.User.add(newuser)
                print(skill.languages)
            return HttpResponse('recieved')
    else:
        print("false")
    form = UserForm
    return render(request, "signup.html", {'form': form})

def matches(request):
    data = User.objects.filter(chosen=False)
    print(data)
    stu = {
        "match": data
    }
    #print(data[0].User)
    return render(request,"matches.html", stu)