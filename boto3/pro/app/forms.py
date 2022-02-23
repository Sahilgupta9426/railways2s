from django import forms

class Profile(forms.Form):
    picture1=forms.ImageField()
    picture2=forms.ImageField()

class TextCapForm(forms.Form):
    pic1=forms.ImageField()

class Mask(forms.Form):
    pic1=forms.ImageField()
    