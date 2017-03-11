from sklearn.neural_network import MLPRegressor
import json
import numpy as np
# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPRegressor(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(80, 35, 25, 10), random_state=1,
                    max_iter=2000)

btc_dash = ()
btc_eth = ()
btc_ltc = ()
btc_xmr = ()
grc_btc = ()

with open('json/btc-dash.json', 'r') as f:
    btc_dash = json.load(f)
with open('json/btc-eth.json', 'r') as f:
    btc_eth = json.load(f)
with open('json/btc-ltc.json', 'r') as f:
    btc_ltc = json.load(f)
with open('json/btc-xmr.json', 'r') as f:
    btc_xmr = json.load(f)
with open('json/grc-btc.json', 'r') as f:
    grc_btc = json.load(f)

btc_dash = btc_dash[0: 100000]
btc_eth = btc_eth[0: 100000]
btc_ltc = btc_ltc[0: 100000]
btc_xmr = btc_xmr[0: 100000]
grc_btc = grc_btc[0: 100000]

# Fetch data into X
X = np.zeros([len(btc_dash), 35])
y = np.zeros([len(btc_dash) - 1])
for i in range(0, len(X) - 1):
    X[i][0] = btc_dash[i]['high']
    X[i][1] = btc_dash[i]['quoteVolume']
    X[i][2] = btc_dash[i]['volume']
    X[i][3] = btc_dash[i]['low']
    X[i][4] = btc_dash[i]['close']
    X[i][5] = btc_dash[i]['weightedAverage']
    X[i][6] = btc_dash[i]['open']
    X[i][7] = btc_eth[i]['high']
    X[i][8] = btc_eth[i]['quoteVolume']
    X[i][9] = btc_eth[i]['volume']
    X[i][10] = btc_eth[i]['low']
    X[i][11] = btc_eth[i]['close']
    X[i][12] = btc_eth[i]['weightedAverage']
    X[i][13] = btc_eth[i]['open']
    X[i][14] = btc_ltc[i]['high']
    X[i][15] = btc_ltc[i]['quoteVolume']
    X[i][16] = btc_ltc[i]['volume']
    X[i][17] = btc_ltc[i]['low']
    X[i][18] = btc_ltc[i]['close']
    X[i][19] = btc_ltc[i]['weightedAverage']
    X[i][20] = btc_ltc[i]['open']
    X[i][21] = btc_xmr[i]['high']
    X[i][22] = btc_xmr[i]['quoteVolume']
    X[i][23] = btc_xmr[i]['volume']
    X[i][24] = btc_xmr[i]['low']
    X[i][25] = btc_xmr[i]['close']
    X[i][26] = btc_xmr[i]['weightedAverage']
    X[i][27] = btc_xmr[i]['open']
    X[i][28] = grc_btc[i]['high']
    X[i][29] = grc_btc[i]['quoteVolume']
    X[i][30] = grc_btc[i]['volume']
    X[i][31] = grc_btc[i]['low']
    X[i][32] = grc_btc[i]['close']
    X[i][33] = grc_btc[i]['weightedAverage']
    X[i][34] = grc_btc[i]['open']
for i in range(0, len(X) - 1):
    #print(str(np.float64(X[i + 1][6]) / np.float64(X[i][6])))
    ratio = np.float128((X[i + 1][6])) / np.float128(X[i][6])
    y[i] = ratio


print("LENGTH: " + str(len(X)))

trX = X[0: len(X) / 2]
testX = X[len(X) / 2: len(X) - 1]
trY = y[0: len(X) / 2]
testY = y[len(X) / 2: len(X) - 1]

gridcoin = 1000000
bitcoin = 10

starting_money = (bitcoin + gridcoin * (trX[len(trX) - 1][6]))

# Train algorithm
clf.fit(trX, trY)

for i in range(0, len(testX) - 1):
    prediction = clf.predict([testX[i]])
    if(prediction > 1):
        if(bitcoin > (prediction-1)*(testX[i][6])*10000):
            bitcoin -= (prediction-1)*(testX[i][6]*10000)
            gridcoin += (prediction-1)*10000
    else:
        if(gridcoin > (1-prediction)*10000):
            gridcoin -= (1-prediction)*10000
            bitcoin += (1-prediction)*(testX[i][6]*10000)

print("Final gridcoin: " + str(gridcoin))
print("Final bitcoin: " + str(bitcoin))
ending_money = (bitcoin + gridcoin * (testX[len(testX) - 1][6]))
print("Starting money: " + str(starting_money))
print("Ending money: " + str(ending_money))
print("Profit: " + str(ending_money - starting_money))
print("Ratio: " + str(float(ending_money) / starting_money))

expecting_profit = (10 + 1000000 * (testX[len(testX) - 1][6])) - starting_money
print("Expected profit: " + str(expecting_profit))
print("Expected ratio: " + str((10 + 1000000 * (testX[len(testX) - 1][6]))/ float(starting_money)))

print("START: " + str(testX[0][6]))
print("END: " + str(testX[len(testX) - 1][6]))

