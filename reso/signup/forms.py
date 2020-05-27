from django import forms
from django_select2.forms import Select2MultipleWidget, ModelSelect2MultipleWidget
from .models import *

class UserForm(forms.Form):
    langchoices = {
        ("python", "python"),
        ("java", "Java"),
        ("c++", "C++"),
        ("django", "Django"), }
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    #languages = forms.CharField(label='Your languages', max_length=100)
    # language = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple, choices=langchoices)
    #lang=forms.ModelMultipleChoiceField(queryset=Skills.objects.all(),widget=Select2MultipleWidget)
    # my_choice = forms.ChoiceField(
    #     widget=ModelSelect2MultipleWidget(
    #         model=Skills,
    #         search_fields=['title__icontains="Go"'],
    #     ))
    #lang=forms.MultipleChoiceField(choices=langchoices,widget=Select2MultipleWidget)

   # extralanguages = forms.CharField(label='Your email', max_length=100)

