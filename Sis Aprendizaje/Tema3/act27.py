import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import datasets

# Cargar el conjunto de datos de cáncer de mama
cancer_data = datasets.load_breast_cancer()
X = cancer_data.data  # Características a estudiar (atributos)
y = cancer_data.target  # Características objetivo (0: benigno, 1: maligno)

# Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir el conjunto de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=1)

# Crear y entrenar el modelo de SVM
svm = SVC(probability=True)
svm.fit(X_train, y_train)

# Obtener las probabilidades estimadas en el conjunto de prueba
y_prob = svm.predict_proba(X_test)

# Las probabilidades para la clase positiva (maligno) están en la segunda columna
probabilidad_maligno = y_prob[:, 1]

# Crear un gráfico de dispersión
plt.scatter(X_test[:, 0], probabilidad_maligno, c=y_test, cmap='coolwarm', edgecolors='k', s=40)
plt.colorbar(label='Etiqueta verdadera')
plt.xlabel('Benigno (Estandarizado)')
plt.ylabel('Probabilidad de ser Maligno')
plt.title('Probabilidad de ser Maligno vs. Benigno (SVM)')
plt.show()
