import urllib
from pprint import pprint

from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Category, Product, Review
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
    context = {}
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


# def product_view(request, pk):
#     template = 'app/product_detail.html'
#     product = get_object_or_404(Product, id=pk)
#     form = ReviewForm
#     key_exists = 'reviewed_products' in request.session
#     if not key_exists:
#         request.session['reviewed_products'] = []
#         reviewed_products = []
#     else:
#         reviewed_products = request.session['reviewed_products']
#     if request.method == 'GET':
#         if not pk in reviewed_products:
#             is_review_exist = 0
#         else:
#             is_review_exist = 1
#     if request.method == 'POST':
#         if not pk in reviewed_products:
#             text = request.POST.get('text')
#             new_review = Review.objects.create(text=text, product=product)
#             reviewed_products.append(pk)
#             request.session['reviewed_products'] = reviewed_products
#             is_review_exist = 0
#         else:
#             is_review_exist = 1
#     all_review = Review.objects.filter(product__id=pk)
#     print(request.session['reviewed_products'])
#     context = {
#         'form': form,
#         'product': product,
#         'reviews': all_review,
#         'is_review_exist': is_review_exist
#     }
#
#     return render(request, template, context)


def category_view(request):
    template = 'shop/categorys.html'
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
    prev_page_url = reverse('category_view') + '?' + str(prev_page_url)
    next_page_url = reverse('category_view') + '?' + str(next_page_url)
    return render(request, template, context={
        'products': articles,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })