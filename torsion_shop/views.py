from django.shortcuts import render

def index(request):
    return render(request, 'torsion_shop/index.html')

def shop(request):
    return render(request, 'torsion_shop/shop.html')

def news(request):
    return render(request, 'torsion_shop/news.html')

def aboutus(request):
    return render(request, 'torsion_shop/about-us.html')

def contact(request):
    return render(request, 'torsion_shop/contact.html')

def login(request):
    return render(request, 'torsion_shop/login.html')

def singleproduct(request):
    return render(request, 'torsion_shop/single-product.html')

def newsdetail(request):
    return render(request, 'torsion_shop/news-detail.html')

def account(request):
    return render(request, 'torsion_shop/account.html')

def wishlist(request):
    return render(request, 'torsion_shop/wishlist.html')

def faq(request):
    return render(request, 'torsion_shop/faq.html')

def cart(request):
    return render(request, 'torsion_shop/cart.html')

def compare(request):
    return render(request, 'torsion_shop/compare.html')

def checkout(request):
    return render(request, 'torsion_shop/checkout.html')


