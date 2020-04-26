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
