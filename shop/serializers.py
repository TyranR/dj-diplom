from rest_framework import serializers
from shop.models import Category, Product, SubCategory, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    article = ArticleSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'model', 'quantity', 'price', 'category', 'subcategory', 'article', 'image')
