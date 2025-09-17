from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description","category", "thumbnail", "is_featured"]


class DeleteProductForm(forms.Form):
    product_id = forms.UUIDField(label="ID Produk")  