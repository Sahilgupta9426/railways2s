
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render,redirect
from django.template.loader import render_to_string
from railway.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY 
import razorpay
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


import app
from .forms import TravelForm,CustomerForm
from .models import Train,Travel_Schedule
from django.contrib import messages
import csv
# Create your views here.
def home(request):
    form=TravelForm()
    data=dict()
    if request.method == "POST" and request.is_ajax():
        form = TravelForm(request.POST)
        if form.is_valid():
            date=request.POST['date']
            
            # print(request.POST['source'],request.POST['destination'])
            t = Travel_Schedule.objects.filter(source=request.POST['source'], destination=request.POST['destination'])
            home.t2=t
            # this loop is used for get seat from Train Table which is fecthed with foreign key
            home.date2=date
            # from here is test
            listseat=list()
            for train_num in t: # sending Travel_schedule object in train_num
                p=train_num.train_no #saving train number from Travel Schedule in p variable
                a=Train.objects.select_related('sid').filter(sid=p)#searching 'sid' whic is Train Number in Train Model 
                # print("all object details",a)
                for obj in a: #sending all 'a' object in obj 
                    seat=obj.seat1 #to get total seats
                    # print("all object details",seat)
                    listseat.append(seat)
            result="hello"      
            # print(listseat)
            mylist = zip(t, listseat)
            home.mylist2=mylist
            context = {
            'trains': mylist,
            'date':date
                }
            # end test
            data['html_train_list'] = render_to_string('include/train_results.html', context)
            data['form_is_valid'] = True
            
        else:
            data['form_is_valid'] = False
        
        context = {'form': form}

        return JsonResponse(data)
    all=Travel_Schedule.objects.all()
    s=[]
    for all1 in all:
        s.append(all1.source)
    d=[]
    for all1 in all:
        d.append(all1.destination)
    
    s = list(set(s))
    d = list(set(d))    
    return render(request,'home.html',{'form':form,'source':s,'destination':d})



def exportcsv(request):
    datas=home.t2
    response=HttpResponse(content_type='text/csv')
    response['Content-Dispostion']='attachment; filename=list_searched_train.csv'
    writer=csv.writer(response)
    writer.writerow(['Train Number','Train Name','Source','Destination','Arrival Time','Fare'])
    data=datas.values_list('train_no','train_name','source','destination','arrival_time','fare')
    for d in data:
        writer.writerow(d)
    return response


# booking customer details
def customer(request,pk):
    date=home.date2
    t=Travel_Schedule.objects.filter(train_no=pk)
    customer.t1=t
    
    seat=Train.objects.select_related('sid').filter(sid=pk)
    # 1.get seat number for seat number  
    ls=[]
    for s in seat:
        s=s.seat1
        ls.append(s)   
    s=ls[0]
    s=int(s)
    print('my test',s)
    customer.seat2=s-1
    # 1. end
    for seats in seat:
        seat=seats.seat1
    form=CustomerForm()
    data=dict()
    data["html_form"]=render_to_string('include/booking_detail.html', {
                "form":form,'trains':t,'seat':seat,'date':date
            },request=request)
    return JsonResponse(data)

def payment(request):
    
    if request.method=="POST":
        # form=CustomerForm(request.POST)
        name=request.POST['cname']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        number=request.POST['number']
        travel=customer.t1
        seat_no=customer.seat2
        # det={'name':name,'age':age,'number':number,'gender':gender,'trains':travel,'seat':seat_no}
        #2 payment details
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        order_amount=100000
        
        response = client.order.create(dict(amount=order_amount, currency=order_currency, receipt=order_receipt, payment_capture='0'))
        order_id = response['id']
        order_status = response['status']
        response['name']=name
        response['email']=email
        response['age']=age
        response['gender']=gender
        response['number']=number
        response['trains']=travel
        response['seat']=seat_no
        response['order_id']=order_id
        return render(request,'include/payment.html',response)
def status(request):
    pass
