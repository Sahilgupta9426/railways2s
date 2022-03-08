from django.contrib import admin
from .models import Bike, Car, Country
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=['id','car_model','quantity']
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display=['id','country','popularity']