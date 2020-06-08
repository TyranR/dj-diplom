from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer


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
    template = 'shop/phone.html'
    all_entries = Product.objects.filter(slug=slug)
    context = {'phone': all_entries}
    print(context)
    return render(request, template, context)