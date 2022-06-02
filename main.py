import numpy as np 
import pandas as pd
import requests
from secrets import IEX_CLOUD_API_TOKEN
import csv



symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
stocks = pd.read_csv('companies.csv')
print(stocks)
