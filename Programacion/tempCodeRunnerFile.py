import random

def generar_palabra():
    diccionario = {"1": "python", "2": "cuerpo", "3": "grano", "4": "plaza", "5": "notas"}
    clave = random.choice(list(diccionario.keys()))
    return diccionario[clave]

def mostrar_palabra_oculta(palabra, letras_acertadas):
    return ''.join(c if c in letras_acertadas else '*' for c in palabra)

def jugar_ahorcado():
    palabra = generar_palabra()
    longitud_palabra = len(palabra)
    palabra_oculta = '*' * longitud_palabra
    letras_acertadas = set()
    
    print("Bienvenido al juego del ahorcado.")
    print(f"La palabra tiene {longitud_palabra} letras.")
    
    intentos = 0
    intentos_maximos = 10
    
    while True:
        print(f"\nPalabra actual: {palabra_oculta}")
        print(f"Intentos restantes: {intentos_maximos - intentos}")
        intento = input("Introduce tu letra: ").lower()
        
        if intento == palabra:
            intentos += 1
            print(f"¡Felicidades! Has adivinado la palabra en {intentos} intentos.")
            break
        elif len(intento) == 1 and intento.isalpha():
            if intento in palabra:
                letras_acertadas.add(intento)
            else:
                intentos += 1
                
            palabra_oculta = mostrar_palabra_oculta(palabra, letras_acertadas)
            
            if palabra_oculta == palabra:
                print(f"¡Felicidades! Has adivinado la palabra en {intentos} intentos.")
                break
        else:
            print("Entrada inválida. Introduce una letra válida.")
        
        if intentos == intentos_maximos:
            print("Lo siento, has perdido. La palabra era:", palabra)
            break

if __name__ == "__main__":
    jugar_ahorcado()