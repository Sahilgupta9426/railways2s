from django.db import models

# Create your models here.
class Car(models.Model):
    op=(('0', 'Ford Bronco Outer Banks SUV 2021'),
    ('1', 'Ford C-Max SEL Hybrid MPV 2013'),
    ('2', 'Ford Bronco Sport Base SUV 2021'),
    ('3','Ford C-Max Energi Titanium Mini MPV'),
    ('4','Ford C-Max Grand MPV 2011')
    )
    
    car_model=models.CharField(max_length=100,choices=op)
    quantity=models.IntegerField()
class Bike(models.Model):
    bop=(('0', 'TVS'),
    ('1', 'BMW'),
    ('2', 'Hero'),
    ('3','Honda'),
    ('4','Bennelli')
    )
    name=models.CharField(max_length=11,choices=bop)
    quantity=models.IntegerField()