import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

# Genero valores aleatorios
np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)

# Añado ruido
y = np.sin(X).ravel()  # aplanar el array
y[::5] += 1 * (0.5 - np.random.rand(8))

# Valores del test 
T = np.linspace(0, 5, 500)[:, np.newaxis]

# KNeighborsRegressor con diferentes ponderaciones
n_neighbors = 5  # Número de vecinos a considerar
# Modelo con pesos uniformes
knn_uniform = KNeighborsRegressor(n_neighbors, weights='uniform')
knn_uniform.fit(X, y)

# Modelo con pesos basados en la distancia
knn_distance = KNeighborsRegressor(n_neighbors, weights='distance')
knn_distance.fit(X, y)

# Predigo los resultados de valores test T
y_pred_uniform = knn_uniform.predict(T)
y_pred_distance = knn_distance.predict(T)

# Muestro resultadoss
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, y_pred_uniform, color='navy', label='prediction (uniform)')
plt.axis('tight')
plt.legend()
plt.title(f"KNeighborsRegressor (uniform weights, k={n_neighbors})")

plt.subplot(1, 2, 2)
plt.scatter(X, y, color='darkorange', label='data')
plt.plot(T, y_pred_distance, color='navy', label='prediction (distance)')
plt.axis('tight')
plt.legend()
plt.title(f"KNeighborsRegressor (distance weights, k={n_neighbors})")

# Grafica
plt.tight_layout()
plt.show()
