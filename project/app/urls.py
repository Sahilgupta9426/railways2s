from django.urls import path,include,re_path
from . import views

urlpatterns = [
    
    re_path(r'^home/$', views.home,name="home"),
    re_path(r'^home/(?P<pk>\d+)/customer/$', views.customer,name="customer"),
    re_path(r'^home/booking/$', views.cutomer_booking_list,name="customer_list"),
    re_path(r'^exportcsv/$', views.exportcsv,name="export_csv"),
    re_path(r'^payment/$', views.payment,name="payment"),
    re_path(r'^status/$', views.status,name="status"),
    re_path(r'^home/(?P<pk>\d+)/cancel/$', views.cancel_booking,name="cancel"),
    # # re_path(r'^books/(?P<pk>\d+)/update/$', views.book_update, name='book_update'),
    
]