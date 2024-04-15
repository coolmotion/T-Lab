from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('whoweare', views.whoweare, name="whoweare"),
    path('ourservices', views.ourservices, name="ourservices"),
    path('academy', views.academy, name="academy"),
    path('ourproduction', views.ourproduction, name="ourproduction"),

]
