#59.Implementa una estructura Lista de enteros con capacidad para diez números en las que se realicen las siguientes operaciones:
# a. Un constructor donde se cree el espacio para los diez elementos
#b. obtenerNumeroElementos
#c. insertarAlFinaldeLaLista
#d. insertarAlPrincipioDeLaLista
#e. insertarEnPosicionXdeLalista
#f. añadirListaAlFinal
#g. EliminarElementoEnPosicionXdeLista
#h. ObtenerElementoEnPosicionXdeLista
#i. mostrarListaComoCadenaDeCaracteres

class Lista:
    def __init__(self):
        self.elementos = [None] * 10

    def obtener_numero_elementos(self):
        return sum(elemento is not None for elemento in self.elementos)

    def insertar_al_final(self, elemento):
        if self.obtener_numero_elementos() < 10:
            self.elementos[self.obtener_numero_elementos()] = elemento
        else:
            print("La lista está llena. No se puede insertar al final.")

    def insertar_al_principio(self, elemento):
        if self.obtener_numero_elementos() < 10:
            for i in range(self.obtener_numero_elementos(), 0, -1):
                self.elementos[i] = self.elementos[i-1]
            self.elementos[0] = elemento
        else:
            print("La lista está llena. No se puede insertar al principio.")

    def insertar_en_posicion(self, elemento, posicion):
        if posicion < 0 or posicion > self.obtener_numero_elementos():
            print("Posición inválida.")
            return

        if self.obtener_numero_elementos() < 10:
            for i in range(self.obtener_numero_elementos(), posicion, -1):
                self.elementos[i] = self.elementos[i-1]
            self.elementos[posicion] = elemento
        else:
            print("La lista está llena. No se puede insertar en la posición", posicion)

    def anadir_lista_al_final(self, lista):
        if self.obtener_numero_elementos() + len(lista) <= 10:
            for elemento in lista:
                self.insertar_al_final(elemento)
        else:
            print("No hay suficiente espacio para añadir la lista completa al final.")

    def eliminar_elemento_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.obtener_numero_elementos():
            print("Posición inválida.")
            return

        for i in range(posicion, self.obtener_numero_elementos() - 1):
            self.elementos[i] = self.elementos[i+1]
        self.elementos[self.obtener_numero_elementos() - 1] = None

    def obtener_elemento_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.obtener_numero_elementos():
            print("Posición inválida.")
            return None
        return self.elementos[posicion]

    def mostrar_lista_como_cadena(self):
        return str(self.elementos)

# Pruebas de la clase Lista
if __name__ == "__main__":
    lista = Lista()
    print(lista.mostrar_lista_como_cadena())

    lista.insertar_al_final(1)
lista.insertar_al_final(2)
lista.insertar_al_final(3)
print(lista.mostrar_lista_como_cadena())

lista.insertar_al_principio(4)
lista.insertar_al_principio(5)
lista.insertar_al_principio(6)
print(lista.mostrar_lista_como_cadena())

lista.insertar_en_posicion(7, 2)
lista.insertar_en_posicion(8, 4)
lista.insertar_en_posicion(9, 6)
print(lista.mostrar_lista_como_cadena())

lista.anadir_lista_al_final([10, 11, 12])  # Esto debería mostrar un mensaje de error porque no hay suficiente espacio.
print(lista.mostrar_lista_como_cadena())

lista.eliminar_elemento_en_posicion(3)
print(lista.mostrar_lista_como_cadena())

print(lista.obtener_elemento_en_posicion(5))
print(lista.obtener_elemento_en_posicion(10))  # Esto debería mostrar un mensaje de error porque la posición es inválida.
