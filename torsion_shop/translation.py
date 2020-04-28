from modeltranslation.translator import  register, TranslationOptions
from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, Category, CategoryMapping, Constant, Content, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, Profile, PromoSale, Region, RunString, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, WaitList, RatingStar, Rating, Review


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'keywords')


@register(CatalogCategory)
class CatalogCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(DeliveryMethod)
class DeliveryMethodTranslationOptions(TranslationOptions):
    fields = ('method_code', 'comment', 'name', 'red')


@register(Manager)
class ManagerMethodTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(RunString)
class RunStringMethodTranslationOptions(TranslationOptions):
    fields = ('full_text', 'comment')


@register(UserRequestType)
class UserRequestTypeMethodTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')
