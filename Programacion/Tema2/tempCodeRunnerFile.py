#63. Crear la clase Punto3D a partir de la clase Punto del ejercicio 60.
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Punto3D(Punto):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distancia_a_otro_punto(self, otro_punto):
        return ((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2 + (otro_punto.z - self.z) ** 2) ** 0.5

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

# Ejemplo de uso de Punto3D
punto3d1 = Punto3D(1, 2, 3)
punto3d2 = Punto3D(4, 5, 6)

print("Coordenadas del punto3d1:", punto3d1)
print("Coordenadas del punto3d2:", punto3d2)

distancia_entre_puntos_3d = punto3d1.distancia_a_otro_punto(punto3d2)
print("Distancia entre punto3d1 y punto3d2: {:.2f}".format(distancia_entre_puntos_3d))
