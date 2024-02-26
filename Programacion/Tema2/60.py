#60. . Escribe la clase Punto que representa un punto de dos dimensiones con componentes x e y enteras.

# Define la clase Punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Crea instancias de la clase Punto
punto1 = Punto(3, 4)
punto2 = Punto(-2, 7)

# Accede a las coordenadas x e y de cada punto
print("Coordenadas del punto 1: ({}, {})".format(punto1.x, punto1.y))
print("Coordenadas del punto 2: ({}, {})".format(punto2.x, punto2.y))

# Realiza algunas operaciones con los puntos
distancia_entre_puntos = ((punto2.x - punto1.x) ** 2 + (punto2.y - punto1.y) ** 2) ** 0.5
print("Distancia entre punto1 y punto2: {:.2f}".format(distancia_entre_puntos))


