from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
     path('', views.index, name="index"),       
     path('signin_view', views.signin_request, name="signin_view"),
     path('signup_view', views.signup_request, name="signup_view"),
     path('signout_view', views.signout_request, name="signout_view"),  
     path('newpost', views.newpost, name="newpost"),   
     path('profit', views.profit, name="profit"),
     path('contact', views.contact, name="contact"),          
 ]