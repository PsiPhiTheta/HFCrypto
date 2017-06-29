from sklearn.neural_network import MLPRegressor
import json
import numpy as np
# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPRegressor(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(8000, 3500, 2500, 1000), random_state=1,
                    max_iter=100)

data = np.empty((0, 1982), dtype=float)
with open('data.txt') as f:
    for line in f:
        currentline = line.strip('\n')
        currentline = currentline.split(',')
        currentline = currentline[0:len(currentline) - 1]
        data = np.vstack((data, currentline))

print("SHAPE: " + str(data.shape))
print("LENGTH: " + str(len(data)))

# Index of lowest ask for BTC_GRC is: 19 * 10 + 2
y = np.empty((len(data), 1), dtype=float)
for i in range(0, len(y) - 1):
    #print(str(np.float64(X[i + 1][6]) / np.float64(X[i][6])))
    ratio = np.float128((data[i + 1][192])) / np.float128(data[i][192])
    y[i] = ratio

trX = np.empty((len(data) / 2, 1982), dtype=float)
np.copyto(trX, data[len(data) / 2][:], casting="unsafe")

testX = np.empty((len(data) - len(data)/ 2, 1982), dtype=float)
np.copyto(testX, data[len(data)/2:len(data)][:], casting="unsafe")

trY = np.empty((len(data) / 2, 1), dtype=float)
print(trY.shape)
print(y.shape)
np.copyto(trY, y[len(data) / 2], casting="unsafe")

testY = np.empty((len(data) - len(data)/2, 0), dtype=float)
np.copyto(testY, y[len(data) / 2:len(data)], casting="unsafe")

gridcoin = 1000000
bitcoin = 10

starting_money = (bitcoin + gridcoin * (trX[len(trX) - 1][192]))

trY = trY.reshape((len(trY),))
print("trX: " + str(trX.shape))
print("trY: " + str(trY.shape))

# Train algorithm
clf.fit(trX, trY)

for i in range(0, len(testX) - 1):
    prediction = clf.predict([testX[i]])
    if(prediction > 1):
        if(bitcoin > (prediction-1)*(testX[i][192])*10000):
            bitcoin -= (prediction-1)*(testX[i][192]*10000)
            gridcoin += (prediction-1)*10000
    else:
        if(gridcoin > (1-prediction)*10000):
            gridcoin -= (1-prediction)*10000
            bitcoin += (1-prediction)*(testX[i][192]*10000)

print("Final gridcoin: " + str(gridcoin))
print("Final bitcoin: " + str(bitcoin))
ending_money = (bitcoin + gridcoin * (testX[len(testX) - 1][192]))
print("Starting money: " + str(starting_money))
print("Ending money: " + str(ending_money))
print("Profit: " + str(ending_money - starting_money))
print("Ratio: " + str(float(ending_money) / starting_money))

expecting_profit = (10 + 1000000 * (testX[len(testX) - 1][192])) - starting_money
print("Expected profit: " + str(expecting_profit))
print("Expected ratio: " + str((10 + 1000000 * (testX[len(testX) - 1][192]))/ float(starting_money)))

print("START: " + str(testX[0][192]))
print("END: " + str(testX[len(testX) - 1][192]))
