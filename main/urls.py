"""car_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .settings import *
from shop.views import *
import shop.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop.views.home_view, name='home'),
    path('index.html', shop.views.home_view, name='home2'),
    path('category_serial/', CategoryView.as_view()),
    path('products/<slug:slug>', shop.views.products, name='products'),
    path('product_serial/', ProductView.as_view()),
    path('product/<slug:slug>', shop.views.show_product, name='show_product'),
    path('cart/', shop.views.cart_view, name='cart'),
    path('sucess_payed/', shop.views.cart_clean, name='cart_clean'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # url(r'^accounts/', include('django.contrib.auth.urls'))
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
