import requests
import numpy as np

def returnTicker():
    url = "https://poloniex.com/public?command=returnTicker"
    response = requests.get(url)
    data = response.json()
    return data

def return24Volume():
    url = "https://poloniex.com/public?command=return24hVolume"
    response = requests.get(url)
    data = response.json()
    return data

def parser(input, output):
    for i in input:
        if(isinstance(input[i], dict)):
            for j in input[i]:
                output.append(input[i][j])
    return output

def orderBookParser(input, output):
    for o in input:
        if (isinstance(input[o], dict)):
            for a in input[o]:
                if (isinstance(input[o][a], list)):
                    for e in range(0, len(input[o][a])):
                        for i in range(0, len(input[o][a][e])):
                            output.append(input[o][a][e][i])
    return output

def currenciesParser(input, output):
    currencies = ["LTC", "ETH", "GRC", "BTC", "DASH"]
    for c in input:
        for currency in currencies:
            if (c == currency):
                output.append(input[c]['txFee'])
    return output

def returnOrderBook():
    url = "https://poloniex.com/public?command=returnOrderBook&currencyPair=all&depth=10"
    response = requests.get(url)
    data = response.json()
    return data

def returnCurrencies():
    url = "https://poloniex.com/public?command=returnCurrencies"
    response = requests.get(url)
    data = response.json()
    return data

def returnLoanOrders(currency):
    url = "https://poloniex.com/public?command=returnLoanOrders&currency=" + currency
    response = requests.get(url)
    data = response.json()
    return data

def loanOrderParser(input, output):
    for i in input:
        totalRate = 0.0
        numberOrders = 0
        totalAmount = 0.0
        for a in range(0, len(input[i])):
            x = input[i][a]['rate']
            y = input[i][a]['amount']
            totalAmount += float(y)
            totalRate += float(x)
            numberOrders += 1
        output.append(totalRate)
        output.append(numberOrders)
        output.append(totalAmount)
    return output


currencies = ["LTC", "ETH", "GRC", "BTC", "DASH", "XMR", "ZEC", "REP"]
data = []
ticker = returnTicker()
data = parser(ticker, data)
volume = return24Volume()
data = parser(volume, data)
ob = returnOrderBook()
data = orderBookParser(ob, data)
cp = returnCurrencies()
data = currenciesParser(cp, data)
for c in currencies:
    lo = returnLoanOrders(c)
    data = loanOrderParser(lo, data)


print len(data)
print data
print data[0]
if(len(data) == 5595):
    with open('data.txt', 'a') as outfile:
        for i in range(0, len(data)):
            outfile.write(str(data[i]) + ',')
        outfile.write('\n')
