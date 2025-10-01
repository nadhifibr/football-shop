from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'brand', 'stock']
    widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }),
            "price": forms.NumberInput(attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            }),
        }