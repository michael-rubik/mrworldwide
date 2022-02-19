import Constants
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helper_functions import *

from alpha_vantage.timeseries import TimeSeries


ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
# Get json object with the intraday data and another with  the call's metadata
data = pd.DataFrame
data, meta_data = ts.get_daily(symbol = 'GOOGL', outputsize='full')

print("data: ", data)