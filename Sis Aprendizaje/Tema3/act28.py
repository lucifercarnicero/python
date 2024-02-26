import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

# Cargar el conjunto de datos de cáncer de mama
cancer_data = load_breast_cancer()
X = cancer_data.data[:, [0, 1]]  # Tomar dos atributos (puedes cambiar estos)
y = cancer_data.target  # Características objetivo (0: benigno, 1: maligno)

# Dividir el conjunto de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Estandarizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear el clasificador KNN y entrenarlo
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)

# Crear un gráfico de dispersión para visualizar la clasificación
plt.figure(figsize=(10, 6))

# Dibujar puntos de entrenamiento
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', edgecolors='k', s=40, label='Entrenamiento')

# Dibujar puntos de prueba
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='coolwarm', marker='x', s=100, label='Prueba')

plt.xlabel('Atributo "Benigno"')
plt.ylabel('Atributo "Maligno"')
plt.title('Clasificación KNN (Benigno vs. Maligno)')
plt.legend(loc='upper right', labels=['Benigno', 'Maligno'])

plt.show()
