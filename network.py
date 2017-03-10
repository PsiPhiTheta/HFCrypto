from sklearn.neural_network import MLPClassifier

# Array X of size (n_samples, n_features): Holds training samples
# Array y of size (n_samples): Holds the target values
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1,
                    max_iter=200)
clf.fit(X, y)
y = clf.predict([[2., 2.], [-1., -2.]])
print(y)