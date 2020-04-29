from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
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
