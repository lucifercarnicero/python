import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('74-75-76/libros.db')
cursor = conn.cursor()

# Eliminar la tabla "usuarios" si existe
cursor.execute("DROP TABLE IF EXISTS usuarios;")

# Commit para guardar los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()
