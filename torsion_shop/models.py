from django.db import models
from datetime import datetime


class Brand(models.Model):
    name = models.CharField("Brand", max_length=300)
    enabled = models.IntegerField()
    source_id = models.CharField(max_length=250)
    wait_list = models.IntegerField()
    is_recommended = models.IntegerField()
    sort_index = models.IntegerField()
    source_type = models.CharField(max_length=250)
    gallery_attribute = models.CharField(max_length=250)
    gallery_name = models.CharField(max_length=250)
    kind = models.CharField(max_length=250)
    description = models.TextField("Description")
    url = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class PriceCategory(models.Model):
    inner_name = models.CharField(max_length=250)
    source_id = models.CharField(max_length=250)

    def __str__(self):
        return self.inner_name

    class Meta:
        verbose_name = "PriceCategory"
        verbose_name_plural = "PriceCategories"


class Product(models.Model):
    article = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    comment = models.TextField()
    specification = models.CharField(max_length=250)
    brand_id = models.ManyToManyField(Brand, related_name="product_brand")
    offer_id = models.IntegerField()
    category_id = models.IntegerField()
    create_date = models.DateTimeField(default=datetime.today)
    income_date = models.DateTimeField()
    source_id = models.CharField(max_length=250)
    search_key = models.CharField(max_length=250)
    sort_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.IntegerField()
    weight = models.DecimalField(max_digits=15, decimal_places=3)
    pack_qty = models.IntegerField()
    ABC = models.CharField(max_length=1)
    is_exists = models.IntegerField()
    code = models.CharField(max_length=250)
    source_type = models.CharField(max_length=250)
    price_category = models.ManyToManyField(PriceCategory, related_name="product_pricecategory")
    product_type = models.IntegerField()
    delete_flag = models.BooleanField(default=0)
    advanced_description = models.TextField("Advanced description")
    keywords = models.CharField(max_length=500)
    url = models.SlugField(max_length=250, unique=True)
    product_id = models.IntegerField()

    def __str__(self):
        return self.article

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Action(models.Model):
    content_id = models.IntegerField()
    comment = models.TextField()
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()

    def __str__(self):
        return self.content_id


class ActionCustomer(models.Model):
    action_id = models.IntegerField()
    customer_id = models.IntegerField()
    win = models.BooleanField(default=0)
    close_action = models.CharField(max_length=1000)

    def __str__(self):
        return self.action_id


class ActionProduct(models.Model):
    action_id = models.IntegerField()
    product_id = models.IntegerField()

    def __str__(self):
        return self.action_id


class Currency(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    source_id = models.CharField(max_length=250)
    rate = models.DecimalField(max_digits=15, decimal_places=5)
    mult = models.IntegerField()
    name_eng = models.CharField(max_length=250)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Customer(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    main_customer_id = models.IntegerField()
    manager_id = models.IntegerField()
    sale_policy = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    region_id = models.IntegerField()
    source_id = models.CharField(max_length=250)
    no_show_balance = models.IntegerField()
    deficit_available = models.IntegerField()
    online_reserve = models.IntegerField()
    online_order = models.IntegerField()
    send_price = models.BooleanField(default=0)
    price_language = models.CharField(max_length=3)
    price_email = models.TextField()
    price_schedule = models.CharField(max_length=500)

    def __str__(self):
        return self.code


class CustomerAgreement(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    customer_id = models.IntegerField()
    currency_id = models.IntegerField()
    price_type_id = models.IntegerField()
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    is_status = models.BooleanField()
    source_id = models.CharField(max_length=250)
    price_available = models.BooleanField(default=0)
    api_available = models.BooleanField(default=0)
    api_token = models.CharField(max_length=250)
    api_user_id = models.IntegerField()
    price_language = models.CharField(max_length=3)
    is_active = models.BooleanField()
    price_schedule = models.CharField(max_length=500)
    price_email = models.TextField()

    def __str__(self):
        return self.code


class CustomerAgreementBak(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    customer_id = models.IntegerField()
    currency_id = models.IntegerField()
    price_type_id = models.IntegerField()
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    is_status = models.BooleanField()
    source_id = models.CharField(max_length=250)
    price_available = models.BooleanField(default=0)
    api_available = models.BooleanField(default=0)
    api_token = models.CharField(max_length=250)
    api_user_id = models.IntegerField()
    price_language = models.CharField(max_length=3)
    is_active = models.BooleanField()
    price_email = models.TextField()

    def __str__(self):
        return self.code


class CustomerCard(models.Model):
    customer_id = models.IntegerField()
    name = models.CharField(max_length=250)
    card = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id


class CustomerContact(models.Model):
    customer_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    is_user = models.BooleanField()
    source_id = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id


class CustomerDiscount(models.Model):
    customer_id = models.IntegerField()
    agreement_id = models.IntegerField()
    criteria_id = models.IntegerField()
    criteria_type = models.CharField(max_length=250)
    discount = models.DecimalField(max_digits=15, decimal_places=2)
    price_type_id = models.IntegerField()

    def __str__(self):
        return self.customer_id


class CustomerPoint(models.Model):
    customer_id = models.IntegerField()
    name = models.CharField(max_length=500)
    source_id = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id


class Balance(models.Model):
    customer_id = models.IntegerField()
    currency_id = models.CharField(max_length=250)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    past_due = models.DecimalField(max_digits=15, decimal_places=2)
    agreement_id = models.IntegerField()

    def __str__(self):
        return self.customer_id


class CacheApi(models.Model):
    partner_code = models.CharField(max_length=250)
    search_number = models.CharField(max_length=250)
    response_api = models.TextField()
    response_date = models.DateTimeField()

    def __str__(self):
        return self.partner_code


class Category(models.Model):
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=300)
    url = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CategoryMapping(models.Model):
    partner_code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    category_id = models.ManyToManyField(Category, related_name="categorymapping_category")

    def __str__(self):
        return self.partner_code

    class Meta:
        verbose_name = "CategoryMapping"
        verbose_name_plural = "CategoryMappings"


class Constant(models.Model):
    code = models.CharField(max_length=250)
    value = models.TextField()

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Constant"
        verbose_name_plural = "Constant"


class Content(models.Model):
    alias = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField()
    published = models.BooleanField(default=0)
    main_image = models.ImageField(upload_to="content/")
    category_id = models.ManyToManyField(Category, related_name="content_category")
    title = models.CharField(max_length=300)
    intro_text = models.CharField(max_length=300)
    full_text = models.TextField()
    meta_tag_title = models.CharField(max_length=300)
    meta_tag_description = models.CharField(max_length=300)
    meta_tag_keyword = models.CharField(max_length=300)
    geo = models.CharField(max_length=250)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"


class CatalogCategory(models.Model):
    parent_id = models.IntegerField()
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=500)
    source_id = models.CharField(max_length=250)
    enabled = models.BooleanField(default=1)
    sort_index = models.IntegerField()
    content_id = models.ManyToManyField(Content, related_name="catalogcategory_content")

    def __str__(self):
        return self.parent_id

    class Meta:
        verbose_name = "CatalogCategory"
        verbose_name_plural = "CatalogCategories"


class Cross(models.Model):
    product_id = models.ManyToManyField(Product, related_name="cross_product")
    brand_name = models.CharField(max_length=300)
    article_nr = models.CharField(max_length=300)
    search_nr = models.CharField(max_length=300)

    def __str__(self):
        return self.product_id

    class Meta:
        verbose_name = "Cross"
        verbose_name_plural = "Crosses"


class CrossErrorStatistic(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    search_number = models.CharField(max_length=1000)
    comment = models.CharField(max_length=1000)
    customer_id = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user_id


class DeficitReserve(models.Model):
    product_id = models.IntegerField()
    sale_policy = models.CharField(max_length=250)
    amount = models.IntegerField()

    def __str__(self):
        return self.product_id


class DeliveryCity(models.Model):
    service_id = models.IntegerField()
    region = models.CharField(max_length=250)
    ref = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(default=datetime.today)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.service_id


class DeliveryMethod(models.Model):
    code = models.CharField(max_length=250)
    region_available = models.TextField()
    method_code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    comment = models.TextField()
    red = models.TextField()

    def __str__(self):
        return self.code


class DeliveryPoint(models.Model):
    service_id = models.IntegerField()
    city_id = models.IntegerField()
    street = models.CharField(max_length=250)
    ref = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    latitude = models.CharField(max_length=250)
    max_weight = models.DecimalField(max_digits=15, decimal_places=3)

    def __str__(self):
        return self.service_id


class DeliveryService(models.Model):
    name = models.CharField(max_length=250)
    has_to_door = models.BooleanField()
    parameters = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class DropshippingWallet(models.Model):
    order_id = models.IntegerField()
    agreement_id = models.IntegerField()
    currency_id = models.IntegerField()
    debit = models.DecimalField(max_digits=15, decimal_places=2)
    credit = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.order_id


class DropshippingWalletTransfer(models.Model):
    order_id = models.IntegerField()
    agreement_id = models.IntegerField()
    sum = models.DecimalField(max_digits=15, decimal_places=2)
    currency_id = models.IntegerField()
    date = models.DateTimeField()
    card = models.IntegerField()

    def __str__(self):
        return self.order_id


class GalleryImage(models.Model):
    type = models.CharField(max_length=250)
    ownerId = models.CharField(max_length=250)
    rank = models.IntegerField()
    name = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.type


class Manager(models.Model):
    inner_name = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    comment = models.CharField(max_length=250)
    source_id = models.CharField(max_length=250)

    def __str__(self):
        return self.inner_name


class Offer(models.Model):
    name = models.CharField(max_length=250)
    group = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    source_id = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.IntegerField()
    agreement_id = models.IntegerField()
    status = models.IntegerField()
    delivery_method = models.CharField(max_length=250)
    create_date = models.DateTimeField(default=datetime.today)
    update_date = models.DateTimeField()
    comment = models.TextField()
    point_id = models.IntegerField()
    delivery_service_id = models.IntegerField()
    delivery_city_id = models.IntegerField()
    delivery_point_id = models.IntegerField()
    delivery_contact = models.CharField(max_length=250)
    delivery_contact_phone = models.CharField(max_length=250)
    order_number = models.CharField(max_length=250)
    waybill_number = models.CharField(max_length=250)
    invoice_number = models.CharField(max_length=250)
    source = models.CharField(max_length=250)
    is_pay_on_delivery = models.BooleanField()
    pay_on_delivery_sum = models.DecimalField(max_digits=15, decimal_places=2)
    import_reason = models.TextField()
    import_status = models.CharField(max_length=250)
    partner_code = models.CharField(max_length=250)
    declared_sum = models.DecimalField(max_digits=15, decimal_places=2)
    declared_currency = models.IntegerField()
    source_type = models.CharField(max_length=250)
    delivery_contact_surname = models.CharField(max_length=250)
    declaration_number = models.CharField(max_length=250)
    delivery_contact_middlename = models.CharField(max_length=250)
    delivery_is_invoice_off = models.IntegerField()

    def __str__(self):
        return self.user_id


class OrderItem(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    currency_id = models.IntegerField()
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    source = models.CharField(max_length=250)
    reserved = models.IntegerField()
    executed = models.IntegerField()
    old_qty = models.IntegerField()
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    update_date = models.DateTimeField()
    purchase_qty = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_currency_id = models.IntegerField()
    purchase_order_id = models.IntegerField()
    purchase_item_id = models.IntegerField()
    partner_branch = models.CharField(max_length=250)

    def __str__(self):
        return self.order_id


class OrderPayment(models.Model):
    order_id = models.IntegerField()
    sum = models.DecimalField(max_digits=15, decimal_places=2)
    date_payment = models.DateTimeField(default=datetime.today)
    currency_id = models.IntegerField()
    payment_sum = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.TextField()
    receiver_commission = models.DecimalField(max_digits=15, decimal_places=2)
    sender_commission = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.order_id


class OrderSourceStatistic(models.Model):
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    source_type = models.CharField(max_length=250)
    add_date = models.DateTimeField()

    def __str__(self):
        return self.product_id


class PartnerApi(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    token = models.CharField(max_length=250)
    margin = models.DecimalField(max_digits=15, decimal_places=2)
    percent_prepayment = models.DecimalField(max_digits=15, decimal_places=2)
    show_branch = models.BooleanField(default=1)
    enabled = models.BooleanField(default=0)

    def __str__(self):
        return self.code


class PartnerApiCache(models.Model):
    partner_code = models.CharField(max_length=250)
    search_number = models.CharField(max_length=250)
    response_date = models.DateTimeField()
    product_json = models.TextField()

    def __str__(self):
        return self.partner_code


class PartnerCategory(models.Model):
    partner_code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    parent_id = models.IntegerField()
    response_date = models.DateTimeField()

    def __str__(self):
        return self.partner_code


class PartnerCategoryCache(models.Model):
    partner_code = models.CharField(max_length=250)
    category_id = models.IntegerField()
    response_date = models.DateTimeField()
    product_json = models.TextField()

    def __str__(self):
        return self.partner_code


class PartnerStock(models.Model):
    product_id = models.IntegerField()
    partner_code = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    qty = models.IntegerField()
    supply_date = models.DateField()
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.product_id


class Price(models.Model):
    product_id = models.IntegerField()
    price_type_id = models.IntegerField()
    currency_id = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.product_id


class PriceBuffer(models.Model):
    code = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    price_category = models.CharField(max_length=250)
    specification = models.CharField(max_length=250)
    article = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=250)
    rest = models.IntegerField()
    agreement_id = models.IntegerField()
    sort_indexcurrency = models.CharField(max_length=300)
    pack_qty = models.IntegerField()
    create_date = models.DateTimeField(default=datetime.today)

    def __str__(self):
        return self.code





class PriceType(models.Model):
    name = models.CharField(max_length=250)
    source_id = models.CharField(max_length=250)
    enabled = models.IntegerField()
    sort_index = models.IntegerField()
    access_policy_data = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProductApiMap(models.Model):
    product_id = models.IntegerField()
    partner_code = models.CharField(max_length=250)
    api_key = models.CharField(max_length=250)

    def __str__(self):
        return self.product_id


class ProductApplicability(models.Model):
    product_id = models.IntegerField()
    vehicle = models.CharField(max_length=250)
    modification = models.CharField(max_length=250)
    engine = models.CharField(max_length=250)
    year = models.CharField(max_length=250)

    def __str__(self):
        return self.product_id


class ProductDescription(models.Model):
    product_id = models.IntegerField()
    property = models.CharField(max_length=250)
    value = models.TextField()

    def __str__(self):
        return self.product_id


class ProductErrorStatistic(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    error_comment = models.CharField(max_length=1000)
    status = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField()
    admin_comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.product_id


class Profile(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=250)
    public_email = models.CharField(max_length=250)
    gravatar_email = models.CharField(max_length=250)
    gravatar_id = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    bio = models.TextField()

    def __str__(self):
        return self.user_id


class PromoSale(models.Model):
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    type = models.CharField(max_length=300)
    is_visible = models.BooleanField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.customer_id


class Region(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class RunString(models.Model):
    created_date = models.DateTimeField(default=datetime.today)
    updated_date = models.DateTimeField()
    full_text = models.CharField(max_length=1000)
    comment = models.CharField(max_length=300)
    published = models.BooleanField(default=0)

    def __str__(self):
        return self.created_date


class Sale(models.Model):
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    qty = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.product_id


class SaleHistory(models.Model):
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self):
        return self.product_id


class SaleProductRelated(models.Model):
    product_id = models.IntegerField()
    related_product_id = models.IntegerField()
    qty_index = models.DecimalField(max_digits=15, decimal_places=2)
    calculation_type = models.CharField(max_length=250)

    def __str__(self):
        return self.product_id


class SaleTask(models.Model):
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self):
        return self.product_id


class ScenarioPolicy(models.Model):
    sale_policy = models.CharField(max_length=250)
    deficit_available = models.BooleanField(default=0)
    online_reserve = models.BooleanField(default=0)
    online_order = models.BooleanField(default=0)

    def __str__(self):
        return self.sale_policy


class SearchRequest(models.Model):
    user_id = models.IntegerField()
    search_keyword = models.CharField(max_length=250)
    search_keyword_clean = models.CharField(max_length=250)
    is_result = models.BooleanField()
    product_list = models.TextField()
    is_added_in_cart = models.BooleanField()
    product_add_in_cart = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.user_id


class SearchRequestBufferIgnore(models.Model):
    search_keyword_clean = models.CharField(max_length=250)

    def __str__(self):
        return self.search_keyword_clean


class SendPriceBuffer(models.Model):
    agreement_id = models.IntegerField()
    price_email = models.CharField(max_length=250)
    customer_id = models.IntegerField()

    def __str__(self):
        return self.agreement_id


class SocialAccount(models.Model):
    user_id = models.IntegerField()
    provider = models.CharField(max_length=300)
    client_id = models.CharField(max_length=300)
    data = models.TextField()
    code = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.today)
    email = models.CharField(max_length=300)
    username = models.CharField(max_length=300)

    def __str__(self):
        return self.user_id


class Stock(models.Model):
    product_id = models.IntegerField()
    stock_name = models.CharField(max_length=300)
    amount_total = models.IntegerField()
    amount_account = models.IntegerField()

    def __str__(self):
        return self.product_id


class Token(models.Model):
    user_id = models.IntegerField()
    code = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=datetime.today)
    type = models.IntegerField()

    def __str__(self):
        return self.user_id


class UploadProduct(models.Model):
    upload_id = models.IntegerField()
    created = models.DateTimeField()
    name = models.CharField(max_length=300)
    article = models.CharField(max_length=300)
    search_key = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    comment = models.CharField(max_length=1000)
    branch = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    qty = models.IntegerField()
    supply = models.CharField(max_length=300)

    def __str__(self):
        return self.upload_id


class UploadSetting(models.Model):
    partner_code = models.CharField(max_length=250)
    file_name = models.CharField(max_length=250)
    first_row = models.IntegerField()
    mapping = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()
    rate = models.DecimalField(max_digits=15, decimal_places=5)
    encoding = models.CharField(max_length=250)
    compare_name = models.IntegerField()

    def __str__(self):
        return self.partner_code


class UserRequest(models.Model):
    user_id = models.IntegerField()
    subject = models.CharField(max_length=250)
    body = models.TextField()
    request_type_id = models.IntegerField()
    source_id = models.CharField(max_length=250)
    checked = models.BooleanField()
    date_request = models.DateTimeField()

    def __str__(self):
        return self.user_id


class UserRequestType(models.Model):
    manager_id = models.IntegerField()
    name = models.CharField(max_length=300)
    comment = models.CharField(max_length=300)


    def __str__(self):
        return self.manager_id


class WaitList(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    date_add = models.DateTimeField()
    send_message = models.BooleanField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.product_id


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "RatingStar"
        verbose_name_plural = "RatingStars"


class Rating(models.Model):
    ip = models.CharField(max_length=50)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
