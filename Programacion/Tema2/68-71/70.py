#70. Pedir números positivos por teclado y guardarlos en un fichero binario hasta que introduzcamos un -1.

import pickle

numeros = []
numero = 0
while numero != -1:
    numero = int(input("Introduce un número: "))
    if numero != -1:
        numeros.append(numero)

with open("68-71/70.bin", "wb") as archivo:
    pickle.dump(numeros, archivo)



