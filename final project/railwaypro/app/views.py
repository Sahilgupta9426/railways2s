from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render,redirect
from django.template.loader import render_to_string
from numpy import number
from railwaypro.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY 
import razorpay
from .forms import TravelForm,CustomerForm
from .models import Train ,Travel_Schedule,Transaction,Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv
# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

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



@login_required
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
@login_required
def customer(request,pk):
    date=home.date2
    t=Travel_Schedule.objects.filter(train_no=pk)
    for fare in t:
        fare=fare.fare
    customer.fare=fare
    customer.t1=t
    customer.pk_train_no=int(pk)
    
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

@login_required
def payment(request):
    if request.method=="POST":
        # form=CustomerForm(request.POST)
        date=home.date2
        name=request.POST['cname']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']
        number=request.POST['number']
        order_amount=100*int(customer.fare)
        travel=customer.t1
        pk=customer.pk_train_no
        seat_no=customer.seat2

        payment.det={'name':name,'age':age,'number':number,'email':email,'gender':gender,'trains':pk,'seat_no':seat_no,'amount':order_amount,'date':date}
        #2 payment details
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        
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
        response['date']=date
        # return render(request,'include/payment.html',response)
        return render(request,'payment/test.html',response)


#  status after payment and save customer details and transaction  
@login_required
def status(request):
    response = request.POST
    usr=request.user
    print('user',usr)
    # print(response)
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    # VERIFYING SIGNATURE
    customer=payment.det
    status1=client.utility.verify_payment_signature(params_dict)
    # update seat query
    train_no=Travel_Schedule.objects.get(train_no=customer['trains'])
    train_seat=Train.objects.filter(sid=customer['trains'])
    for trainseat2 in train_seat:
        train_seat1=trainseat2.seat1
        tid=trainseat2.id
    print('seat',train_seat1)
    toupdateseat=Train.objects.get(id=tid)
    # end update seat query
    
    if status1==True:
        train_seat1=train_seat1-1
        toupdateseat.seat1=train_seat1
        toupdateseat.save()
        
        savecustomer=Booking(name=customer['name'],age=customer['age'],gender=customer['gender'],number=customer['number'],email=customer['email'],seat_no=train_seat1,amount=customer['amount'],journey_date=customer['date'],s_id=train_no,p_status=True,user=usr)

        savecustomer.save()
        id=savecustomer.id
        get_id=Booking.objects.get(id=id)

        savetransaction=Transaction(payment_id=response['razorpay_payment_id'],order_id= response['razorpay_order_id'],signature=response['razorpay_signature'],bid=get_id,user=usr)
        savetransaction.save()

    elif status==False:
        savecustomer=Booking(name=customer['name'],age=customer['age'],gender=customer['gender'],number=customer['number'],email=customer['email'],s_id=train_no,p_status=False,user=usr)
        savecustomer.save()
    try:
        
        status = client.utility.verify_payment_signature(params_dict)
        

        

        return render(request, 'payment/order_summery.html', {'status': 'Payment Successful'})
    except:
        
        return render(request, 'payment/order_summery.html', {'status': 'Payment Faliure!!!'})

@login_required
def cutomer_booking_list(request):
    data={}
    booking=Booking.objects.all()
    
    data["html_form"]=render_to_string('include/booking_list.html', {
        'book':booking
            })
    return JsonResponse(data)

@login_required
def cancel_booking(request, pk):
    
    book1=Booking.objects.filter(id=pk)
    for b in book1:
        s_id=b.s_id
    train=Train.objects.filter(sid=s_id)
    for t in train:
        seat=t.seat1
        tid=t.id
    data={}
    data["html_form"]=render_to_string('include/confirm.html', {
        'book':book1
            },request=request)
    if request.method=="POST":
        
        book1=Booking.objects.get(id=pk)
        book1.delete()
        train=Train.objects.get(id=tid)
        train.seat1=seat+1
        train.save()
        return redirect("/home/")
    return JsonResponse(data)