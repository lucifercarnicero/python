# Pedir al usuario las palabras y sus traducciones
diccionario = {}
palabras = input("Introduce las palabras y sus traducciones en formato palabra:traducción separadas por comas: ")

# Dividir la cadena en una lista de palabras
for palabra in palabras.split(","):
    # Dividir cada palabra en una lista de dos elementos
    clave, valor = palabra.split(":")
    # Agregar clave y valor al diccionario
    diccionario[clave] = valor

# Pedir una frase para traducir
frase = input("Introduce una frase en español: ")

# Traducir la frase palabra a palabra
for palabra in frase.split():
    if palabra in diccionario:
        print(diccionario[palabra], end=" ")
    else:
        print(palabra, end=" ")