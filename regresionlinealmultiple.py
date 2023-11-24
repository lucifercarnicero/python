import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Carga de los datos
diabetes = datasets.load_diabetes()

# Selección de la variable dependiente y de las independientes
y = diabetes.target
X = diabetes.data[:, np.newaxis, 2]
print(diabetes.data.shape)
print(diabetes.data[:, 2].shape)

# División en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

# Generación del método y entrenamiento
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X_train, y_train)

# Cálculo de valores predichos
y_train_predicted = linear_regression.predict(X_train)
y_test_predicted = linear_regression.predict(X_test)

# Cálculo de las diferencias entre predicho y real
train_MSD = mean_squared_error(y_train, y_train_predicted)
test_MSD = mean_squared_error(y_test, y_test_predicted)

# Graficación de las curvas predichas y de las reales
fig, axs = plt.subplots(1, 2, figsize=(15, 4))
axs[0].scatter(X_train, y_train, color='orange')
axs[0].plot(X_train, y_train_predicted, color='black')
axs[0].set_title('training set, MSD:{:.0f}'.format(train_MSD))
axs[1].scatter(X_test, y_test, color='gray')
axs[1].plot(X_test, y_test_predicted, color='black')
axs[1].set_title('testing set, MSD:{:.0f}'.format(test_MSD))

plt.show()
