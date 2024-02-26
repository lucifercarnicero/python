#64. Escribe y ejecuta un programa que cree y escriba un archivo txt. En ese archivo se debe escribir el nombre y apellidos de cada alumno de la clase.

def ingresar_alumnos():
    with open("64-65/alumnos.txt", "w") as archivo:
        while True:
            alumno = input("Introduce el nombre y apellidos del alumno (deja en blanco para terminar): ")
            if not alumno:
                break
            archivo.write(alumno + "\n")

ingresar_alumnos()




