def longitud_palabras(frase):
    palabras = frase.split()
    return {palabra: len(palabra) for palabra in palabras}

frase = input("Introduce una frase: ")
print(longitud_palabras(frase))