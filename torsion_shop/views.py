from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
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
from .forms import RegistrationForm, ReviewContentForm, RatingContentForm, ReviewProductForm, RatingProductForm


def index(request):
    return render(request, 'torsion_shop/index.html')


class ShopView(View):
    def get(self, request):
        shop = Product.objects.all()
        catalogcategory = CatalogCategory.objects.all()
        context = {'shop_list': shop, 'catalogcategory_list': catalogcategory}
        return render(request, 'torsion_shop/shop.html', context)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["star_form"] = RatingContentForm()
        context["form"] = ReviewContentForm()
        return context


class AddReviewContent(View):
    def post(self, request, pk):
        form = ReviewContentForm(request.POST)
        content = Content.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.content = content
            form.save()
        return redirect(content.get_absolute_url())


class AddStarRatingContent(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingContentForm(request.POST)
        if form.is_valid():
            RatingProduct.objects.update_or_create(
                ip=self.get_client_ip(request),
                shop_id=int(request.POST.get('singleproduct')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class AddReviewProduct(View):
    def post(self, request, pk):
        form = ReviewProductForm(request.POST)
        singleproduct = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.singleproduct = singleproduct
            form.save()
        return redirect(singleproduct.get_absolute_url())


class AddStarRatingProduct(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingContentForm(request.POST)
        if form.is_valid():
            RatingProduct.objects.update_or_create(
                ip=self.get_client_ip(request),
                news_id=int(request.POST.get("news")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


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
    def cart(self, request):
        return render(request, 'torsion_shop/cart.html')


def compare(request):
    return render(request, 'torsion_shop/compare.html')


class CheckoutView(View):
    def checkout(self, request):
        return render(request, 'torsion_shop/checkout.html')


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


class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class FilterProductView(ListView):
    paginate_by = 5

    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["year"] = ''.join([f"year={x}&" for x in self.request.GET.getlist("year")])
        context["genre"] = ''.join([f"genre={x}&" for x in self.request.GET.getlist("genre")])
        return context


class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context