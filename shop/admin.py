from django.contrib import admin

from shop.models import Category, Product, Article, SubCategory, Review, AbstractUser, User
from .forms import ProductAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('id',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'price', 'category', 'subcategory', 'article', 'slug','rating')
    list_filter = ('model', 'price', 'category', 'subcategory', 'article','rating')
    search_fields = ('model', 'price', 'category', 'subcategory', 'article','rating')
    form = ProductAdminForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'description','mark', 'product', 'name')
    list_filter = ('mark', 'product', 'name')
    search_fields = ('mark', 'product', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass