# Definimos las funciones de pertenencia para "distancia media recorrida diaria"

# Función de pertenencia para "Poca"
def poca(distancia):
    if distancia <= 15:
        return 1
    elif 15 < distancia < 20:
        return (20 - distancia) / (20 - 15)
    else:
        return 0

# Función de pertenencia para "Media"
def media(distancia):
    if 15 <= distancia <= 20:
        return (distancia - 15) / (20 - 15)
    elif 20 < distancia <= 30:
        return 1
    elif 30 < distancia < 35:
        return (35 - distancia) / (35 - 30)
    else:
        return 0

# Función de pertenencia para "Mucha"
def mucha(distancia):
    if 30 <= distancia <= 35:
        return (distancia - 30) / (35 - 30)
    elif distancia > 35:
        return 1
    else:
        return 0

# Rango de valores para la distancia recorrida diariamente
distancias = np.linspace(0, 50, 500)  # 500 puntos desde 0 hasta 50 km

# Cálculo de las funciones de pertenencia para cada punto en el rango de distancias
y_poca = np.array([poca(d) for d in distancias])
y_media = np.array([media(d) for d in distancias])
y_mucha = np.array([mucha(d) for d in distancias])

# Grados de pertenencia para Persona A (31 km) y Persona B (15 km)
grado_poca_B = poca(15)
grado_media_A = media(31)

# Crear las gráficas de las funciones de pertenencia
plt.figure(figsize=(10, 5))

plt.plot(distancias, y_poca, label="Poca")
plt.plot(distancias, y_media, label="Media")
plt.plot(distancias, y_mucha, label="Mucha")

# Marcar los puntos de Persona A y Persona B
plt.plot(31, grado_media_A, 'ro', label="Persona A (31 km)")
plt.plot(15, grado_poca_B, 'bo', label="Persona B (15 km)")

plt.title("Funciones de Pertenencia para la Distancia Media Recorrida Diaria")
plt.xlabel("Distancia (km)")
plt.ylabel("Grado de Pertenencia")
plt.legend()
plt.grid(True)
plt.show()
