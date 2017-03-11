from sklearn.neural_network import MLPClassifier

# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
clf = MLPClassifier(activation='relu', solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1,
                    max_iter=200)

# Get input