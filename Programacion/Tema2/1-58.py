#1. Escribir y ejecutar un programa que imprima el nombre, edad y dirección del alumno 

print('Lucía')
print('37')
print('Oviedo')

#2. Escribir y ejecutar un programa que imprima el número 1 en asteriscos.

numero = input('Introduce un número: ')
print('*' * int(numero))

#3. Escribir y ejecutar un programa que nos devuelva el espacio recorrido en t= 2 s, por un vehículo con velocidad inicial 5 m/s, aceleración 2 m/s2 y espacio inicial recorrido 5 m.

vi= 5
ac = 2
si = 5
temp=2
sf = si + vi*temp + 1/2*ac*temp**2
print('El espacio recorrido es: ', sf)

#4. Construir un programa que nos devuelve la longitud de la circunferencia, el área de esta y la superficie y volumen de una esfera introduciendo por teclado el radio. (π=3.14159)

radio = input('Introduce el radio: ')
pi = 3.14159
longitud = 2*pi*int(radio)
area = pi*int(radio)**2
superficie = 4*pi*int(radio)**2
volumen = 4/3*pi*int(radio)**3
print('La longitud de la circunferencia es: ', longitud)
print('El área de la circunferencia es: ', area)
print('La superficie de la esfera es: ', superficie)
print('El volumen de la esfera es: ', volumen)


#5. Emplear la fórmula de la gravitación universal. Para obtener el valor de F. Se introducirán por teclado las masas m1 y m2, y la distancia entre ellas.

m1 = input('Introduce la masa 1: ')
m2 = input('Introduce la masa 2: ')
d = input('Introduce la distancia: ')
G = 6.673*(10**-11)
F = G*int(m1)*int(m2)/int(d)**2
print('La fuerza de atracción es: ', F)

#6. Construir un programa que indique si un número introducido por teclado es positivo, negativo o cero.

numero = input('Introduce un número: ')
if int(numero) > 0:
    print('El número es positivo')
elif int(numero) < 0:
    print('El número es negativo')
else:
    print('El número es cero')

#7. Escribir y ejecutar un programa que resuelva una ecuación de 2º grado introduciendo por teclado las constantes a, b y c.

a = input('Introduce el valor de a: ')
b = input('Introduce el valor de b: ')
c = input('Introduce el valor de c: ')

if int(a) == 0:
    print('La ecuación no es de segundo grado')
else:
    print('La ecuación es de segundo grado')
    discriminante = int(b)**2 - 4*int(a)*int(c)
    if discriminante < 0:
        print('La ecuación no tiene solución real')
    elif discriminante == 0:
        x = -int(b)/(2*int(a))
        print('La solución es: ', x)
    else:
        x1 = (-int(b) + discriminante**0.5)/(2*int(a))
        x2 = (-int(b) - discriminante**0.5)/(2*int(a))
        print('Las soluciones son: ', x1, ' y ', x2)


#8. Escribir un bucle while que dado un número introducido por teclado calcula la suma de todos los enteros desde 1 hasta este número.

numero = input('Introduce un número: ')
suma = 0
i = 1
while i <= int(numero):
    suma = suma + i
    i = i + 1
print('La suma es: ', suma)

#9. Calcule la suma de la serie 1/1 + 1/2 + 1/3 + ... + 1/N, donde el número N se introducirá por teclado.

numero = input('Introduce un número: ')
suma = 0
i = 1
while i <= int(numero):
    suma = suma + 1/i
    i = i + 1
print('La suma es: ', suma)


#10. Escribir un programa que introduzca N números reales desde teclado, los sume y calcule la media, mostrándola por pantalla.

numero = input('Introduce un número: ')
suma = 0
i = 1
while i <= int(numero):
    suma = suma + i
    i = i + 1
print('La suma es: ', suma)
print('La media es: ', suma/int(numero))


#11. Escribe un programa que calcule la letra del DNI introducido por teclado sabiendo que tenemos 23 letras en el becedario y que existe una correspondencia entre letras y números tal que así: 0 = T, 1=R, etc

dni = input('Introduce el DNI: ')
letras = 'TRWAGMYFPDXBNJZSQVHLCKE'

print('La letra del DNI es: ', letras[int(dni)%23])

#12. Escribir un programa que realice un juego que consiste en acertar un número desconocido generado aleatoriamente entre uno y cien. Para ello se leerán de teclado números, y se compararán con el número secreto, indicando si son mayores o menores que este, hasta acertar.

import random
secreto = random.randint(1, 100)
numero = int(input('Introduce un número: '))
while numero != secreto:
    if numero > secreto:
        print('El número secreto es menor')
    else:
        print('El número secreto es mayor')
    numero = int(input('Introduce un número: '))    
print('Has acertado')

#13. Escribir un programa que introduzca las edades de una serie de alumnos, y que se detendrá al introducir un numero negativo. Se calculará la media, la suma y el número de alumnos con más de 18 años.

edad = int(input('Introduce la edad: '))
suma = 0
contador = 0
mayores = 0
while edad >= 0:
    suma = suma + edad
    contador = contador + 1
    if edad > 18:
        mayores = mayores + 1
    edad = int(input('Introduce la edad: '))

print('La media es: ', suma/contador)
print('El número de alumnos mayores de 18 es: ', mayores)

#14. Escribe un programa que pida al usuario una cantidad de euros, una tasa de interés y un número de años. Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida. Recordar que un capital C euros a un interés r durante n años nos da un rendimiento de rendimiento= C x r x t /100.

C= input('Introduce el capital: ')
r= input('Introduce el interés: ')
t= input('Introduce el número de años: ')

rendimiento = int(C)*float(r)*int(t)/100
print('El rendimiento es: ', rendimiento)

#15. Escribir un programa que calcule el producto de los 50 primeros números impares.

producto = 1
i = 1
while i <= 50:
    producto = producto * i
    i = i + 2

print('El producto es: ', producto)


#16. Implementar la tabla de multiplicar de un número del 1 al 10 introducido por teclado. El programa comprobará si el numero introducido está dentro de ese rango

numero = int(input('Introduce un número: '))
if numero >= 1 and numero <= 10:
    i = 1
    while i <= 10:
        print(numero, ' x ', i, ' = ', numero*i)
        i = i + 1
else:
    print('El número introducido no está en el rango')

#17. Pedir un número por teclado y dibujar un triángulo rectángulo con asteriscos

numero = int(input('Introduce un número: '))
i = 1
while i <= numero:
    print('*'*i)
    i = i + 1

#18. Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

palabras = []
numero = int(input('Introduce el número de palabras: '))
i = 0
while i < numero:
    if i == numero - 1:
        palabra = input('Última palabra: ')
    else:
        palabra = input(str(i+1) + 'º palabra: ')
    palabras.append(palabra)
    i = i + 1
print(palabras)

#19. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa palabra de la lista.

palabras = []
palabra = input('Introduce una palabra (en blanco cuando termines): ')
while palabra != '':
    palabras.append(palabra)
    palabra = input('Introduce otra palabra (en blanco cuando termines): ')
print('La lista creada es: ', palabras)
palabra = input('Introduce la palabra a eliminar: ')
while palabra in palabras:
    palabras.remove(palabra)
print('La lista es ahora: ', palabras)



#Recursividad en potencia hasta que el número sea 1. Con try catch. (creo que este es el ejemplo pero como no se escucha la mitad pues gg)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
try:
    base = int(input('Introduce la base: '))
    exponente = int(input('Introduce el exponente: '))
    print('El resultado es: ', potencia(base, exponente))
except:
    print('Error en los datos introducidos')



#20. Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

palabras = []
palabra = input('Introduce una palabra (en blanco cuando termines): ')
while palabra != '':
    palabras.append(palabra)
    palabra = input('Introduce otra palabra (en blanco cuando termines): ')
print('La lista creada es: ', palabras)
palabra = input('Introduce la palabra a buscar: ')
contador = 0
for i in palabras:
    if i == palabra:
        contador = contador + 1
print('La palabra ', palabra, ' aparece ', contador, ' veces')


#21. Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones): 
# a) Lista de palabras que aparecen en las dos listas. b) Lista de palabras que aparecen en la primera lista, pero no en la segunda. 
# c) Lista de palabras que aparecen en la segunda lista, pero no en la primera.

palabras = ["pato","gallina","pollo","ornitorrinco"]
palabras2 = ["perro","gato","nutria","ornitorrinco"]

for element in palabras:
  if element in palabras2:
    print(f"el elemento {element} está repetido!")
    break

#resta los arrays y saca lo que no se repite (parece easy)
def solo_en_palabras(lista1, lista2):
    return list(set(lista1) - set(lista2))

def solo_en_palabras2(lista1, lista2):
    return list(set(lista2) - set(lista1))

solo_palabras = solo_en_palabras(palabras, palabras2)
solo_palabras2 = solo_en_palabras2(palabras, palabras2)


print("Palabras en lista de AVES:", solo_palabras)
print("Palabras en lista animales CUQUIS:", solo_palabras2)

#22. Escribir un programa que almacene los módulos de un ciclo -por ejemplo Programación, Lenguajes de Marcas, Bases de Datos- en una lista y la muestre por pantalla

modulos = ["Programacion","Lenguaje de Marcas", "BBDD", "Whatever"]
for i in modulos:
    print(i)


#23. Escribir un programa que almacene los módulos de un ciclo en una lista y la muestre por pantalla el mensaje Yo estudio <modulo>, donde <modulo> es cada una de los módulos de la lista.

modulos = ["Cliente","Servidor","Interfaces"]

for i in modulos:
    print("Yo estudio ",i)

#24. Escribir un programa que almacene los módulos de un ciclo en una lista, pregunte al usuario la nota que ha sacado en cada módulo, y después las muestre por pantalla con el mensaje En <módulo> has sacado <nota>, donde <módulo> es cada uno de los módulos de la lista y <nota> la calificación introducida por teclado.

modulos = ["Cliente","Servidor","Interfaces"]
modulos_con_nota = []

for i in modulos:
    nota = input (f"Introduce la nota para {i}: ")
    modulos_con_nota.append((i,nota))

for modulo, nota in modulos_con_nota:
    print(f"En {modulo} has sacado {nota}")


#25. Escribe una función llamada "elimina" que tome una lista y elimine el primer y último elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.

def elimina(lista):
    # Verificar que la lista tiene al menos dos elementos
    if len(lista) >= 2:
        # Eliminar el primer y último elemento
        lista_resultante = lista[1:-1]
        return lista_resultante
    else:
        print("La lista debe tener al menos dos elementos.")

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
nueva_lista = elimina(mi_lista)

print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)


#26. Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva lista que contenga todos los elementos de la lista anterior menos el primero y el último.

def media(lista):
    # Verificar que la lista tiene al menos dos elementos
    if len(lista) >= 2:
        # Eliminar el primer y último elemento
        lista_resultante = lista[1:-1]
        return lista_resultante
    else:
        print("La lista debe tener al menos dos elementos.")

# Ejemplo de uso
mi_lista = [1, 2, 3, 4, 5]
nueva_lista = media(mi_lista)

print("Lista original:", mi_lista)
print("Nueva lista:", nueva_lista)


#27. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

numeros = [1,2,3,4,5,6,7,8,9,10]

numeros.sort(reverse=True)

for x in numeros:
    print(x, end=",")
print("\b");


#28. . Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


print(sum([1,2,3,4])) #función sum ya existe en python

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def multiplicar_lista(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto


lista = [1, 2, 3, 4]
resultado_suma = sumar_lista(lista)
resultado_multiplicacion = multiplicar_lista(lista)

print(resultado_suma)
print(resultado_multiplicacion)

#29. Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen impares, y muestre por pantalla la lista resultante.

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

nueva_lista = [letra for indice, letra in enumerate(abc) if indice % 2 != 0]

print(nueva_lista)


#30. Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal y cada consonante.

# Pedir al usuario una palabra
palabra = input("Ingrese una palabra: ")

# Inicializar contadores para vocales y consonantes
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonantes = {}

# Recorrer cada letra en la palabra
for letra in palabra:
    # Convertir la letra a minúsculas para evitar distinción entre mayúsculas y minúsculas
    letra_minuscula = letra.lower()

    # Verificar si la letra es una vocal
    if letra_minuscula in vocales:
        vocales[letra_minuscula] += 1
    # Verificar si la letra es una consonante
    elif letra_minuscula.isalpha():
        if letra_minuscula not in consonantes:
            consonantes[letra_minuscula] = 1
        else:
            consonantes[letra_minuscula] += 1

# Mostrar los resultados
print("Número de veces que contiene cada vocal:")
for vocal, conteo in vocales.items():
    print(f"{vocal}: {conteo}")

print("Consonantes y su frecuencia:")
for consonante, conteo in consonantes.items():
    print(f"{consonante}: {conteo}")

#31. Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

animales_cuquis = ["nutria","gato","ewok"]
animales_asesinos = ["gato","hipopotamo","koala"]

def superposicion(lista1,lista2):
    for y in lista1:
        for x in lista2:
            if y == x:
                return True
    return False



comparando = superposicion(animales_cuquis,animales_asesinos)

print(comparando)

#32. Escribir un programa que pregunte al usuario su nombre, edad, departamento y salario y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, trabaja en el departamento <departamento> y su salario es <salario>.

nombre = input("Nombre ")
edad = input ("Edad ")
departamento = input ("Departamento ")
salario = input ("Salario ")

empleado = {"nombre":nombre,"edad":edad,"departamento":departamento, "salario":salario}
print(empleado)
print(f"{empleado['nombre']} tiene {empleado['edad']} años, trabaja en el departamento {empleado['departamento']} y su salario es {empleado['salario']}.")

#33. . Escribir un programa que almacene el diccionario con los créditos de los módulos de un ciclo {'Programación': 9, 'Lenguajes de marcas': 4, 'Bases de datos': 5} y después muestre por pantalla los créditos de cada módulo en el formato <módulo> tiene <créditos> créditos, Al final debe mostrar también el número total de créditos del módulo.

    # Definir el diccionario con los créditos de los módulos
creditos_modulos = {'Programación': 9, 'Lenguajes de marcas': 4, 'Bases de datos': 5}

# Mostrar los créditos de cada módulo en el formato solicitado
for modulo, creditos in creditos_modulos.items():
    print(f"{modulo} tiene {creditos} créditos")

# Calcular y mostrar el número total de créditos
total_creditos = sum(creditos_modulos.values())
print(f"\nEl número total de créditos del ciclo es: {total_creditos}")

# 34. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español y francés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# Pedir al usuario las palabras y sus traducciones
diccionario = {}
palabras = input("Introduce las palabras y sus traducciones en formato palabra:traducción separadas por comas: ")

# Dividir la cadena en una lista de palabras y agregarlas al diccionario
for palabra in palabras.split(","):
    clave, valor = palabra.split(":")
    diccionario[clave.lower()] = valor.lower()

# Imprimir el diccionario para depuración
print("Diccionario:", diccionario)

# Pedir una frase para traducir
frase = input("Introduce una frase en español: ")

# Traducir la frase palabra a palabra
traduccion = []
for palabra in frase.lower().split():
    traducida = diccionario.get(palabra, palabra)
    print(f"Traduciendo '{palabra}': '{traducida}'")  # Impresión de depuración
    traduccion.append(traducida)

print("Frase traducida:", " ".join(traduccion))



        
#35. Escribir un programa que gestione las facturas de una familia. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el tipo de factura -agua, gas,…- y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el tipo de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el tipo de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


facturas = {}
cantidad_cobrada = 0
cantidad_pendiente = 0

while True:
    accion = input("¿Desea añadir una nueva factura (a), pagar una existente (p) o terminar (t)? ")

    if accion == "a":
        tipo = input("Introduce el tipo de factura: ")
        coste = float(input("Introduce el coste de la factura: "))
        facturas[tipo] = coste
        cantidad_pendiente += coste
    elif accion == "p":
        if not facturas:
            print("No hay facturas para pagar.")
            continue

        print("Facturas existentes:")
        print(facturas)

        tipo = input("Introduce el tipo de factura a pagar: ")
        if tipo in facturas:
            costo_pagado = facturas[tipo]
            cantidad_cobrada += costo_pagado
            cantidad_pendiente -= costo_pagado
            del facturas[tipo]  # Eliminar la factura pagada después de restar el costo
        else:
            print("La factura no existe")
            continue
    elif accion == "t":
        break
    else:
        print("La acción no es correcta")

    print(f"Recaudado hasta el momento: {cantidad_cobrada}")
    print(f"Pendiente de cobro: {cantidad_pendiente}")

#36. Escribe un programa que implemente una función una función que dependiendo de los parámetros que reciba: convierte a segundos o a horas:
    # a) Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos.
    # b) Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.
    # Nota: emplear el concepto de los parámetros *args en funciones de Python

def convertir(*args):
    if len(args) == 1:
        segundos = args[0]
        horas = segundos // 3600
        segundos %= 3600
        minutos = segundos // 60
        segundos %= 60
        return horas, minutos, segundos
    elif len(args) == 3:
        horas, minutos, segundos = args
        return horas * 3600 + minutos * 60 + segundos
    else:
        print("La función necesita 1 o 3 argumentos")

    # Ejemplo de uso
print(convertir(3600))
print(convertir(1, 0, 0))

#37. Diseñar una función que calcule el n-ésimo término de la serie de Fibonacci. Investiga en la red la expresión matemática de dicha serie.

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(25))

#38. Diseñar una función que calcule la distancia euclídea entre dos puntos introducidos por teclado, de la forma (x1,y1) e (x2,y2).

import math 

def distancia_euclidea(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(distancia_euclidea(1,2,3,4))


#39. Escribir un programa que introduciendo las coordenadas x e y de un punto en el espacio de dos dimensiones, calcule las coordenadas polares. Debe crearse un método que realice esta transformación. Las ecuaciones de la transformación son: 𝑥 = 𝑟 × cos 𝜃   𝑦 = 𝑟 × sin 𝜃

import math

def coordenadas_polares(x,y):
    r = math.sqrt(x**2+y**2)
    theta = math.atan2(y,x)
    return r, theta

print(coordenadas_polares(1,1))

#40. Resuelve el ejercicio 7 empleando un método que lleve como parámetros los coeficientes de la ecuación de segundo grado.  (#7. Escribir y ejecutar un programa que resuelva una ecuación de 2º grado introduciendo por teclado las constantes a, b y c.)

import math

def ecuacion_segundo_grado(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print('La ecuación no tiene solución real')
    elif discriminante == 0:
        x = -b/(2*a)
        print('La solución es: ', x)
    else:
        x1 = (-b + discriminante**0.5)/(2*a)
        x2 = (-b - discriminante**0.5)/(2*a)
        print('Las soluciones son: ', x1, ' y ', x2)

ecuacion_segundo_grado(1,2,1)

#41. Escribe un método que introduzca 10 números enteros en una lista y que luego los invierta, colocando el primero en la décima posición, el segundo en la novena posición, etc…

lista = []
numeros = input("Introduce 10 números separados por coma: ")
for numero in numeros.split(","):
    lista.append(int(numero))

lista_invertida = []
for numero in lista:
    lista_invertida.insert(0, numero)

print("Lista original:", lista)
print("Lista invertida:", lista_invertida)

#42. Escriba un programa que obtenga los 20 primeros números primos, los introduzca en una lista, y muestre esa lista por pantalla.

primos = []
numero = 2

while len(primos) < 20:
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(numero)
    numero += 1

print(primos)

#43. Desarrolle un juego en el que se tenga que adivinar una combinación secreta formada por n números del 1 al 5, donde n se introducirá por teclado. Se generará una combinación aleatoria de n elementos que el usuario tendrá que acertar. En cada intento se muestra si el digito que introduce el jugador es mayor, menor o igual que el que corresponde en la combinación secreta.

import random

def generar_combinacion_secreta(n):
    return [random.randint(1, 5) for _ in range(n)]

def jugar_juego():
    intentos = 0

    while True:
        n = int(input("Introduce la longitud de la combinación secreta (número de elementos): "))
        combinacion_secreta = generar_combinacion_secreta(n)

        print("Combinación secreta generada. ¡Adivina la combinación!")

        while True:
            intento = input("Introduce tu combinación (separada por espacios): ")
            intento_lista = [int(num) for num in intento.split()]

            if len(intento_lista) != n:
                print(f"Debes introducir exactamente {n} números. Intenta de nuevo.")
                continue

            intentos += 1

            if intento_lista == combinacion_secreta:
                print(f"¡Felicidades! Adivinaste la combinación en {intentos} intentos.")
                break
            else:
                comparacion = [">" if a > b else "<" if a < b else "=" for a, b in zip(intento_lista, combinacion_secreta)]
                print(f"Respuesta: {comparacion}. Intenta de nuevo.")

jugar_juego()


#44. Diseñar un programa que determine la media de las calificaciones en cada asignatura de primero de bachillerato para 10 alumnos. Emplear listas para resolver el ejercicio.

# Definir las asignaturas
asignaturas = ["Lengua", "Historia", "Filosofía"]

# Pedir al usuario las calificaciones de los 10 alumnos
calificaciones = []
for i in range(10):
    calificaciones_alumno = []
    for asignatura in asignaturas:
        calificacion = float(input(f"Introduce la calificación de {asignatura} del alumno {i+1}: "))
        calificaciones_alumno.append(calificacion)
    calificaciones.append(calificaciones_alumno)

# Calcular la media de cada alumno
medias = [sum(calificaciones_alumno) / len(calificaciones_alumno) for calificaciones_alumno in calificaciones]

# Calcular la media de cada asignatura
medias_asignaturas = [sum(calificaciones[j][i] for j in range(10)) / 10 for i in range(len(asignaturas))]

# Mostrar los resultados
print("Las medias de cada alumno son:")
for i, media in enumerate(medias):
    print(f"Alumno {i+1}: {media}")

print("Las medias de cada asignatura son:")
for i, media_asignatura in enumerate(medias_asignaturas):
    print(f"{asignaturas[i]}: {media_asignatura}")

#45. Escribir un programa que incluya un método que lea 10 líneas, cada una de ellas de un máximo de 50 caracteres y ordénalas por número de caracteres en una lista

def leer_lineas():
    lineas = []
    for i in range(10):
        linea = input(f"Introduce la línea {i+1}: ")
        lineas.append(linea)
    return lineas

def ordenar_lineas(lineas):
    return sorted(lineas, key=len)

lineas = leer_lineas()

print("Líneas ordenadas por longitud:")
print(ordenar_lineas(lineas))

#46. Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def longitud_palabras(frase):
    palabras = frase.split()
    return {palabra: len(palabra) for palabra in palabras}

frase = input("Introduce una frase: ")
print(longitud_palabras(frase))

#47. Escribir una función reciba un diccionario con los módulos y las notas de un alumno y devuelva otro diccionario con los módulos en mayúsculas y las calificaciones correspondientes a las notas.

def calificaciones_mayusculas(calificaciones):
    print("Diccionario original:")
    print(calificaciones)
    
    calificaciones_mayus = {modulo.upper(): calificacion for modulo, calificacion in calificaciones.items()}
    
    print("\nDiccionario con módulos en mayúsculas:")
    print(calificaciones_mayus)
    
    return calificaciones_mayus

calificaciones = {"Programación": 9, "Lenguajes de marcas": 4, "Bases de datos": 5}
calificaciones_mayusculas(calificaciones)

#48. Escribe un programa que incluya un método que lleve como parámetro un string introducido por teclado y que busque en él las vocales y nos indique la posición en la que están.

def buscar_vocales(frase):
    vocales = "aeiou"
    vocales_encontradas = []
    for i, letra in enumerate(frase):
        if letra in vocales:
            vocales_encontradas.append((i, letra))
    return vocales_encontradas

frase = input("Introduce una frase: ")
print(buscar_vocales(frase))

#49. . Emplea el método de ordenación por inserción para ordenar:  23,15, 6, 2, 34,1 ,4 ,8

def ordenar_insercion(lista):
    for i in range(1, len(lista)):
        valor_actual = lista[i]
        posicion_actual = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

lista = [23, 15, 6, 2, 34, 1, 4, 8]
ordenar_insercion(lista)
print(lista)

#50. Escribe un programa que incluya un método que lea una frase de teclado e indique si es palíndroma, esto es, que se lee igual de derecha a izquierda que de izquierda a derecha sin tener en cuenta los espacios ni las tildes.

def es_palindroma(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

frase = input("Introduce una frase: ")
if es_palindroma(frase):
    print("La frase es palíndroma")
else:
    print("La frase no es palíndroma")


#51. Diseñar un programa que lea una frase de teclado y la muestre en mayúsculas.

frase = input("Introduce una frase: ")
print(frase.upper())

#52. . Diseñar un programa que lea una frase por teclado e indique cuantos espacios en blanco tiene.

frase = input("Introduce una frase: ")
print(frase.count(" "))

#53. Diseñar el juego “la contraseña” en el cual el jugador tiene que introducir palabras por teclado hasta que acierte la contraseña. Como pista el programa le indicara en cada intento cuantas letras ha acertado y en que posición están.

import random

def generar_contraseña():
    palabras = ["python", "cuerpo", "grano", "plaza", "notas"]
    return random.choice(palabras)

def mostrar_contraseña_oculta(contraseña, letras_acertadas):
    return ''.join(c if c in letras_acertadas else '*' for c in contraseña)

def jugar_contraseña():
    contraseña = generar_contraseña()
    longitud_contraseña = len(contraseña)
    contraseña_oculta = '*' * longitud_contraseña
    letras_acertadas = set()
    
    print("Bienvenido al juego de la contraseña.")
    print(f"La contraseña tiene {longitud_contraseña} letras.")
    
    intentos = 0
    
    while True:
        print(f"\nContraseña actual: {contraseña_oculta}")
        intento = input("Introduce tu palabra: ").lower()
        
        if intento == contraseña:
            intentos += 1
            print(f"¡Felicidades! Has adivinado la contraseña en {intentos} intentos.")
            break
        else:
            coincidencias = sum(c1 == c2 for c1 in intento for c2 in contraseña)
            letras_acertadas.update(c1 for c1 in intento if c1 in contraseña)
            
            contraseña_oculta = mostrar_contraseña_oculta(contraseña, letras_acertadas)
            
            print(f"Letras acertadas: {coincidencias}")
            print(f"Nueva contraseña: {contraseña_oculta}")
            
            intentos += 1

if __name__ == "__main__":
    jugar_contraseña()

#54. Introducir por teclado dos palabras e indicar cual es la que tiene menos caracteres.

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

if len(palabra1) < len(palabra2):
    print(f"{palabra1} tiene menos caracteres que {palabra2}")
elif len(palabra1) > len(palabra2):
    print(f"{palabra2} tiene menos caracteres que {palabra1}")
else:
    print("Ambas palabras tienen el mismo número de caracteres")

#55. Diseñar un programa que lea una frase de teclado e indique cuantas veces aparece cada letra del abecedario en ella.


frase = input("Introduce una frase: ")
letras = "abcdefghijklmnopqrstuvwxyz"

for letra in letras:
    repeticiones = frase.count(letra)
    if repeticiones > 0:
        print(f"La letra {letra} aparece {repeticiones} veces")

#56. Realice un programa que implemente el juego del ahorcado.

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

# 57. Diseñar la clase CuentaCorriente, sabiendo que los datos necesarios son: saldo, DNI, nombre y descubierto -que será por defecto de 50 euros-. Las operaciones típicas con una cuenta corriente son:
# a. Sacar dinero: se necesita el DNI y nombre del titular 
# b. Crear la cuenta:
#c. Ingresar dinero, incrementando el saldo
#d. Mostrar la información de la cuenta.
# Se pide crear al menos tres cuentas en el main de una clase principal, con un menú de opciones que permita navegar entre las diferentes operaciones. Asimismo habrá otro menú que permite elegir la cuenta corriente sobre la que se va a realizar esas operaciones. Los atributos serán siempre privados por lo que deben crearse los getters y setters.

class CuentaCorriente:

    def __init__(self, saldo, dni, nombre, descubierto=50):
        self.saldo = saldo
        self.dni = dni
        self.nombre = nombre
        self.descubierto = descubierto

    def sacar_dinero(self, dni, nombre, cantidad):
        if dni == self.dni and nombre == self.nombre:
            if self.saldo - cantidad >= -self.descubierto:
                self.saldo -= cantidad
                print(f"Has sacado {cantidad} euros. Saldo actual: {self.saldo}")
            else:
                print("No tienes suficiente saldo para sacar esa cantidad")
        else:
            print("Los datos introducidos no son correctos")

    def ingresar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Has ingresado {cantidad} euros. Saldo actual: {self.saldo}")

    def mostrar_informacion(self):
        print(f"Saldo: {self.saldo}")
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nombre}")
        print(f"Descubierto: {self.descubierto}")

if __name__ == "__main__":

    cuenta1 = CuentaCorriente(1000, "12345678A", "Pepe")
    cuenta2 = CuentaCorriente(500, "87654321B", "Juan")
    cuenta3 = CuentaCorriente(1500, "11111111C", "Ana")

    cuentas = [cuenta1, cuenta2, cuenta3]

    while True:
        print("\nMenú principal")
        print("1. Seleccionar cuenta")
        print("2. Salir")
        opcion = input("Introduce una opción: ")

        if opcion == "1":
            print("\nSeleccionar cuenta")
            print("1. Cuenta 1")
            print("2. Cuenta 2")
            print("3. Cuenta 3")
            opcion = input("Introduce una opción: ")

            if opcion == "1":
                cuenta = cuenta1
            elif opcion == "2":
                cuenta = cuenta2
            elif opcion == "3":
                cuenta = cuenta3
            else:
                print("Opción inválida")
                continue

            while True:
                print("\nMenú de operaciones")
                print("1. Sacar dinero")
                print("2. Ingresar dinero")
                print("3. Mostrar información")
                print("4. Cambiar de cuenta")
                print("5. Salir")
                opcion = input("Introduce una opción: ")

                if opcion == "1":
                    dni = input("Introduce tu DNI: ")
                    nombre = input("Introduce tu nombre: ")
                    cantidad = float(input("Introduce la cantidad a sacar: "))
                    cuenta.sacar_dinero(dni, nombre, cantidad)
                elif opcion == "2":
                    cantidad = float(input("Introduce la cantidad a ingresar: "))
                    cuenta.ingresar_dinero(cantidad)
                elif opcion == "3":
                    cuenta.mostrar_informacion()
                elif opcion == "4":
                    break
                elif opcion == "5":
                    exit()
                else:
                    print("Opción inválida")
        elif opcion == "2":
            exit()
        else:
            print("Opción inválida")


#58. Crear los paquetes y clases necesarios para gestionar una empresa ferroviaria en la que se distinguen dos grandes grupos de clases, Personal y Maquinaria. En la primera se ubican todos los empleados de la empresa y en la segunda todos los vehículos.
# Tenemos los siguientes actores:
# a. Maquinistas: nombre, DNI, salario y rango
# b. Mecánicos: nombre, tfno, DNI,especialidad
# c. Jefes de estación: nombre y DNI
# d. Vagones: matrícula, capacidad máxima en kg, capacidad actual en kg, y tipo de mercancía
# e. Locomotoras: matricula, potencia del motor, antigüedad y mecánico asignado
# f. Trenes: locomotora y varios vagones, hasta cinco. Un maquinista asignado.
# Se pide crear además la Clase principal con un main donde se crearán dos trenes con todos los elementos indicados.

#Supongo que hay dos clases Empleado y Maquina de cual heredan las clases Maquinista, Mecanico, JefeEstacion, Vagon, Locomotora y Tren

class Empleado:

    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Maquinista(Empleado):
    
        def __init__(self, nombre, dni, salario, rango):
            super().__init__(nombre, dni)
            self.salario = salario
            self.rango = rango

class Mecanico(Empleado):

    def __init__(self, nombre, dni, telefono, especialidad):
        super().__init__(nombre, dni)
        self.telefono = telefono
        self.especialidad = especialidad

class JefeEstacion(Empleado):

    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)

class Maquina:
    
        def __init__(self, matricula):
            self.matricula = matricula

class Vagon(Maquina):

    def __init__(self, matricula, capacidad_maxima, capacidad_actual, tipo_mercancia):
        super().__init__(matricula)
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_actual = capacidad_actual
        self.tipo_mercancia = tipo_mercancia

class Locomotora(Maquina):

    def __init__(self, matricula, potencia_motor, antiguedad, mecanico_asignado):
        super().__init__(matricula)
        self.potencia_motor = potencia_motor
        self.antiguedad = antiguedad
        self.mecanico_asignado = mecanico_asignado

class Tren:

    def __init__(self, locomotora, vagones, maquinista_asignado):
        self.locomotora = locomotora
        self.vagones = vagones
        self.maquinista_asignado = maquinista_asignado

if __name__ == "__main__":
    # Crear algunos maquinistas
    maquinista1 = Maquinista("Carlos", "12345678A", 3000, "Principiante")
    maquinista2 = Maquinista("Laura", "98765432B", 3500, "Experto")

    # Crear algunos mecánicos
    mecanico1 = Mecanico("Pedro", "23456789C", "123456789", "Motores")
    mecanico2 = Mecanico("Ana", "87654321D", "987654321", "Frenos")

    # Crear algunos jefes de estación
    jefe1 = JefeEstacion("Juan", "34567890E")
    jefe2 = JefeEstacion("María", "56789012F")

    # Crear algunas máquinas
    locomotora1 = Locomotora("L123", 5000, 5, mecanico1)
    locomotora2 = Locomotora("L456", 6000, 3, mecanico2)

    vagon1 = Vagon("V001", 8000, 2000, "Carga general")
    vagon2 = Vagon("V002", 10000, 5000, "Líquidos")

    # Crear algunos trenes
    tren1 = Tren(locomotora1, [vagon1], maquinista1)
    tren2 = Tren(locomotora2, [vagon2], maquinista2)

    # Imprimir información de los maquinistas
    print("Información de Maquinistas:")
    print(f"Maquinista 1: {maquinista1.nombre}, DNI: {maquinista1.dni}, Salario: {maquinista1.salario}, Rango: {maquinista1.rango}")
    print(f"Maquinista 2: {maquinista2.nombre}, DNI: {maquinista2.dni}, Salario: {maquinista2.salario}, Rango: {maquinista2.rango}")

    # Imprimir información de las máquinas
    print("\nInformación de Máquinas:")
    print(f"Locomotora 1: Matrícula: {locomotora1.matricula}, Potencia Motor: {locomotora1.potencia_motor}, Antigüedad: {locomotora1.antiguedad}")
    print(f"Locomotora 2: Matrícula: {locomotora2.matricula}, Potencia Motor: {locomotora2.potencia_motor}, Antigüedad: {locomotora2.antiguedad}")
    print(f"Vagón 1: Matrícula: {vagon1.matricula}, Capacidad Máxima: {vagon1.capacidad_maxima}, Capacidad Actual: {vagon1.capacidad_actual}, Tipo Mercancía: {vagon1.tipo_mercancia}")
    print(f"Vagón 2: Matrícula: {vagon2.matricula}, Capacidad Máxima: {vagon2.capacidad_maxima}, Capacidad Actual: {vagon2.capacidad_actual}, Tipo Mercancía: {vagon2.tipo_mercancia}")

    # Imprimir información de los trenes
    print("\nInformación de Trenes:")
    print(f"Tren 1: Maquinista: {tren1.maquinista_asignado.nombre}, Locomotora: {tren1.locomotora.matricula}, Vagones: {[vagon.matricula for vagon in tren1.vagones]}")
    print(f"Tren 2: Maquinista: {tren2.maquinista_asignado.nombre}, Locomotora: {tren2.locomotora.matricula}, Vagones: {[vagon.matricula for vagon in tren2.vagones]}")


        





























        













#ejercicio 36 no se que pasa que dice q no tocarlo

