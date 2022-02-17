from wsgiref.util import request_uri
import Constants
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helper_functions import *

alpha_vantage_query = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"

api_uri = Constants.API_URIS.get("alpha vantage")

api_key = Constants.API_KEYS.get("alpha vantage") # req
function = "TIME_SERIES_INTRADAY" #req
symbol = "IBM" #req
interval = "5min" #req
adjusted = "true"#/"false"
outputsize = "compact"#/"full"
datatype = "json"#/"csv"
request_url = (api_uri
    + "?function="
    + function
    + "&symbol="
    + symbol
    + "&interval="
    + interval
    + "&datatype="
    + datatype
    + "&adjusted="
    + adjusted
    + "&outputsize="
    + outputsize
    + "&apikey="
    +  api_key
    )

response = requests.get(request_url)
data = response.json()
if "Error Message" in data:
    print("Error: ", data["Error Message"])
    quit()

data = data.json()
#df = pd.json_normalize(data["Time Series (" + interval + ")"])[::-1]
print(data)

#print("head: ", df.head)
#print("tail: ", df.tail)
#print("shape: ", df.shape)

#df.plot(x = "date", y = "open", kind = 'scatter')

#plt.show()
