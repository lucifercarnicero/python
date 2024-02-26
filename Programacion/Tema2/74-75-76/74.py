#74. Realiza un ejercicio en el que puedas acceder a un base de datos LIBROS, con una tabla libros que tenga como campos:

## CLAVE: VARCHAR(4).
## TITULO: VARCHAR(10).
## AUTOR: VARCHAR(20).
## FECHA EDICION: INTEGER.
## NUMERO_PAG: VARCHAR(20)

# En el script Introduce varios registros, borra al menos uno y actualiza al menos otro. Tras cada operación la salida de datos deberá mostrar el contenido de la tabla por consola.

import sqlite3

def mostrar_tabla(cursor):
    cursor.execute('SELECT * FROM libros')
    for libro in cursor.fetchall():
        print(libro)

# Conectar a la base de datos
conn = sqlite3.connect('74-75-76/libros.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    clave VARCHAR(4),
    titulo VARCHAR(10),
    autor VARCHAR(20),
    fecha_edicion INTEGER,
    numero_pag VARCHAR(20)
)
''')

# Bucle principal para operaciones del usuario
while True:
    print("\nOperaciones disponibles:")
    print("1. Insertar un nuevo registro")
    print("2. Borrar un registro")
    print("3. Actualizar un registro")
    print("4. Mostrar todos los registros")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        clave = input("Introduce la clave (VARCHAR(4)): ")
        titulo = input("Introduce el título (VARCHAR(10)): ")
        autor = input("Introduce el autor (VARCHAR(20)): ")
        fecha_edicion = int(input("Introduce la fecha de edición (INTEGER): "))
        numero_pag = input("Introduce el número de páginas (VARCHAR(20)): ")
        cursor.execute('INSERT INTO libros VALUES (?, ?, ?, ?, ?)', (clave, titulo, autor, fecha_edicion, numero_pag))

    elif opcion == '2':
        clave = input("Introduce la clave del libro a borrar: ")
        cursor.execute('DELETE FROM libros WHERE clave = ?', (clave,))

    elif opcion == '3':
        clave = input("Introduce la clave del libro a actualizar: ")
        nuevo_titulo = input("Introduce el nuevo título: ")
        cursor.execute('UPDATE libros SET titulo = ? WHERE clave = ?', (nuevo_titulo, clave))

    elif opcion == '4':
        mostrar_tabla(cursor)

    elif opcion =='5':
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")

    # Guardar cambios y mostrar contenido actualizado de la tabla
    conn.commit()
    print("\nEstado actualizado de la tabla:")
    mostrar_tabla(cursor)

# Cerrar la conexión a la base de datos después de salir del bucle
conn.close()



