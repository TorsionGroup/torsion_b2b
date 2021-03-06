from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('filter/', views.FilterProductView.as_view(), name='filter'),
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('about-us/', views.AboutUsView.as_view(), name='about-us'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('faq/', views.faq, name='faq'),
    path('compare/', views.compare, name='compare'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('add-rating-product/', views.AddStarRatingProduct.as_view(), name='add_rating_product'),
    path('add-rating-content/', views.AddStarRatingContent.as_view(), name='add_rating_content'),
    path('review-product/<int:pk>/', views.AddReviewProduct.as_view(), name='add_review_product'),
    path('review-content/<int:pk>/', views.AddReviewContent.as_view(), name='add_review_content'),
]
