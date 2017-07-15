import requests
import pandas as pd

url = 'https://poloniex.com/public?command=returnLoanOrders&currency='

currencies = ["LTC", "ETH", "GRC", "BTC", "DASH", "XMR", "ZEC", "REP"]
features = ['txFee', 'minConf', 'disabled', 'delisted', 'frozen']

result = []

for currency in currencies:
    response = requests.get(url + currency)
    data = response.json()


    # Offers of each of the hardcoded currencies
    offerRate = 0
    offerAmount = 0
    try:
        for offer in data['offers']:
            offerRate += float(offer['rate'])
            offerAmount += float(offer['amount'])
        try:
            result.append(pd.to_numeric(offerRate / len(data['offers']), 'coerce'))
        except(ZeroDivisionError):
            result.append(float(0))
        try:
            result.append(pd.to_numeric(offerAmount / len(data['offers']), 'coerce'))
        except(ZeroDivisionError):
            result.append(float(0))
    except:
        for i in range(0,4):
            result.append(float('nan'))
        break

    # Demands of each of the HC'd currencies
    demandRate = 0
    demandAmount = 0
    for demand in data['demands']:
        demandRate += float(demand['rate'])
        demandAmount += float(demand['amount'])
    try:
        result.append(pd.to_numeric(demandRate / len(data['demands']), 'coerce'))
    except(ZeroDivisionError):
        result.append(float(0))
    try:
        result.append(pd.to_numeric(demandAmount / len(data['demands']), 'coerce'))
    except(ZeroDivisionError):
        result.append(float(0))

print(result)
