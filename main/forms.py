from django.forms import ModelForm
from main.models import Product
from django import forms
from django.utils.html import strip_tags

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
    
    def clean_name(self):
        title = self.cleaned_data["name"]
        return strip_tags(title)

    def clean_description(self):
        content = self.cleaned_data["description"]
        return strip_tags(content)

    def clean_brand(self):
        content = self.cleaned_data["brand"]
        return strip_tags(content)