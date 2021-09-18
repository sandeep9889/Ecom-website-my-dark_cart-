
from django.urls import path
from.import views #here first import views of shop 

urlpatterns = [
    #from mdc file from url goes to here with the help of include function and then from this goes to view and function index
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productview/', views.prodview, name="productview"),
    path('checkout/', views.checkout, name="Checkout"),
    

]