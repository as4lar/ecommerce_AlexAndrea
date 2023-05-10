
from django import forms
from .models import Product, Brand

class ProductCreate(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=100)