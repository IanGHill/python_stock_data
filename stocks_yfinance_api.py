import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import json

with open("apple.json") as json_file:
    apple_info = json.load(json_file)

# print(apple_info['country'])

apple = yf.Ticker("AAPL")
apple_share_price_data = apple.history(period="max")
# print(apple_share_price_data.head())

apple_share_price_data.reset_index(inplace=True)

plt.plot(apple_share_price_data['Date'], apple_share_price_data['Open'])
plt.show()