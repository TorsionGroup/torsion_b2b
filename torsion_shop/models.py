from django.db import models
from datetime import datetime
from creditcards.models import CardNumberField


class Brand(models.Model):
    name = models.CharField("Brand", max_length=300, null=True)
    enabled = models.BooleanField(default=1)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    wait_list = models.BooleanField(default=0)
    is_recommended = models.BooleanField(default=0)
    sort_index = models.IntegerField(default=999)
    source_type = models.CharField(max_length=250, default='1C')
    gallery_attribute = models.CharField(max_length=250, default='article')
    gallery_name = models.CharField(max_length=250, null=True)
    kind = models.CharField(max_length=250, default='secondary')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class PriceCategory(models.Model):
    inner_name = models.CharField(max_length=250, null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.inner_name

    class Meta:
        verbose_name = "PriceCategory"
        verbose_name_plural = "PriceCategories"


class CatalogCategory(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    enabled = models.BooleanField(default=1)
    sort_index = models.IntegerField(default=999, null=True)
    content_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.parent_id

    class Meta:
        verbose_name = "CatalogCategory"
        verbose_name_plural = "CatalogCategories"


class Offer(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    group = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Offer"
        verbose_name_plural = "Offers"


class Product(models.Model):
    specification = models.CharField(max_length=250, null=True)
    article = models.CharField(max_length=250, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.SET_NULL, related_name="product_brand", blank=True, null=True)
    offer_id = models.ForeignKey(
        Offer, on_delete=models.SET_NULL, related_name="product_offer", blank=True, null=True)
    category_id = models.ForeignKey(
        CatalogCategory, on_delete=models.SET_NULL, related_name="product_catalog", blank=True, null=True)
    create_date = models.DateTimeField(default=datetime.today, null=True)
    income_date = models.DateTimeField(default=datetime.today, null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    search_key = models.CharField(max_length=250, null=True)
    sort_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    is_active = models.BooleanField(default=1)
    weight = models.DecimalField(max_digits=15, decimal_places=3, null=True)
    pack_qty = models.IntegerField(null=True)
    ABC = models.CharField(max_length=1, null=True)
    is_exists = models.BooleanField(default=0)
    code = models.CharField(max_length=250, null=True)
    source_type = models.CharField(max_length=250, null=True)
    price_category = models.ManyToManyField(PriceCategory, related_name="product_pricecategory")
    product_type = models.IntegerField(null=True)
    delete_flag = models.BooleanField(default=0)
    advanced_description = models.TextField("Advanced description", null=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    keywords = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.specification

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Currency(models.Model):
    code = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    rate = models.DecimalField(max_digits=15, decimal_places=5, null=True)
    mult = models.IntegerField(null=True)
    name_eng = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Manager(models.Model):
    inner_name = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=250, null=True, blank=True)
    skype = models.CharField(max_length=250, default='skype', blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.inner_name

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"


class Customer(models.Model):
    code = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=300, null=True)
    main_customer_id = models.IntegerField(null=True, blank=True)
    manager_id = models.ForeignKey(
        Manager, on_delete=models.SET_NULL, related_name="customer_manager", null=True, blank=True)
    sale_policy = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    region_id = models.IntegerField(null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    no_show_balance = models.BooleanField(default=0)
    deficit_available = models.BooleanField(default=0)
    online_reserve = models.BooleanField(default=0)
    online_order = models.BooleanField(default=0)
    send_price = models.BooleanField(default=0)
    price_language = models.CharField(max_length=2, default='ru', null=True)
    price_email = models.TextField(null=True, blank=True)
    price_schedule = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class PriceType(models.Model):
    name = models.CharField(max_length=300, null=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    enabled = models.BooleanField(default=1)
    sort_index = models.IntegerField(default=999, null=True)
    access_policy_data = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "PriceType"
        verbose_name_plural = "PriceTypes"


class CustomerAgreement(models.Model):
    code = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    number = models.CharField(max_length=250, null=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="agreement_customer", null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="agreement_currency", null=True, blank=True)
    price_type_id = models.ForeignKey(
        PriceType, on_delete=models.CASCADE, related_name="agreement_pricetype", null=True, blank=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    is_status = models.BooleanField()
    source_id = models.CharField(max_length=300, null=True, blank=True)
    price_available = models.BooleanField(default=0)
    api_available = models.BooleanField(default=0)
    api_token = models.CharField(max_length=250, null=True, blank=True)
    api_user_id = models.IntegerField(null=True, blank=True)
    price_language = models.CharField(max_length=2, default='ru', null=True)
    is_active = models.BooleanField(default=1)
    price_schedule = models.CharField(max_length=500, null=True, blank=True)
    price_email = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "CustomerAgreement"
        verbose_name_plural = "CustomerAgreements"


class CustomerCard(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="card_customer", null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    card = CardNumberField(null=True, blank=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        verbose_name = "CustomerCard"
        verbose_name_plural = "CustomerCard"


class CustomerContact(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="contact_customer", null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True, blank=True)
    is_user = models.BooleanField(default=0)
    source_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        verbose_name = "CustomerContact"
        verbose_name_plural = "CustomerContacts"


class CustomerDiscount(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="discount_customer", null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="discount_agreement", null=True, blank=True)
    criteria_id = models.IntegerField(null=True, blank=True)
    criteria_type = models.CharField(max_length=250, null=True, blank=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    price_type_id = models.ForeignKey(
        PriceType, on_delete=models.CASCADE, related_name="discount_pricetype", null=True, blank=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        verbose_name = "CustomerDiscount"
        verbose_name_plural = "CustomerDiscounts"


class CustomerPoint(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="point_customer", null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.customer_id
    
    class Meta:
        verbose_name = "CustomerPoint"
        verbose_name_plural = "CustomerPoints"


class Balance(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="balance_customer", null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="balance_currency", null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    past_due = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="balance_agreement", null=True, blank=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        verbose_name = "Balance"
        verbose_name_plural = "Balances"


class Price(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="price_product", null=True, blank=True)
    price_type_id = models.ForeignKey(
        PriceType, on_delete=models.CASCADE, related_name="price_pricetype", null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="price_currency", null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"


class PriceBuffer(models.Model):
    code = models.CharField(max_length=250, null=True, blank=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="pricebuffer_brand", null=True, blank=True)
    category = models.CharField(max_length=250, null=True, blank=True)
    price_category = models.ForeignKey(
        PriceCategory, on_delete=models.CASCADE, related_name="pricebuffer_pricecategory", null=True, blank=True)
    specification = models.CharField(max_length=250, null=True, blank=True)
    article = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=250, null=True, blank=True)
    rest = models.IntegerField(null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="discount_agreement", null=True, blank=True)
    sort_index = models.CharField(max_length=300, null=True, blank=True)
    pack_qty = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "PriceBuffer"
        verbose_name_plural = "PriceBuffers"


class Stock(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="stock_product", null=True, blank=True)
    stock_name = models.CharField(max_length=300, null=True, blank=True)
    amount_total = models.IntegerField(default=0, null=True)
    amount_account = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"


class Category(models.Model):
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=500, null=True, blank=True)
    url = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Constant(models.Model):
    code = models.CharField(max_length=250, null=True, blank=True)
    value = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Constant"
        verbose_name_plural = "Constant"


class Content(models.Model):
    alias = models.SlugField(max_length=300, unique=True)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField(default=datetime.today)
    published = models.BooleanField(default=0)
    main_image = models.ImageField(upload_to="content/main_image/", blank=True)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name="content_category", null=True, blank=True)
    title = models.CharField(max_length=300)
    intro_text = models.CharField(max_length=500)
    full_text = models.TextField()
    meta_tag_title = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_description = models.CharField(max_length=500, null=True, blank=True)
    meta_tag_keyword = models.CharField(max_length=500, null=True, blank=True)
    geo = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"


class ContentImage(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="content/content_image/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ContentImage"
        verbose_name_plural = "ContentImages"


class Cross(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cross_product", null=True, blank=True)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cross_brand", null=True, blank=True)
    article_nr = models.CharField(max_length=500, null=True, blank=True)
    search_nr = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Cross"
        verbose_name_plural = "Crosses"


class CrossErrorStatistic(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="crosserror_product", null=True, blank=True)
    search_number = models.CharField(max_length=1000)
    comment = models.CharField(max_length=500, null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="crosserror_customer", null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "CrossErrorStatistic"
        verbose_name_plural = "CrossErrorStatistics"


class ProductApplicability(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="applicabilty_product", null=True, blank=True)
    vehicle = models.CharField(max_length=250, null=True, blank=True)
    modification = models.CharField(max_length=250, null=True, blank=True)
    engine = models.CharField(max_length=250, null=True, blank=True)
    year = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "ProductApplicability"
        verbose_name_plural = "ProductApplicabilities"


class ProductDescription(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="description_product", null=True, blank=True)
    property = models.CharField(max_length=500, null=True, blank=True)
    value = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "ProductDescription"
        verbose_name_plural = "ProductDescriptions"


class ProductErrorStatistic(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cross_product", null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    error_comment = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField(default=datetime.today)
    admin_comment = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "ProductErrorStatistic"
        verbose_name_plural = "ProductErrorStatistics"


class DeficitReserve(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="deficit_product", null=True, blank=True)
    sale_policy = models.CharField(max_length=250, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "DeficitReserve"
        verbose_name_plural = "DeficitReserves"


class Region(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class DeliveryMethod(models.Model):
    code = models.CharField(max_length=250, null=True, blank=True)
    region_available = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    red = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "DeliveryMethod"
        verbose_name_plural = "DeliveryMethods"


class DeliveryService(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    has_to_door = models.BooleanField(default=0)
    parameters = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "DeliveryService"
        verbose_name_plural = "DeliveryService"


class DeliveryCity(models.Model):
    service_id = models.ForeignKey(
        DeliveryService, on_delete=models.CASCADE, related_name="city_service", null=True, blank=True)
    region = models.CharField(max_length=250, null=True, blank=True)
    ref = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.today)
    update_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.service_id

    class Meta:
        verbose_name = "DeliveryCity"
        verbose_name_plural = "DeliveryCities"


class DeliveryPoint(models.Model):
    service_id = models.ForeignKey(
        DeliveryService, on_delete=models.CASCADE, related_name="point_service", null=True, blank=True)
    city_id = models.ForeignKey(
        DeliveryCity, on_delete=models.CASCADE, related_name="point_city", null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    ref = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    longitude = models.CharField(max_length=250, null=True, blank=True)
    latitude = models.CharField(max_length=250, null=True, blank=True)
    max_weight = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.service_id

    class Meta:
        verbose_name = "DeliveryPoint"
        verbose_name_plural = "DeliveryPoints"


class PartnerApi(models.Model):
    code = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    token = models.CharField(max_length=250, null=True, blank=True)
    margin = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    percent_prepayment = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    show_branch = models.BooleanField(default=1)
    enabled = models.BooleanField(default=0)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "PartnerApi"
        verbose_name_plural = "PartnerApies"


class CacheApi(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="cache_parnter", null=True, blank=True)
    search_number = models.CharField(max_length=250)
    response_api = models.TextField(null=True, blank=True)
    response_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "CacheApi"
        verbose_name_plural = "CacheApis"


class PartnerApiCache(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="apicache_parnter", null=True, blank=True)
    search_number = models.CharField(max_length=250, null=True, blank=True)
    response_date = models.DateTimeField(default=datetime.today)
    product_json = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "PartnerApiCache"
        verbose_name_plural = "PartnerApiCaches"


class PartnerCategory(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="category_parnter", null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, default=0, null=True)
    response_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "PartnerCategory"
        verbose_name_plural = "PartnerCategories"


class CategoryMapping(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="mapping_parnter", null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    category_id = models.ForeignKey(
        PartnerCategory, on_delete=models.CASCADE, related_name="mapping_category", null=True, blank=True)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "CategoryMapping"
        verbose_name_plural = "CategoryMappings"


class PartnerCategoryCache(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="categorycache_parther", null=True, blank=True)
    category_id = models.ForeignKey(
        PartnerCategory, on_delete=models.CASCADE, related_name="categorycache_category", null=True, blank=True)
    response_date = models.DateTimeField(default=datetime.today)
    product_json = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "PartnerCategoryCache"
        verbose_name_plural = "PartnerCategoryCaches"


class PartnerStock(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_parther", null=True, blank=True)
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="stock_parther", null=True, blank=True)
    branch = models.CharField(max_length=250, null=True, blank=True)
    qty = models.IntegerField(default=0, null=True)
    supply_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "PartnerStock"
        verbose_name_plural = "PartnerStocks"


class ProductApiMap(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_apimap", null=True, blank=True)
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="parther_apimap", null=True, blank=True)
    api_key = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "ProductApiMap"
        verbose_name_plural = "ProductApiMaps"


class Order(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="order_agreement", null=True, blank=True)
    status = models.SmallIntegerField(default=0)
    delivery_method = models.ForeignKey(
        DeliveryMethod, on_delete=models.CASCADE, related_name="order_delivery", null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.today)
    update_date = models.DateTimeField(default=datetime.today)
    comment = models.TextField(null=True, blank=True)
    point_id = models.ForeignKey(
        CustomerPoint, on_delete=models.CASCADE, related_name="order_customerpoint", null=True, blank=True)
    delivery_service_id = models.ForeignKey(
        DeliveryService, on_delete=models.CASCADE, related_name="order_delpoint", null=True, blank=True)
    delivery_city_id = models.ForeignKey(
        DeliveryCity, on_delete=models.CASCADE, related_name="order_delcity", null=True, blank=True)
    delivery_point_id = models.ForeignKey(
        DeliveryPoint, on_delete=models.CASCADE, related_name="order_delpoint", null=True, blank=True)
    delivery_contact = models.CharField(max_length=250, null=True)
    delivery_contact_phone = models.CharField(max_length=250, null=True)
    order_number = models.CharField(max_length=250, null=True, blank=True)
    waybill_number = models.CharField(max_length=250, null=True, blank=True)
    invoice_number = models.CharField(max_length=250, null=True, blank=True)
    source = models.CharField(max_length=250, default='site', null=True)
    is_pay_on_delivery = models.BooleanField(default=0)
    pay_on_delivery_sum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    import_reason = models.TextField(null=True, blank=True)
    import_status = models.CharField(max_length=250, null=True, blank=True)
    partner_code = models.CharField(max_length=250, null=True, blank=True)
    declared_sum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    declared_currency = models.BooleanField(default=1)
    source_type = models.CharField(max_length=250, default='B2B', null=True)
    delivery_contact_surname = models.CharField(max_length=250, null=True)
    declaration_number = models.CharField(max_length=250, null=True, blank=True)
    delivery_contact_middlename = models.CharField(max_length=250, null=True)
    delivery_is_invoice_off = models.BooleanField(default=1)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItem(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_item", null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="order_product", null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="order_currency", null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    source = models.CharField(max_length=250, null=True, blank=True)
    reserved = models.IntegerField(null=True, blank=True)
    executed = models.IntegerField(null=True, blank=True)
    old_qty = models.IntegerField(null=True, blank=True)
    old_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    purchase_qty = models.IntegerField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    purchase_currency_id = models.IntegerField(null=True, blank=True)
    purchase_order_id = models.IntegerField(null=True, blank=True)
    purchase_item_id = models.IntegerField(null=True, blank=True)
    partner_branch = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "OrderItem"
        verbose_name_plural = "OrderItems"


class OrderPayment(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_payment", null=True, blank=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2)
    date_payment = models.DateTimeField(default=datetime.today)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="order_currency", null=True, blank=True)
    payment_sum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    receiver_commission = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    sender_commission = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "OrderPayment"
        verbose_name_plural = "OrderPayments"


class OrderSourceStatistic(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orderstatistik_product", null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orderstatistik_customer", null=True, blank=True)
    source_type = models.CharField(max_length=250, null=True, blank=True)
    add_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "OrderSourceStatistic"
        verbose_name_plural = "OrderSourceStatistics"


class DropshippingWallet(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="dwallet_order", null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="dwallet_agreement", null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="dwallet_currency", null=True, blank=True)
    debit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "DropshippingWallet"
        verbose_name_plural = "DropshippingWallets"


class DropshippingWalletTransfer(models.Model):
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="dtransfer_order", null=True, blank=True)
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="dtransfer_agreement", null=True, blank=True)
    sum = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    currency_id = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name="dtransfer_currency", null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)
    card = CardNumberField(null=True, blank=True)

    def __str__(self):
        return self.order_id

    class Meta:
        verbose_name = "DropshippingWalletTransfer"
        verbose_name_plural = "DropshippingWalletTransfers"


class Profile(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    public_email = models.EmailField(null=True, blank=True)
    gravatar_email = models.EmailField(null=True, blank=True)
    gravatar_id = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class PromoSale(models.Model):
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="promosale_customer", null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="promosale_product", null=True, blank=True)
    type = models.CharField(max_length=300, null=True, blank=True)
    is_visible = models.BooleanField(default=0)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.customer_id

    class Meta:
        verbose_name = "PromoSale"
        verbose_name_plural = "PromoSales"


class RunString(models.Model):
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField(default=datetime.today)
    full_text = models.CharField(max_length=1000, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    published = models.BooleanField(default=0)

    def __str__(self):
        return self.created_date

    class Meta:
        verbose_name = "RunString"
        verbose_name_plural = "RunStrings"


class Sale(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sale_product", null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="sale_customer", null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"


class SaleHistory(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="saleh_product", null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="saleh_customer", null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "SaleHistory"
        verbose_name_plural = "SaleHistories"


class SaleProductRelated(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="srelated_product", null=True, blank=True)
    related_product_id = models.IntegerField(null=True, blank=True)
    qty_index = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    calculation_type = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "SaleProductRelated"
        verbose_name_plural = "SaleProductRelateds"


class SaleTask(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="stask_product", null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="stask_customer", null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "SaleTask"
        verbose_name_plural = "SaleTasks"


class ScenarioPolicy(models.Model):
    sale_policy = models.CharField(max_length=250, null=True, blank=True)
    deficit_available = models.BooleanField(default=0, null=True)
    online_reserve = models.BooleanField(default=0, null=True)
    online_order = models.BooleanField(default=0, null=True)

    def __str__(self):
        return self.sale_policy

    class Meta:
        verbose_name = "ScenarioPolicy"
        verbose_name_plural = "ScenarioPolicies"


class SearchRequest(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    search_keyword = models.CharField(max_length=250, null=True, blank=True)
    search_keyword_clean = models.CharField(max_length=250, null=True, blank=True)
    is_result = models.BooleanField(default=0, null=True)
    product_list = models.TextField(null=True, blank=True)
    is_added_in_cart = models.BooleanField(default=0, null=True)
    product_add_in_cart = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "ScenarioPolicy"
        verbose_name_plural = "ScenarioPolicies"


class SearchRequestBufferIgnore(models.Model):
    search_keyword_clean = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.search_keyword_clean

    class Meta:
        verbose_name = "SearchRequestBufferIgnore"
        verbose_name_plural = "SearchRequestBufferIgnores"


class SendPriceBuffer(models.Model):
    agreement_id = models.ForeignKey(
        CustomerAgreement, on_delete=models.CASCADE, related_name="sendprice_agreement", null=True, blank=True)
    price_email = models.CharField(max_length=250, null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="sendprice_customer", null=True, blank=True)

    def __str__(self):
        return self.agreement_id

    class Meta:
        verbose_name = "SendPriceBuffer"
        verbose_name_plural = "SendPriceBuffers"


class Token(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=300, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.today)
    type = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "Token"
        verbose_name_plural = "Tokens"


class UploadProduct(models.Model):
    upload_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(default=datetime.today)
    name = models.CharField(max_length=300, null=True, blank=True)
    article = models.CharField(max_length=300, null=True, blank=True)
    search_key = models.CharField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=300, null=True, blank=True)
    brand = models.CharField(max_length=300, null=True, blank=True)
    comment = models.CharField(max_length=1000, null=True, blank=True)
    branch = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    supply = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.upload_id

    class Meta:
        verbose_name = "UploadProduct"
        verbose_name_plural = "UploadProducts"


class UploadSetting(models.Model):
    partner_code = models.ForeignKey(
        PartnerApi, on_delete=models.CASCADE, related_name="uploadsetting_parther", null=True, blank=True)
    file_name = models.CharField(max_length=250, null=True, blank=True)
    first_row = models.IntegerField(null=True, blank=True)
    mapping = models.TextField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    rate = models.DecimalField(max_digits=15, decimal_places=5, null=True, blank=True)
    encoding = models.CharField(max_length=250, null=True, blank=True)
    compare_name = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "UploadSetting"
        verbose_name_plural = "UploadSettings"


class UserRequest(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    request_type_id = models.IntegerField(null=True, blank=True)
    source_id = models.CharField(max_length=300, null=True, blank=True)
    checked = models.BooleanField(default=0)
    date_request = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = "UserRequest"
        verbose_name_plural = "UserRequests"


class UserRequestType(models.Model):
    manager_id = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name="userrequest_manager", null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.manager_id

    class Meta:
        verbose_name = "UserRequestType"
        verbose_name_plural = "UserRequestTypes"


class WaitList(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="waitlist_product", null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    date_add = models.DateTimeField(default=datetime.today)
    send_message = models.BooleanField(default=0)
    is_active = models.BooleanField(default=0)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "WaitList"
        verbose_name_plural = "WaitLists"


class Action(models.Model):
    content_id = models.ForeignKey(
        Content, on_delete=models.CASCADE, related_name="action_customer", null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    start_at = models.DateTimeField(default=datetime.today)
    finish_at = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.content_id

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"


class ActionCustomer(models.Model):
    action_id = models.ForeignKey(
        Action, on_delete=models.CASCADE, related_name="action_customer", null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="discount_customer", null=True, blank=True)
    win = models.BooleanField(default=0)
    close_action = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.action_id

    class Meta:
        verbose_name = "ActionCustomer"
        verbose_name_plural = "ActionCustomers"


class ActionProduct(models.Model):
    action_id = models.ForeignKey(
        Action, on_delete=models.CASCADE, related_name="product_action", null=True, blank=True)
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="action_product", null=True, blank=True)

    def __str__(self):
        return self.action_id

    class Meta:
        verbose_name = "ActionProduct"
        verbose_name_plural = "ActionProducts"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "RatingStar"
        verbose_name_plural = "RatingStars"


class RatingProduct(models.Model):
    ip = models.CharField(max_length=50)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "RatingProduct"
        verbose_name_plural = "RatingProducts"


class ReviewProduct(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "ReviewProduct"
        verbose_name_plural = "ReviewProducts"


class RatingContent(models.Model):
    ip = models.CharField(max_length=50)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.content}"

    class Meta:
        verbose_name = "RatingContent"
        verbose_name_plural = "RatingContents"


class ReviewContent(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.content}"

    class Meta:
        verbose_name = "ReviewContent"
        verbose_name_plural = "ReviewContents"
