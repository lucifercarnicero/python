#67. Diseñar un programa que cree una agenda que se escriba como un fichero de texto, y que contenga contactos con ombre, DNI y teléfono. La agenda podrá añadir un nuevo contactocomprobando que no está ya en la agenda y que no esté llena-, buscar por nombre – o por cadena de texto introducida por teclado - , mostrar todos y salir guardando los datos en un archivo de texto. La agenda al iniciarse leerá el fichero de texto para comprobar si hay contactos y los cargará.

class Contacto:
    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - DNI: {self.dni} - Teléfono: {self.telefono}"

class Agenda:
    def __init__(self):
        self.contactos = []
        self.cargar_contactos()

    def añadir_contacto(self):
        nombre = input("Introduce el nombre del contacto: ")
        dni = input("Introduce el DNI del contacto: ")
        telefono = input("Introduce el teléfono del contacto: ")

        if not any(contacto.dni == dni for contacto in self.contactos):
            self.contactos.append(Contacto(nombre, dni, telefono))
            print("Contacto añadido.")
            self.guardar_contactos()
        else:
            print("El contacto ya existe.")

    def buscar_contacto(self, cadena):
        encontrados = [contacto for contacto in self.contactos if cadena.lower() in contacto.nombre.lower()]
        for contacto in encontrados:
            print(contacto)

    def mostrar_todos(self):
        for contacto in self.contactos:
            print(contacto)

    def guardar_contactos(self):
        with open("67/agenda.txt", "w") as archivo:
            for contacto in self.contactos:
                archivo.write(f"{contacto.nombre},{contacto.dni},{contacto.telefono}\n")

    def cargar_contactos(self):
        try:
            with open("agenda.txt", "r") as archivo:
                for linea in archivo:
                    nombre, dni, telefono = linea.strip().split(",")
                    self.contactos.append(Contacto(nombre, dni, telefono))
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará una nueva agenda.")

def menu():
    agenda = Agenda()

    while True:
        print("\nAgenda de contactos")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agenda.añadir_contacto()
        elif opcion == "2":
            cadena = input("Introduce el nombre o parte del nombre a buscar: ")
            agenda.buscar_contacto(cadena)
        elif opcion == "3":
            agenda.mostrar_todos()
        elif opcion == "4":
            agenda.guardar_contactos()
            print("Contactos guardados. Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
