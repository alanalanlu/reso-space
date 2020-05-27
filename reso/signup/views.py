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
        if request.method == "POST":
            print("___________-")
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            # lang = form.cleaned_data['language']
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
    
    #tracks number of overlapping skills btwn users
    # overlap=[]
    # for i in range(len(all_user)):
    #     overlap.append((0,all_user[i]))
    overlap={}
    # for i in range(1,len(all_user)):
    #      overlap[all_user[i].email]=0
    print(overlap)
    count=5
    all_user = User.objects.filter(chosen=False)
    all_skill=Skills.objects.all()
    while(len(all_user)>2 and count>0):
        all_user = User.objects.filter(chosen=False)
        all_skill=Skills.objects.all()
        count-=1
        lead=all_user[0]
        user_skill=lead.skill.all()
        print(lead,"<=== lead")
        print(user_skill,"<=== user_skill")
        #get all skills of lead and find users in each skill
        for i in range(len(user_skill)):
            user_skill_instance=all_user.filter(skill=user_skill[i])
            print(user_skill[i])
            print(user_skill_instance)
            for x in user_skill_instance:
                #Uses django model instance as key
                if x not in overlap:
                    overlap[x]=1
                else:
                    overlap[x]+=1
        print(overlap)
        newsquad = Squad()
        newsquad.save()
        #biggest overlap=user w/ most common skills
        # better way pick highest overlap
        if len(overlap)!=0:
            common_user=max(overlap, key=overlap.get) 
            print("common1",common_user)
            common_user.team=newsquad
            common_user.chosen=True
            common_user.save()
            overlap.pop(common_user)
            lead.team=newsquad
            lead.chosen=True
            lead.save()
        #only if overlap is long enough
        if len(overlap)!=0:
            common_user=max(overlap, key=overlap.get) 
            print("common2",common_user)
            common_user.team=newsquad
            common_user.chosen=True
            common_user.save()
            overlap.pop(common_user)
            print(common_user.team)
        print("UserSet===>",newsquad.user_set.all())
    overlap={}
    #common_user.chosen=True
    for i in User.objects.filter(chosen=True):
        i.chosen=False
        i.save()
    stu = {
        "match": ["a","a"]
    }
    return render(request,"matches.html", stu)


