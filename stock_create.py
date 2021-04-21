import csv
import plotly.express as px
import plotly
import pandas as pd
import requests
import sys
from alpha_vantage.timeseries import TimeSeries
import json
import plotly.graph_objs as go
import numpy as np


key = 'VG7VFW3TBRFINU4E'


# Function Name: stock_handler
# parameters: symbol(stock)
# Purpose: Given a symbol(stock symbol specifically) this function accesses the alphavantage api
# and generates a table based off the information given
# Known Issues: None at the moment

def stock_handler(symbol):
    base_url = 'https://www.alphavantage.co/query?'

    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'datatype': 'csv',
        'apikey': key,
        }

    response = requests.get(base_url, params=params)

    with open('stock.csv', 'wb') as file:
        file.write(response.content)



def user_messaging():
 
    account_sid = 'ACf44018909f37667ae6228c396c4e9d8b' 
    auth_token = '[AuthToken]' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create(         
                              to='+19783970339' 
                          ) 
 
    print(message.sid)


def latest_change(filename, percent):
    df = pd.read_csv(filename)
    percent_change = int(percent) / 100

    print(df.head(3))
    
    if df.iloc[0, 1] - df.iloc[1, 1] > 0:
        percent_change = 1 - (df.iloc[0, 1] / df.iloc[1, 1])
        return percent_change
        
    elif df.iloc[0, 1] - df.iloc[1, 1] == 0:
        percent_change = 1 - (df.iloc[0, 1] / df.iloc[1, 1])
        return percent_change
    elif df.iloc[0, 1] - df.iloc[1, 1] < 0:
        percent_change = 1 - (df.iloc[0, 1] / df.iloc[1, 1])
        return percent_change


if __name__ == '__main__':
   stock_handler('AAPL')