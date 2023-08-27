import math
from os import close
import time
import pandas_datareader as web
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)



def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print( Fore.GREEN + f"\r|{bar}| {percent:.2f}%", end="\r")

import yfinance as yf

ticker_list = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA', 'NVDA', 'PYPL', 'ADBE', 'INTC']
closing_prices = []

for ticker in ticker_list:
    data = yf.download(ticker, start='2023-01-01', end='2023-07-31')
    last_price = data['Close'].iloc[-1]
    closing_prices.append(last_price)
    progress_bar(ticker_list.index(ticker) + 1, len(ticker_list))

print("\nClosing prices:", closing_prices)
