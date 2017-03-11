from sklearn.neural_network import MLPRegressor
import json
import numpy as np
# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPRegressor(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(10, 12, 8, 5), random_state=1,
                    max_iter=2000)

gridcoin_data = ()
monero_data = ()

# Reading data back
with open('gridcoin.json', 'r') as outfile:
    data = json.load(outfile)

    # Fetch data into X
    X = np.zeros([len(data), 7])
    y = np.zeros([len(data) - 1])
    for i in range(0, len(data)):
        X[i][0] = data[i]['high']
        X[i][1] = data[i]['quoteVolume']
        X[i][2] = data[i]['volume']
        X[i][3] = data[i]['low']
        X[i][4] = data[i]['close']
        X[i][5] = data[i]['weightedAverage']
        X[i][6] = data[i]['open']
    for i in range(0, len(data) - 1):
        #print(str(np.float64(X[i + 1][6]) / np.float64(X[i][6])))
        ratio = np.float64((X[i + 1][6])) / np.float64(X[i][6])
        y[i] = ratio


print("LENGTH: " + str(len(data)))

trX = X[50000: len(data) - 100000]
testX = X[len(data) - 150000: len(data) - 1]
trY = y[50000: len(data) - 100000]
testY = y[len(data) - 150000: len(data) - 1]

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

