from django.shortcuts import render,redirect
import os
from .forms import Addstock,Removestock
from .models import Stock
import requests

# Create your views here.
API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

def portfolio(request):
    stocks = Stock.objects.all()
    portfolio_data = []

    for stock in stocks:
        response = requests.get(BASE_URL,params={
            'function' : 'GLOBAL_QUOTE',
            'symbol' : stock.ticker,
            'apikey' : API_KEY
        })
        data = response.json().get("Global Quote", {})
        portfolio_data.append({
            'ticker' : stock.ticker,
            'name' : stock.name,
            'quantity' : stock.quantity,
            'current_price' : data.get('05. price', 'N/A'),
            'change_price' : data.get('10. change percent', 'N/A'),
        })
    return render(request,'portfolio.html',{'portfolio': portfolio_data})

def add_stock(request):
    if request.method == 'POST':
        form = Addstock(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = Addstock()

    return render(request,'add_stock.html',{'form':form})

def remove_stock(request):
    if request.method=='POST':
        form = Removestock(request.POST)
        if form.is_valid():
            Stock.objects.filter(ticker=form.cleaned_data['ticker']).delete()
            return redirect('portfolio')
    else:
        form = Removestock()

    return render(request,'remove_stock.html',{'form':form})