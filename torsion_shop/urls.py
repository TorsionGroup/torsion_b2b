from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about-us/', views.aboutus, name='about-us'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('login/', views.login, name='login'),
    path('single-product/', views.singleproduct, name='single-product'),
    path('news-detail/', views.newsdetail, name='news-detail'),
    path('account/', views.account, name='account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('faq/', views.faq, name='faq'),
    path('compare/', views.compare, name='compare'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]
