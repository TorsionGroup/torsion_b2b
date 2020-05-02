from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, Category, CategoryMapping, Constant, Content, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, Profile, PromoSale, Region, RunString, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, WaitList, RatingStar, Rating, Review


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'comment', 'url')
    list_display_links = ('name',)


class ContentAdminForm(forms.ModelForm):
    full_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = '__all__'


@admin.register(Content)
class ContentAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'alias', 'published')
    list_filter = ('category_id',)
    list_display_links = ('title',)
    save_on_top = True
    #form = ContentAdminForm


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sort_index', 'enabled', 'wait_list', 'is_recommended', 'kind', 'enabled')
    list_filter = ('sort_index',)
    list_display_links = ('name',)
    search_fields = ('name',)


class ReviewInLine(admin.StackedInline):
    model = Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'article', 'specification', 'sort_price', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name', 'article',)
    save_on_top = True


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'email', 'product')
    list_display_links = ('name',)
    search_fields = ('name', 'product',)


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'inner_name', 'source_id')
    list_display_links = ('inner_name',)


