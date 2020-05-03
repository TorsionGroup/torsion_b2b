from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Brand, Product, Category, Content, PriceCategory, ReviewContent, ReviewProduct, Account
from .forms import UserCreationForm, UserChangeForm


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'article', 'specification', 'sort_price', 'is_active')
    list_display_links = ('name',)
    search_fields = ('name', 'article',)
    save_on_top = True


@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'inner_name', 'source_id')
    list_display_links = ('inner_name',)


class ReviewInLine(admin.StackedInline):
    model = ReviewContent, ReviewProduct


@admin.register(ReviewContent)
class ReviewContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'email', 'content')
    list_display_links = ('name',)
    search_fields = ('name', 'content',)


@admin.register(ReviewProduct)
class ReviewProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'email', 'product')
    list_display_links = ('name',)
    search_fields = ('name', 'product',)


@admin.register(Account)
class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'phone', 'date_of_birth', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()
