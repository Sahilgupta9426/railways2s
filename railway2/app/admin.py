from django.contrib import admin
from .models import Train,Travel_Schedule,Booking,Transaction
# Register your models here.
@admin.register(Travel_Schedule)
class AdminTravelSchedule(admin.ModelAdmin):
    list_display=['train_no','train_name','source','destination','arrival_time','fare']


@admin.register(Train)
class AdminTrain(admin.ModelAdmin):
    list_display=['id','seat1','seat2','seat3','seat4','seat5','seat6','seat7','seat8','seat9','seat10','sid']
@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    list_display=['id','s_id','name','age','gender','email','number','seat_no','p_status']
@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display=['id','payment_id','order_id','signature','bid']