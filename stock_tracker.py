from lib2to3.pgen2.pgen import DFAState
import Constants
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from helper_functions import *
from alpha_vantage.timeseries import TimeSeries
from pathlib import Path

def getFromAPI(symbol):
    ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_daily(symbol = symbol, outputsize='full')


    columns = ["open", "high", "low", "close", "volume"]
    data.columns = columns

    data["TradeDate"] = data.index.date

    data.to_csv(f'{symbol}.csv')
    return data

symbol = 'GOOGL'
path = Path(f'./{symbol}.csv')

try:
    df = pd.read_csv(f'{symbol}.csv')
except:
    df = getFromAPI(symbol)

df.plot()

plt.show()