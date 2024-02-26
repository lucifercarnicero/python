#69. Abrir el fichero binario y leer el double y pasarlo por pantalla.

import pickle

with open("68-71/68.bin", "rb") as archivo:
    numero = pickle.load(archivo)
    print(numero)

    