from django import forms

from .models import Product


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['model', 'price', 'quantity', 'category', 'subcategory', 'article', 'image']
