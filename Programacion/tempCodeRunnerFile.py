def leer_lineas():
    lineas = []
    for i in range(10):
        linea = input(f"Introduce la línea {i+1}: ")
        lineas.append(linea)
    return lineas

def ordenar_lineas(lineas):
    return sorted(lineas, key=len)

lineas = leer_lineas()

print("Líneas ordenadas por longitud:")
print(ordenar_lineas(lineas))