from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
#generación de los datos de manera aleatoria
numero_muestras = 50
X = np.zeros((numero_muestras,2))
y = np.zeros((numero_muestras,2))
X[:,0] = np.array(list(range(numero_muestras)))
y[:,0] = 5+X[:,0] + np.random.rand(numero_muestras)*20
print(y)
#creación y entrenamiento del modelo
linear_regression = linear_model.LinearRegression()
linear_regression.fit(X,y)
w = linear_regression.coef_
b = linear_regression.intercept_
print(w[0][0])
print(b[0])
#calculo de los valores predichos y muestra por pantalla
y_predicted = linear_regression.predict(X)
plt.plot(X,y_predicted,'k-')
plt.plot(X,y,'yo')
plt.show()
