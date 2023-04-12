from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('chocolate', views.chocolate, name='chocolate'),
    path('icecream', views.icecream, name='icecream'),
    path('bakery', views.bakery, name='bakery'),
    path('contact', views.contact, name='contact'),
]