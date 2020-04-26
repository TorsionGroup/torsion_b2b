from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about-us/', views.aboutus, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
]
