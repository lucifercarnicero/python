import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv('reviews_sentiment.csv', delimiter=';')

# Seleccionar las características y la característica objetivo
X = df[['wordcount', 'sentimentValue']]
y = df['Star Rating']

# Asegurarte de que la característica objetivo esté en el rango de 1 a 5
y = y.clip(1, 5)  # Esto limita las valoraciones a un rango de 1 a 5

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Estandarizar 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear modelo KNNN
knn_regressor = KNeighborsRegressor(n_neighbors=5)

# Entrenar modelo
knn_regressor.fit(X_train, y_train)

# Realizar predicciones 
y_pred = knn_regressor.predict(X_test)

# Calcular la exactitud
accuracy = knn_regressor.score(X_test, y_test)

# Crear un gráfico 
x_min, x_max = X_test[:, 0].min() - 1, X_test[:, 0].max() + 1
y_min, y_max = X_test[:, 1].min() - 1, X_test[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = knn_regressor.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.8, cmap='viridis')
plt.colorbar(label='Predicción de Valoración')
plt.xlabel('wordcount')
plt.ylabel('sentimentValue')
plt.title('Predicción de Valoración vs. Características (Contorno)')
plt.show()

# Mostrar precisión
print(f"Precisión del Modelo: {accuracy}")
