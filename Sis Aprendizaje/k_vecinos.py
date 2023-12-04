import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
import random

# Generación de los valores de X e y
X = np.array(list(range(100)))[:, np.newaxis]
y = [20 + X[i] + random.random() * 60 for i in range(len(X))]

fig, axs = plt.subplots(2, 2, figsize=(15, 7))

# Cálculo de la regresión para diferentes números de vecinos
for i, n_neighbors in zip([0, 1, 2, 3], [2, 10, 18, 26]):
    knn_regressor = KNeighborsRegressor(n_neighbors)
    knn_model = knn_regressor.fit(X, y)
    y_prediction = knn_model.predict(X)
    axs[int(i / 2), i % 2].scatter(X, y, c='y')
    axs[int(i / 2), i % 2].plot(X, y_prediction, c='k')
    axs[int(i / 2), i % 2].set_title(f'Scikit KNeighborsRegressor, k={n_neighbors}')

plt.show()
