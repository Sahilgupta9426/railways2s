from pyexpat import model
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .models import Bike, Car, Country
# Create your views here.
def home(request):
    
    return render(request,'home.html')
def piechart(request):
    datas=Car.objects.all()
    listcar=[]
    for car in datas:
        
        que=car.quantity
        model=car.get_car_model_display()
        
        
        listcar.append([model,que])
    print(listcar)
    title="Total Ford Cars Model Sell"
    # data=[['Ford Bronco Outer Banks SUV 2021',10],['Ford Bronco Outer Banks SUV 2021', 10],['Ford Bronco Sport Base SUV 2021', 9],['Ford C-Max Energi Titanium Mini MPV', 1],['Ford C-Max Grand MPV 2011', 2]]
    
    
    
    
    ajaxdata={}
    ajaxdata["html_form"]=render_to_string('include/piechart.html', {
                'data':listcar,'title':title
            },request=request)
    return JsonResponse(ajaxdata)

def vegachart(request):
    datas=Bike.objects.all()
    listcar=[]
    for bike in datas:
        
        que=bike.quantity
        name=bike.get_name_display()
        
        
        listcar.append([name,que])
    print(listcar)
    
    ajaxdata={}
    ajaxdata["html_form"]=render_to_string('include/vegachart.html', {'data':listcar},request=request)
    return JsonResponse(ajaxdata)

    
def geochart(request):
    ajaxdata={}
    data=[
            ['Country', 'Popularity']
          ]
    datas=Country.objects.all()
    for country in datas:
        
        que=country.popularity

        name=country.get_country_display()
        
        
        data.append([name,que])
    print(data)
    ajaxdata["html_form"]=render_to_string('include/geochart.html', {'data':data},request=request)
    return JsonResponse(ajaxdata)
