from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime


def home_view(request):
    template_name = 'shop/index.html'
    context = {}
    return render(request, template_name, context)