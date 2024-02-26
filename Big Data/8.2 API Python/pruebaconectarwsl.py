import mysql.connector

try:
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host='localhost',       # o la IP de tu base de datos si no está en localhost
        user='root',            # reemplaza con tu usuario de la base de datos
        password='',            # reemplaza con tu contraseña
        database='prueba'
    )

    # Crear un cursor
    cursor = conn.cursor()

    # Datos a insertar
    datos = [
        ('Juan Perez', 30),
        ('Ana Gomez', 25)
    ]

    # Ejecutar la inserción de datos en la tabla 'holis' en lugar de 'holi'
    cursor.executemany("INSERT INTO holis (nombre, edad) VALUES (%s, %s)", datos)

    # Hacer commit de la transacción
    conn.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    print("Datos insertados correctamente.")

except mysql.connector.Error as err:
    print("Se produjo un error:", err)
