#65. Escribe y ejecuta un programa que lea el archivo creado en el ejercicio anterior y muestre su contenido por pantalla, siguiendo el modelo del comando more de Linux pero con 20 líneas de cada vez, indicando el número de caracteres, de líneas y de palabras -se considera que están separadas por un único espacio en blanco-.

def mostrar_contenido():
    ruta = "64-65/alumnos.txt"  
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
            total_lineas = len(lineas)
            lineas_por_pagina = 20
            pagina_actual = 0

            while pagina_actual < total_lineas:
                print(f"--- Página {pagina_actual // lineas_por_pagina + 1} ---")
                contador_caracteres = 0
                contador_lineas = 0
                contador_palabras = 0

                while (contador_lineas < lineas_por_pagina) and (pagina_actual < total_lineas):
                    linea = lineas[pagina_actual]
                    contador_lineas += 1
                    contador_caracteres += len(linea)
                    contador_palabras += len(linea.split())
                    print(linea, end='')
                    pagina_actual += 1

                print(f"\nNúmero de caracteres: {contador_caracteres}")
                print(f"Número de líneas: {contador_lineas}")
                print(f"Número de palabras: {contador_palabras}\n")
                
                continuar = input("Presiona Enter para continuar o ingresa 'q' para salir: ")
                if continuar.lower() == 'q':
                    break

    except FileNotFoundError:
        print("El archivo 'alumnos.txt' no se encontró.")

mostrar_contenido()
