import datetime
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
class TravelForm(forms.Form):
    source=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'id':'source','class':"form-control"}),label=('Source'))
    destination=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'id':'destination','class':'form-control'}),label=('Destination'))
    # date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'MM/DD/YYYY'}),label=('Date'))
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date','class':'form-control datetimepicker-input'}),label=('Date'))
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
class CustomerForm(forms.Form):
    op=(('0', 'Male'),
    ('1', 'Female'),
    ('2', 'Transgender'))
    cname=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),label=('Your Name'))
    email=forms.EmailField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),label=('Your Email'))
    gender=forms.ChoiceField(choices = op)
    age=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Age'}),label=('Age'))
    number=forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'Number'}),label=('Number'))


