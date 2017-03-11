from sklearn.neural_network import MLPClassifier
import json
import numpy as np
# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPClassifier(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1,
                    max_iter=200)


# Reading data back
with open('data.json', 'r') as outfile:
    data = json.load(outfile)
    # Fetch data into X
    X = np.zeros([len(data), 7])
    y = np.zeros([len(data) - 1])
    for i in range(0, len(X)):
        X[i][0] = data[i]['high']
        X[i][1] = data[i]['quoteVolume']
        X[i][2] = data[i]['volume']
        X[i][3] = data[i]['low']
        X[i][4] = data[i]['close']
        X[i][5] = data[i]['weightedAverage']
        X[i][6] = data[i]['open']
    for i in range(0, len(X) - 1):
        print(np.round(10000.0 * (X[i + 1][6] - X[i][6])))
        y[i] = np.round(10000.0 * (X[i + 1][6] - X[i][6]))

X = X[0: len(X) - 1]
clf.fit(X, y)
print(X[0])
print("Final result: " + str(clf.predict([X[0]])))

