#73. Escribir un texto línea a línea, de modo que cada vez que se pulse Intro se guarde en un fichero binario. El proceso se termina cuando se introduce una línea vacia. Luego se abre el fichero y se muestra por pantalla.

def escribir_lineas():
    with open("72-73/73.bin", "wb") as archivo:
        while True:
            linea = input("Introduce una línea (deja en blanco para terminar): ")
            if not linea:
                break
            archivo.write(linea.encode() + b"\n")

escribir_lineas()

with open("72-73/73.bin", "rb") as archivo:
    print("Líneas escritas en el archivo:")
    for linea in archivo:
        print(linea.decode().rstrip())

