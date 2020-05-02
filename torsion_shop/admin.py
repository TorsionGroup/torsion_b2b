from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Brand, Product, Category, Content, PriceCategory, ReviewContent, ReviewProduct


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


