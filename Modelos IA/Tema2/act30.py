import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones de pertenencia
def poca(distancia):
    if distancia <= 15:
        return 1
    elif 15 < distancia < 20:
        return (20 - distancia) / (20 - 15)
    else:
        return 0

def media(distancia):
    if 15 <= distancia <= 20:
        return (distancia - 15) / (20 - 15)
    elif 20 < distancia <= 30:
        return 1
    elif 30 < distancia < 35:
        return (35 - distancia) / (35 - 30)
    else:
        return 0

def mucha(distancia):
    if 30 <= distancia <= 35:
        return (distancia - 30) / (35 - 30)
    elif distancia > 35:
        return 1
    else:
        return 0

# Creación del rango de distancias y cálculo de grados de pertenencia
distancias = np.linspace(0, 50, 500)
y_poca = np.array([poca(d) for d in distancias])
y_media = np.array([media(d) for d in distancias])
y_mucha = np.array([mucha(d) for d in distancias])

# Gráficas de las funciones de pertenencia
plt.figure(figsize=(10, 5))
plt.plot(distancias, y_poca, label="Poca")
plt.plot(distancias, y_media, label="Media")
plt.plot(distancias, y_mucha, label="Mucha")

# Marcar los puntos de las personas A y B
plt.plot(31, media(31), 'ro', label="Persona A (31 km)")
plt.plot(15, poca(15), 'bo', label="Persona B (15 km)")

plt.title("Funciones de Pertenencia para la Distancia Media Recorrida Diaria")
plt.xlabel("Distancia (km)")
plt.ylabel("Grado de Pertenencia")
plt.legend()
plt.grid(True)
plt.show()
