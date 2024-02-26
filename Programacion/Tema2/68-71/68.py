#68. Pedir un double por teclado y guardarlo en un fichero binario.

import pickle

numero = float(input("Introduce un número: "))
with open("68-71/68.bin", "wb") as archivo:
    pickle.dump(numero, archivo)

    