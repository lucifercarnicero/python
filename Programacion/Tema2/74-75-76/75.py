#75. Modifica el ejercicio 74 para que se muestre como salida el conjunto de libros cuyos autores tengan un nombre determinado introducido por teclado y un número de páginas mayor que el introducido por teclado.

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
    print("5. Buscar libros por autor")
    print("6. Buscar libros por número de páginas")
    print("7. Salir")
    opcion = input("Elige una opción (1-7): ")

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

    elif opcion == '5':
        autor_busqueda = input("Introduce el nombre del autor: ")
        cursor.execute('SELECT * FROM libros WHERE autor = ?', (autor_busqueda,))
        libros_encontrados = cursor.fetchall()
        if libros_encontrados:
            print("\nLibros encontrados por autor:")
            for libro in libros_encontrados:
                print(libro)
        else:
            print("\nNo se encontraron libros con ese autor.")

    elif opcion == '6':
        paginas_busqueda = int(input("Introduce el número de páginas mínimo: "))
        cursor.execute('SELECT * FROM libros WHERE CAST(numero_pag AS INTEGER) > ?', (paginas_busqueda,))
        libros_encontrados = cursor.fetchall()
        if libros_encontrados:
            print("\nLibros encontrados por número de páginas:")
            for libro in libros_encontrados:
                print(libro)
        else:
            print("\nNo se encontraron libros con ese número de páginas mínimo.")

    elif opcion =='7':
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 7.")

    # Guardar cambios y mostrar contenido actualizado de la tabla
    conn.commit()

# Cerrar la conexión a la base de datos después de salir del bucle
conn.close()
