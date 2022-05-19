import numpy as np 
import pandas as pd
import requests
import secrets
symbol='AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_059b97af715d417d9f49f50b51b1c448'
data = requests.get(api_url).json()
print(data)