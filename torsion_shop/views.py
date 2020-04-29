from django.shortcuts import render
from django.views.generic.base import View

from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, Category, CategoryMapping, Constant, Content, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, Profile, PromoSale, Region, RunString, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, WaitList, RatingStar, Rating, Review


def index(request):
    return render(request, 'torsion_shop/index.html')


def shop(request):
    return render(request, 'torsion_shop/shop.html')


class NewsView(View):
    def get(self, request):
        news = Content.objects.all()
        return render(request, 'torsion_shop/news.html', {'news_list': news})


class AboutUsView(View):
    def get(self, request):
        aboutus = Content.objects.all()
        return render(request, 'torsion_shop/about-us.html', {'aboutus_list': aboutus})


class ContactsView(View):
    def get(self, request):
        contacts = Content.objects.all()
        return render(request, 'torsion_shop/contacts.html', {'contacts_list': contacts})


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


