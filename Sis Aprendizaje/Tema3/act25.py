from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn import datasets

# Cargar el conjunto de datos de iris
iris = datasets.load_iris()
X = iris.data[:, [0, 1]]  # Longitud y anchura del sépalo
y = iris.target  # Etiquetas de clase (0, 1, 2)

# Crear el modelo de regresión logística
rloc = LogisticRegression()

# Realizar validación cruzada con 5 divisiones (cada bloque será un 20% del conjunto de datos)
scores = cross_val_score(rloc, X, y, cv=5)

# Imprimir la precisión de cada iteración
for i, score in enumerate(scores):
    print(f'Iteración {i + 1}: Precisión = {score:.2f}')

# Calcular la precisión media y desviación estándar
mean_accuracy = scores.mean()
std_accuracy = scores.std()

print(f'Precisión media: {mean_accuracy:.2f}')
print(f'Desviación estándar de la precisión: {std_accuracy:.2f}')
