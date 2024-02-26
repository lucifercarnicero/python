#71.Leer un conjunto de números double de un fichero binario y mostrarlos por pantalla.

import random
import struct

# Genera 10 números double aleatorios y guárdalos en una lista
numeros_double = [random.uniform(0.0, 100.0) for _ in range(10)]

nombre_archivo = "68-71/doubles.bin"

try:
    # Escribir números double en un archivo binario
    with open(nombre_archivo, "wb") as archivo_binario:
        for numero in numeros_double:
            dato_binario = struct.pack('d', numero)
            archivo_binario.write(dato_binario)
    
    print(f"Se han escrito {len(numeros_double)} números double en el archivo {nombre_archivo}")
except IOError as e:
    print(f"Error al escribir en el archivo: {str(e)}")

try:
    # Leer números double desde un archivo binario y mostrarlos
    with open(nombre_archivo, "rb") as archivo_binario:
        while True:
            dato_binario = archivo_binario.read(8)
            if not dato_binario:
                break
            numero = struct.unpack('d', dato_binario)[0]
            print(numero)
except IOError as e:
    print(f"Error al leer el archivo: {str(e)}")
except struct.error as se:
    print(f"Error al desempaquetar el dato binario: {str(se)}")
