from django.shortcuts import render
from django.http import HttpResponse
import pandas_datareader.data as pdr
import datetime
import yfinance as yf

yf.pdr_override()

# Create your views here.

def index(requests):
    #pair = ['USDJPY', 'EURJPY', 'AUDJPY', 'GBPJPY']
    pair = ['USDJPY']
    end = datetime.date.today()
    start = end - datetime.timedelta(days=150)

    for i in range(len(pair)):
        rate = get_exchange_rate(pair[i], start, end)
    
    params = {
        'data': rate
    }

    return render(requests, 'index.html', params)

def get_exchange_rate(pair, start, end):
    selected = f"{pair}=X"
    df = pdr.get_data_yahoo("USDJPY=X", start, end).drop(['Volume', 'Adj Close'], axis=1)
    
    return df