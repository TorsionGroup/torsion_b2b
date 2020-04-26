from django.contrib import admin
from .models import Brand, Product, Action, ActionCustomer, ActionProduct, Balance, CacheApi, CatalogCategory, CatalogCategoryLang, Category, CategoryLang, CategoryMapping, Constant, Content, ContentLang, Cross, CrossErrorStatistic, Currency, Customer, CustomerAgreement, CustomerAgreementBak, CustomerCard, CustomerContact, CustomerDiscount, CustomerPoint, DeficitReserve, DeliveryCity, DeliveryMethod, DeliveryMethodLang, DeliveryPoint, DeliveryService, DropshippingWallet, DropshippingWalletTransfer, GalleryImage, Manager, ManagerLang, Offer, Order, OrderItem, OrderPayment, OrderSourceStatistic, PartnerApi, PartnerApiCache, PartnerCategory, PartnerCategoryCache, PartnerStock, Price, PriceBuffer, PriceCategory, PriceType, ProductApiMap, ProductApplicability, ProductDescription, ProductErrorStatistic, ProductLang, ProductPriceCategory, Profile, PromoSale, Region, RunString, RunStringLang, Sale, SaleHistory, SaleProductRelated, SaleTask, ScenarioPolicy, SearchRequest, SearchRequestBufferIgnore, SendPriceBuffer, SocialAccount, Stock, Token, UploadProduct, UploadSetting, UserRequest, UserRequestType, UserRequestTypeLang, WaitList, RatingStar, Rating, Review

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Content)
