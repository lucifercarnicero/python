#66. . Escribe y ejecuta un programa que lea un fichero de texto y añada una línea al final del mismo.

def anadir_linea():
    ruta = "66/fichero.txt"  
    try:
        with open(ruta, "a") as archivo:
            nueva_linea = input("Introduce la línea que deseas añadir al archivo: ")
            archivo.write(nueva_linea + "\n")
    except FileNotFoundError:
        print("El archivo 'fichero.txt' no se encontró.")

anadir_linea()
