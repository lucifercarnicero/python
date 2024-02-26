#72. Escribir una frase y guardarla en un archivo binario y luego recuperarla.

# Solicitar al usuario que ingrese una frase
frase = input("Ingresa una frase: ")

file = "72-73/frase_binaria.bin"

try:
    # Escribir la frase en el archivo binario
    with open(file, "wb") as archivo_binario:
        # Codificar la frase en bytes y escribirla en el archivo
        archivo_binario.write(frase.encode('utf-8'))
    
    print(f"Frase escrita en el archivo {file}")

    # Recuperar la frase desde el archivo binario
    with open(file, "rb") as archivo_binario:
        # Leer los datos del archivo y decodificarlos para obtener la frase
        frase_recuperada = archivo_binario.read().decode('utf-8')

    print("Frase recuperada del archivo:")
    print(frase_recuperada)

except IOError as e:
    print(f"Error al escribir/leer el archivo: {str(e)}")
