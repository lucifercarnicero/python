import numpy as np
import matplotlib.pyplot as plt

# Definición de las funciones de pertenencia para "duración de un vuelo"

# Convertimos las horas y minutos a horas decimales para facilitar los cálculos
vuelo_A_horas = 2 + 15/60  # 2 horas y 15 minutos
vuelo_B_horas = 7  # 7 horas

# Función de pertenencia para "Corta"
def corta(duracion):
    if duracion <= 2:
        return 1
    elif 2 < duracion < 3:
        return (3 - duracion) / (3 - 2)
    else:
        return 0

# Función de pertenencia para "Media"
def media(duracion):
    if 2 <= duracion <= 3:
        return (duracion - 2) / (3 - 2)
    elif 3 < duracion <= 6:
        return 1
    elif 6 < duracion < 8:
        return (8 - duracion) / (8 - 6)
    else:
        return 0

# Función de pertenencia para "Larga"
def larga(duracion):
    if 6 <= duracion <= 8:
        return (duracion - 6) / (8 - 6)
    elif duracion >= 8:
        return 1
    else:
        return 0

# Rango de valores para la duración del vuelo
duracion_vuelos = np.linspace(0, 10, 500)

# Cálculo de las funciones de pertenencia para cada punto en el rango de duración de vuelos
y_corta = np.array([corta(d) for d in duracion_vuelos])
y_media = np.array([media(d) for d in duracion_vuelos])
y_larga = np.array([larga(d) for d in duracion_vuelos])

# Grados de pertenencia para el vuelo A y vuelo B
grado_media_vuelo_A = media(vuelo_A_horas)
grado_larga_vuelo_B = larga(vuelo_B_horas)

# La afirmación "el vuelo A es de duración media o el vuelo B es de duración larga"
# se evalúa utilizando la t-conorma, que generalmente es el máximo de los dos grados de pertenencia.
grado_afirmacion = max(grado_media_vuelo_A, grado_larga_vuelo_B)

# Crear las gráficas de las funciones de pertenencia
plt.figure(figsize=(10, 5))

plt.plot(duracion_vuelos, y_corta, label="Corta")
plt.plot(duracion_vuelos, y_media, label="Media")
plt.plot(duracion_vuelos, y_larga, label="Larga")

# Marcar los puntos de vuelo A y vuelo B
plt.plot(vuelo_A_horas, grado_media_vuelo_A, 'ro', label="Vuelo A (2h 15m)")
plt.plot(vuelo_B_horas, grado_larga_vuelo_B, 'bo', label="Vuelo B (7h)")

plt.title("Funciones de Pertenencia para la Duración de un Vuelo")
plt.xlabel("Duración (horas)")
plt.ylabel("Grado de Pertenencia")
plt.legend()
plt.grid(True)
plt.show()
