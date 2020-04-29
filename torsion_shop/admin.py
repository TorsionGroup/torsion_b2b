from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, Category, CategoryMapping, Constant, Content, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, Profile, PromoSale, Region, RunString, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, WaitList, RatingStar, Rating, Review

admin.site.register(Brand)
admin.site.register(Product)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'comment', 'url')
    list_display_links = ('name',)


@admin.register(Content)
class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'alias', 'published')
    list_display_links = ('title',)
