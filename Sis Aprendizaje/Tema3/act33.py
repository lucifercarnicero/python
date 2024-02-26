from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Cargo los datos
iris = load_iris()
X, y = iris.data, iris.target

# Entrenamiento y prueba
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, test_size=0.2, random_state=1)

# Árbol Depth=3 
arbol_depth_3 = DecisionTreeClassifier(max_depth=3, random_state=10)
arbol_depth_3.fit(X_ent, y_ent)

# Árbol sin para
arbol_default = DecisionTreeClassifier(random_state=10)
arbol_default.fit(X_ent, y_ent)

# Exactitud de los modelos
print("Exactitud del conjunto de entrenamiento (Depth=3): {:.2f}".format(arbol_depth_3.score(X_ent, y_ent)))
print("Exactitud del conjunto de prueba (Depth=3): {:.2f}".format(arbol_depth_3.score(X_pru, y_pru)))
print("Exactitud del conjunto de entrenamiento (Default): {:.2f}".format(arbol_default.score(X_ent, y_ent)))
print("Exactitud del conjunto de prueba (Default): {:.2f}".format(arbol_default.score(X_pru, y_pru)))
