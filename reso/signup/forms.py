from django import forms


class UserForm(forms.Form):
    langchoices = {
        ("python", "python"),
        ("java", "Java"),
        ("c++", "C++"),
        ("django", "Django"), }
    name = forms.CharField(label='Your name', max_length=100)
    email = forms.CharField(label='Your email', max_length=100)
    #languages = forms.CharField(label='Your languages', max_length=100)
    languages = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=langchoices)
   # extralanguages = forms.CharField(label='Your email', max_length=100)

