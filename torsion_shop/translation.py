from modeltranslation.translator import  register, TranslationOptions
from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, Category, CategoryMapping, Constant, Content, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, Profile, PromoSale, Region, RunString, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, WaitList, RatingStar, Rating, Review


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'comment')


@register(Product)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'keywords')

