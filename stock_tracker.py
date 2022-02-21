import Constants
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from helper_functions import *

from alpha_vantage.timeseries import TimeSeries


ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_daily(symbol = 'GOOGL', outputsize='full')

#df = df[(datetime.datetime(df.dateTimeIndex)<datetime.datetime(2005,1,1))]

columns = ["open", "high", "low", "close", "volume"]
data.columns = columns

data["TradeDate"] = data.index.date

df = data[data.TradeDate<datetime.date(2005,1,1)]

print(df)