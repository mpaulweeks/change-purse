import json

"""
expects raw.json file with contents from
https://api.coinmarketcap.com/v1/ticker/?limit=0
"""

with open('raw.json') as f:
    market = json.load(f)
    ticker_names = {
        t['symbol']: t['name']
        for t in market
    }
with open('ticker_names.json', 'wb') as f:
    json.dump(ticker_names, f, separators=(',', ':'))
