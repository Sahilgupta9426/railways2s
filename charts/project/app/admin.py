from django.contrib import admin
from .models import Bike, Car
# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=['id','car_model','quantity']
@admin.register(Bike)
class CarAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity']
