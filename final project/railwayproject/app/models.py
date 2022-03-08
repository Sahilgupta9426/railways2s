from django.db import models

from django.contrib.auth.models import User



# Create your models here.
class Travel_Schedule(models.Model):
    
    train_no=models.IntegerField(primary_key=True)
    train_name=models.CharField(max_length=100)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    arrival_time=models.CharField(max_length=30)
    fare=models.IntegerField()
class Train(models.Model):
    id=models.IntegerField(primary_key=True)
    seat1=models.IntegerField()
    
    sid=models.ForeignKey("Travel_Schedule",on_delete=models.CASCADE)

class Booking(models.Model):
    op=(('0', 'Male'),
    ('1', 'Female'),
    ('2', 'Transgender'))
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=15,choices=op)
    number=models.CharField(max_length=11)
    email=models.CharField(max_length=100)
    seat_no=models.CharField(max_length=4,blank=True)
    journey_date=models.CharField(max_length=20,blank=True)
    amount=models.IntegerField(blank=True)
    p_status=models.BooleanField(default=False)
    s_id=models.ForeignKey(Travel_Schedule,on_delete=models.CASCADE)
    order_id=models.CharField(max_length=200,unique=True)
    user=models.ForeignKey('auth.User', related_name='+',on_delete=models.CASCADE)
class Transaction(models.Model):
    payment_id=models.CharField(max_length=200,unique=True)
    user=models.ForeignKey('auth.User', related_name='+',on_delete=models.CASCADE)
    signature=models.CharField(max_length=200)
    bid=models.ForeignKey('Booking',on_delete=models.CASCADE)
    dateofbooking=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey('auth.User', related_name='+',on_delete=models.CASCADE)