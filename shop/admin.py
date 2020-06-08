from django.contrib import admin

# from .models import Car, Review
# from .forms import ReviewAdminForm
from shop.models import Category, Product, Article, SubCategory
from .forms import ProductAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', 'price', 'category', 'subcategory', 'article', 'slug')
    list_filter = ('model', 'price', 'category', 'subcategory', 'article')
    search_fields = ('model', 'price', 'category', 'subcategory', 'article')
    form = ProductAdminForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)