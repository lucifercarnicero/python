import numpy as np
from matplotlib import pyplot as plt
import random
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Generación de los valores X e y
y = []
X = np.array(list(range(80)))[:, np.newaxis]
for i in range(len(X)):
    y.append(20 + X[i] + random.random() * 50)

# Generación del kernel
kernel = RBF(length_scale=10.0)

fig, axs = plt.subplots(1, 3, figsize=(17, 3))

# Generar la regresión gaussiana para diversos valores de alfa
for i, alpha in zip([0, 1, 2], [0.01, 0.05, 0.08]):
    gp = GaussianProcessRegressor(alpha=alpha, kernel=kernel)

    # Generación del modelo y predicción
    gp.fit(X, y)
    y_pred, sigma = gp.predict(X, return_std=True)

    # Graficación de los resultados
    axs[i].plot(X, y, 'y.', markersize=11, label='Muestras')
    axs[i].plot(X, y_pred, 'k-', label='Predicción')
    axs[i].legend()
    axs[i].set_title('Alpha = ' + str(alpha))
    axs[i].grid()

plt.show()
