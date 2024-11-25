from django import forms
from .models import Stock

class Addstock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker','name','quantity','purch_price']

class Removestock(forms.Form):
    ticker = forms.CharField(max_length=10, label='Stock Ticker')