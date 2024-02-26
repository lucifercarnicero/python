import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv('reviews_sentiment.csv', delimiter=';')

# Seleccionar las características y la característica objetivo
X = df[['wordcount', 'sentimentValue']]
y = df['Star Rating']

# Asegurarte de que la característica objetivo esté en el rango de 1 a 5
y = y.clip(1, 5)  # Esto limita las valoraciones a un rango de 1 a 5

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Estandarizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el modelo KNN para regresión
knn_regressor = KNeighborsRegressor(n_neighbors=5)

# Entrenar el modelo con el conjunto de entrenamiento
knn_regressor.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = knn_regressor.predict(X_test)

# Calcular la precisión (exactitud) del modelo
accuracy = knn_regressor.score(X_test, y_test)

# Imprimir la predicción de valoración
print("Predicción de Valoración:")
print(y_pred)

# Imprimir la precisión del modelo
print(f"Precisión del Modelo: {accuracy}")
