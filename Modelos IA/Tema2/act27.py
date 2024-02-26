import numpy as np

# Definición de las funciones de membresía
def trapezoidal(x, a, b, c, d):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return 1
    elif c <= x <= d:
        return (d - x) / (d - c)
    return 0

def triangular(x, a, b, c):
    return max(min((x - a) / (b - a), (c - x) / (c - b)), 0)

# Funciones de membresía para "frío" y "fresco" (ya definidas anteriormente)
def membresia_frio(x):
    # Tu definición aquí
    pass

def membresia_fresco(x):
    # Tu definición aquí
    pass

# Entrada de ejemplo
temperatura_entrada = 16  # Grados Celsius
iluminacion_entrada = 50  # klux

# Fusificación
grado_frio = membresia_frio(temperatura_entrada)
grado_fresco = membresia_fresco(temperatura_entrada)
grado_buen_tiempo = trapezoidal(temperatura_entrada, 15, 17, 20, 25)
grado_calor = trapezoidal(temperatura_entrada, 20, 25, 35, 35)
grado_sombra = triangular(iluminacion_entrada, 0, 20, 25)
grado_media = trapezoidal(iluminacion_entrada, 20, 30, 65, 85)
grado_fuerte = trapezoidal(iluminacion_entrada, 60, 85, 100, 100)

# Aplicación de una regla de inferencia simple
def aplicar_reglas(grado_fresco, grado_media):
    # Regla de ejemplo: Si temperatura es fresco Y iluminación es media, entonces persiana a media altura.
    return min(grado_fresco, grado_media)

grado_media_altura = aplicar_reglas(grado_fresco, grado_media)

# Defusificación con método del centroide (simplificado para este ejemplo)
def centroide(grado, a, b, c, d):
    return (grado * (a + b + c + d)) / 4

# Suponiendo que 'media altura' de la persiana es representada por una función trapezoidal con puntos 25, 40, 85, 100
altura_persiana = centroide(grado_media_altura, 25, 40, 85, 100)

# Imprime el resultado final
print("Altura de la persiana después de defusificar:", altura_persiana)
