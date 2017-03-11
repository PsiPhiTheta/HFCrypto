from sklearn.neural_network import MLPClassifier
import json
import numpy as np
# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPClassifier(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1,
                    max_iter=200)

# Reading data back
with open('data.json', 'r') as f:
    new_data = json.load(f)

print(new_data[0])

# Fetch data into X
# X = np.zeros(7, len(data))
# for i in range(0, len(data)):
#     for j in range(0, 7):
#         X[j,i] = data
