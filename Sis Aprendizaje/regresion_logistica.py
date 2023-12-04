from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

dataset = datasets.load_breast_cancer()
X = dataset.data
y = dataset.target
X = X[:, [1, 2]]
y = y[:]
X[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
X[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()

X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, random_state=1)

rloc = LogisticRegression()
rloc.fit(X_ent, y_ent)

print('Exactitud con el conjunto de entrenamiento: {:2f}'.format(rloc.score(X_ent, y_ent)))
print('Exactitud con conjunto de pruebas: {:2f}'.format(rloc.score(X_pru, y_pru)))

colores = ['#FFFFA', '#EFEFEF']
cmap_light = ListedColormap(colores[0:2])
min_x = int(min(X_ent[:, 0]))
max_x = int(max(X_ent[:, 0]))
xx = np.linspace(min_x, max_x, 100)
yy = -(xx * rloc.coef_[0][0] + rloc.intercept_[0]) / rloc.coef_[0][1]

plt.plot(xx, yy, color="black")

for class_value in range(2):
    row_ix = np.where(y == class_value)
    plt.scatter(X[row_ix, 0], X[row_ix, 1])

plt.xlabel("textura media")
plt.ylabel("radio medio")

y_pred = rloc.predict(X_pru)

print(metrics.confusion_matrix(y_true=y_pru, y_pred=y_pred))
print("Exactitud: {:.2f}".format(metrics.accuracy_score(y_true=y_pru, y_pred=y_pred)))
print("Precision: {:.2f}".format(metrics.precision_score(y_true=y_pru, y_pred=y_pred)))
print("Sensibilidad: {:.2f}".format(metrics.recall_score(y_true=y_pru, y_pred=y_pred)))
print(metrics.classification_report(y_true=y_pru, y_pred=y_pred))

plt.show()  # Agregado para mostrar la gráfica
