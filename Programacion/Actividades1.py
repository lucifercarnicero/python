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












#ejercicio 36 no se que pasa que dice q no tocarlo

