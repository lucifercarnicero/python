from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

# Cargar el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data[:, [0, 1]]  # Longitud y anchura del sépalo
y = iris.target  # Etiquetas de clase (0, 1, 2)

# Estandarizar las características
X[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

# Dividir el conjunto de datos en entrenamiento y prueba
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, random_state=1)

# Crear y entrenar el modelo de regresión logística
rloc = LogisticRegression()
rloc.fit(X_ent, y_ent)

# Calcular la exactitud en los conjuntos de entrenamiento y prueba
exactitud_entrenamiento = rloc.score(X_ent, y_ent)
exactitud_prueba = rloc.score(X_pru, y_pru)

print('Exactitud en el conjunto de entrenamiento: {:.2f}'.format(exactitud_entrenamiento))
print('Exactitud en el conjunto de pruebas: {:.2f}'.format(exactitud_prueba))

# Graficar la región de decisión
x_min, x_max = X_ent[:, 0].min() - 1, X_ent[:, 0].max() + 1
y_min, y_max = X_ent[:, 1].min() - 1, X_ent[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
Z = rloc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Crear un mapa de colores
colores = ['#FFFFAA', '#AAFFAA', '#AAAAFF']
cmap_light = ListedColormap(colores)

# Graficar la región de decisión
plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

# Graficar los puntos de entrenamiento
plt.scatter(X_ent[:, 0], X_ent[:, 1], c=y_ent, edgecolor='k', s=20)
plt.xlabel('Longitud del Sépalo (estandarizada)')
plt.ylabel('Anchura del Sépalo (estandarizada)')
plt.title('Clasificación de Plantas de Iris (Sépalo)')
plt.show()
