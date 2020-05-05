from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
import json
import datetime
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from .utils import cookieCart, cartData, guestOrder
from .models import *
from .forms import RegistrationForm


def index(request):
    return render(request, 'torsion_shop/index.html')


class ShopView(View):
    def get(self, request):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        shop = Product.objects.all()
        catalogcategory = CatalogCategory.objects.all()
        return render(request, 'torsion_shop/shop.html', {'shop_list': shop, 'catalogcategory_list': catalogcategory, 'cartItems':cartItems})


class SingleProductView(View):
    def get(self, request, pk):
        singleproduct = Product.objects.get(id=pk)
        return render(request, 'torsion_shop/single-product.html', {'shop_detail': singleproduct})


class NewsView(View):
    def get(self, request):
        news = Content.objects.filter(category_id=2)
        return render(request, 'torsion_shop/news.html', {'news_list': news})


class NewsDetailView(View):
    def get(self, request, slug):
        newsdetail = Content.objects.get(alias=slug)
        return render(request, 'torsion_shop/news-detail.html', {'news_detail': newsdetail})


class AboutUsView(View):
    def get(self, request):
        aboutus = Content.objects.filter(category_id=4)
        return render(request, 'torsion_shop/about-us.html', {'aboutus_list': aboutus})


class ContactsView(View):
    def get(self, request):
        contacts = Content.objects.filter(category_id=5)
        return render(request, 'torsion_shop/contacts.html', {'contacts_list': contacts})


def login(request):
    return render(request, 'torsion_shop/account/login.html')


def account(request):
    return render(request, 'torsion_shop/account/account.html')


def wishlist(request):
    return render(request, 'torsion_shop/wishlist.html')


def faq(request):
    return render(request, 'torsion_shop/faq.html')


class CartView(View):
    def cart(request):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'torsion_shop/cart.html', context)


def compare(request):
    return render(request, 'torsion_shop/compare.html')


class CheckoutView(View):
    def checkout(request):
        data = cartData(request)
        cartItems = data['cartItems']
        order = data['order']
        items = data['items']
        context = {'items': items, 'order': order, 'cartItems': cartItems}
        return render(request, 'torsion_shop/checkout.html', context)

    def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()

        return JsonResponse('Item was added', safe=False)

    def processOrder(request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
        else:
            customer, order = guestOrder(request, data)

        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

        return JsonResponse('Payment submitted..', safe=False)


class RegistrationView(CreateView):
    template_name = 'torsion_shop/account/login.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    model = Account
    fields = ['username', 'phone', 'date_of_birth', 'picture']
    template_name = 'torsion_shop/account/account.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user

