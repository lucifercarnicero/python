import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# carga de los datos y almacenamiento de los diez primeros registros
df = pd.read_csv(r"data.csv")
X = df[['sqft_living']].values[:10]
y = df['price'].values[:10]
epocas = 100

# normalización de los datos
sc_x = StandardScaler()
sc_y = StandardScaler()
X_esc = sc_x.fit_transform(X)
y_esc = sc_y.fit_transform(y[:, np.newaxis]).flatten()

# creación de las matrices de datos de entrenamiento y prueba
X_ent, X_pru, y_ent, y_pru = train_test_split(X_esc, y_esc, test_size=0.3, random_state=50)

poly = PolynomialFeatures(degree=2)
X_ent_poly = poly.fit_transform(X_ent)
X_pru_poly = poly.fit_transform(X_pru)

# obtención de la regresión múltiple asociada
reg = LinearRegression()
reg.fit(X_ent_poly, y_ent)
print('Coeficientes:', reg.coef_)
print('Intercepto:', reg.intercept_)

# muestra de la función obtenida gráficamente y de la precisión
x_fit = np.arange(X_ent.min(), X_ent.max(), 1)[:, np.newaxis]
y_p = reg.predict(poly.fit_transform(x_fit))

plt.scatter(X_ent, y_ent, label="puntos de entrenamiento")
plt.plot(x_fit, y_p, color='gray')
plt.legend(loc='upper left')
plt.show()

print('Precision del modelo: {:.2f}'.format(reg.score(X_ent_poly, y_ent)))
