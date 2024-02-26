import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
dataframe = pd.read_csv(r"usuarios_win_mac_lin.csv")

# Mostrar las primeras filas del conjunto de datos
print(dataframe.head())
# Mostrar estadísticas descriptivas del conjunto de datos
print(dataframe.describe())

# Mostrar la distribución de clases
print(dataframe.groupby('clase').size())

# Eliminar la columna 'clase' (debe hacerse después de la visualización)
dataframe.drop('clase', axis=1, inplace=True)

# Mostrar histogramas para cada característica
dataframe.hist()
plt.show()

# Separar características y variable objetivo
X = np.array(dataframe.drop(['clase'], axis=1))  # Error: 'clase' ya fue eliminada
y = np.array(dataframe['clase'])  # Error: 'clase' ya fue eliminada
print(X.shape)  # Mostrar la forma de X

# Crear y entrenar el modelo de regresión logística
model = linear_model.LogisticRegression()
model.fit(X, y)

# Realizar predicciones con el modelo
predictions = model.predict(X)
print(predictions[:5])  # Corregido para mostrar correctamente las primeras 5 predicciones

# Evaluar el rendimiento del modelo
print(model.score(X, y))

# Dividir los datos en conjuntos de entrenamiento y validación
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, y, test_size=validation_size, random_state=seed)

# Validación cruzada
name = 'Logistic Regression'
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
print(msg)

# Realizar predicciones sobre el conjunto de validación y evaluar
predictions = model.predict(X_validation)
print("Exactitud:", accuracy_score(Y_validation, predictions))
print("Matriz de Confusión:\n", confusion_matrix(Y_validation, predictions))
print("Informe de Clasificación:\n", classification_report(Y_validation, predictions))

# Predecir con nuevos datos
X_new = pd.DataFrame({'duracion': [10], 'paginas': [3], 'acciones': [5], 'valor': [9]})
print("Predicción para nuevos datos:", model.predict(X_new))
