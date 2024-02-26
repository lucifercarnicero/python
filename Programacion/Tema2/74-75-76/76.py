#76. Modifica el ejercicio 74 para crear un sistema de menús de opciones, con un primer menú de identificación de un usuario, que recogerá los datos -usuario y contraseña -y los mapeará contra una tabla USUARIOS de la base de datos LIBROS con dos campos:
## USUARIO: VARCHAR(50)
## CONTRASEÑA: VARCHAR(50)
# Si el usuario es reconocido se pasa a un segundo menú donde las opciones serán:
# Mostrar todos los datos de la tabla libros
# Actualizar un registro introduciendo como parámetro de localización la clave
# Borrar un registro empleando como criterio de identificación la clave
# Introducir una consulta por teclado y mostrar su resultado
# Salir del menú
## Si el usuario no es reconocido se pasará a una pantalla de error


import sqlite3

def mostrar_tabla(cursor):
    cursor.execute('SELECT * FROM libros')
    for libro in cursor.fetchall():
        print(libro)

# Función para verificar el login
def verificar_login(cursor, usuario, contrasena):
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?', (usuario, contrasena))
    return cursor.fetchone() is not None

# Función para crear un nuevo usuario
def crear_usuario(cursor, usuario, contrasena):
    cursor.execute('INSERT INTO usuarios VALUES (?, ?)', (usuario, contrasena))

# Función para borrar un usuario
def borrar_usuario(cursor, usuario):
    confirmacion = input("¿Estás seguro de que quieres borrar este usuario? Escribe 'sí' para confirmar: ")
    if confirmacion.lower() == 'sí':
        cursor.execute('DELETE FROM usuarios WHERE usuario = ?', (usuario,))
        print("Usuario borrado con éxito.")
    else:
        print("Borrado cancelado.")

# Conectar a la base de datos
conn = sqlite3.connect('74-75-76/libros.db')
cursor = conn.cursor()

# Crear tabla de libros si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS libros (
    clave VARCHAR(4),
    titulo VARCHAR(10),
    autor VARCHAR(20),
    fecha_edicion INTEGER,
    numero_pag VARCHAR(20)
)
''')

# Crear tabla de usuarios si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    usuario VARCHAR(50),
    contrasena VARCHAR(50)
)
''')

# Bucle principal para el menú de login
while True:
    print("\nMenú principal:")
    print("1. Login")
    print("2. Crear usuario")
    opcion_login = input("Elige una opción (1-2): ")

    if opcion_login == '1':
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        if verificar_login(cursor, usuario, contrasena):
            break
        else:
            print("Usuario o contraseña incorrectos.")
    elif opcion_login == '2':
        usuario = input("Crear usuario: ")
        contrasena = input("Crear contraseña: ")
        crear_usuario(cursor, usuario, contrasena)
        print("Usuario creado con éxito.")
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 2.")


# Bucle principal para operaciones del usuario
while True:
    print("\nOperaciones disponibles:")
    print("1. Insertar un nuevo registro")
    print("2. Borrar un registro")
    print("3. Actualizar un registro")
    print("4. Mostrar todos los registros")
    print("5. Buscar libros por autor")
    print("6. Buscar libros por número de páginas")
    print("7. Borrar usuario actual")
    print("8. Salir")
    opcion = input("Elige una opción (1-8): ")

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

    elif opcion == '7':
        borrar_usuario(cursor, usuario)
        break  # Salir del programa después de borrar el usuario

    elif opcion == '8':
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 8.")

    # Guardar cambios y mostrar contenido actualizado de la tabla
    conn.commit()

# Cerrar la conexión a la base de datos después de salir del bucle
conn.close()
