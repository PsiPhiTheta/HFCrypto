import requests
import time

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
    numberBids = 0;
    numberAsks = 0;
    sumOfBidsFirst = 0;
    sumOfBidsSecond = 0;
    sumOfAsksFirst = 0;
    sumOfAsksSecond = 0;
    for a in input:
        if(isinstance(input[a], dict)):
            for e in input[a]:
                if(isinstance(input[a][e], list)):
                    for i in range(0, len(input[a][e])):
                        if(e == 'asks'):
                            numberAsks += 1;
                            sumOfAsksFirst += float(input[a][e][i][0])
                            sumOfAsksSecond += float(input[a][e][i][1])
                        elif(e == 'bids'):
                            numberBids += 1;
                            sumOfBidsFirst += float(input[a][e][i][0])
                            sumOfBidsSecond += float(input[a][e][i][1])
        output.append(numberAsks)
        output.append(sumOfAsksFirst)
        output.append(sumOfAsksSecond)
        output.append(numberBids)
        output.append(sumOfBidsFirst)
        output.append(sumOfBidsSecond)
    return output

def currenciesParser(input, output):
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


currencies = ["BTC", "LTC", "ETH", "GRC", "DASH", "XMR", "ZEC", "REP"]

data = []
ticker = returnTicker()
data = parser(ticker, data)
print(len(data))
volume = return24Volume()
data = parser(volume, data)
print(len(data))
ob = returnOrderBook()
data = orderBookParser(ob, data)
print(len(data))
cp = returnCurrencies()
data = currenciesParser(cp, data)
print(len(data))
for c in currencies:
    lo = returnLoanOrders(c)
    data = loanOrderParser(lo, data)

print(len(data))