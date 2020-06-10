import urllib
from pprint import pprint

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Category, Product, Review, SubCategory, Article
from shop.serializers import CategorySerializer, ProductSerializer
from django.core.paginator import Paginator


class CategoryView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        pass


class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            new_product = serializer.save()
            return Response(new_product)
        else:
            return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        pass


def home_view(request):
    template_name = 'shop/index.html'
    all_products = Product.objects.all()
    all_category = Category.objects.all()
    all_subcategory = SubCategory.objects.all()
    all_articles = Article.objects.all()
    paginator = Paginator(Product.objects.all(), 3)
    current_page = request.GET.get('page', 1)
    things = paginator.get_page(current_page)
    prev_page_number = next_page_number = 0
    if things.has_previous():
        prev_page_number = int(current_page) - 1
    if things.has_next():
        next_page_number = int(current_page) + 1
    prev_page_url = urllib.parse.urlencode({'page': prev_page_number})
    next_page_url = urllib.parse.urlencode({'page': next_page_number})
    prev_page_url = str(prev_page_url)
    next_page_url = str(next_page_url)
    context = {
        'products': things,
        'all_products': all_products,
        'categorys': all_category,
        'articles': all_articles,
        'subcategorys': all_subcategory,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url
    }
    return render(request, template_name, context)



def show_product(request, slug):
    template = 'shop/product.html'
    all_entries = Product.objects.filter(slug=slug)
    for each in all_entries:
        model_product = each.id
    all_reviews = Review.objects.filter(product=model_product)
    context = {
        'product': all_entries,
        'reviews': all_reviews
    }
    return render(request, template, context)


def products(request, slug):
    template = 'shop/products_new.html'
    all_category = Category.objects.all()
    all_subcategory = SubCategory.objects.all()
    click_subcategory = SubCategory.objects.filter(slug=slug)
    for each in click_subcategory:
        product_name = each.id
        current_subcategory = each.name
    click_product = Product.objects.filter(subcategory=product_name)
    paginator = Paginator(Product.objects.all(), 2)
    current_page = request.GET.get('page', 1)
    articles = paginator.get_page(current_page)
    prev_page_number = next_page_number = 0
    if articles.has_previous():
        prev_page_number = int(current_page)-1
    if articles.has_next():
        next_page_number = int(current_page)+1
    prev_page_url = urllib.parse.urlencode({'page' : prev_page_number})
    next_page_url = urllib.parse.urlencode({'page': next_page_number})
    prev_page_url = slug + '?' + str(prev_page_url)
    next_page_url = slug + '?' + str(next_page_url)
    return render(request, template, context={
        'products': click_product,
        'categorys': all_category,
        'subcategorys': all_subcategory,
        'current': current_subcategory,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })


def login_view(request):
    template = 'shop/login.html'
    context = {}
    if request.user.is_authenticated:
        pass
    else:
        pass
    return render(request, template, context)


def cart_view(request):
    template = 'shop/cart.html'
    context = {}
    return render(request, template, context)

