import requests
import base64
import mysql.connector
from datetime import datetime, timedelta

# Tus credenciales de usuario y contraseña de la API
user = '93I2S5UCP1ISEF4F'
password = '6552EBDADED14014B18359DB4C3B6D4B3984D0781C2545B6A33727A4BBA1E46E'

# Codificar en Base64 las credenciales
credentials = base64.b64encode(f"{user}:{password}".encode('utf-8')).decode('utf-8')

# Encabezado de autenticación básica
headers = {
    'Authorization': f'Basic {credentials}'
}

# URL y parámetros de la API
url = 'https://sensecap.seeed.cc/openapi/list_telemetry_data'
params = {
    'device_eui': '2CF7F1C044300627',
    'channel_index': 1,
    # Aquí debes calcular el tiempo de inicio y fin basado en la fecha actual y el último mes
    'time_start': (datetime.now() - timedelta(days=30)).timestamp() * 1000,
    'time_end': datetime.now().timestamp() * 1000,
}

# Hacer la solicitud GET
response = requests.get(url, headers=headers, params=params)

# Imprimir la respuesta de la API (para depuración)
print("Respuesta de la API:")
print(response.text)

# Configuración de la conexión a la base de datos en AWS
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'sensores',  # Nombre de tu base de datos
}

# Conectar a la base de datos
conn = mysql.connector.connect(**config)

# Crear un cursor
cursor = conn.cursor()

# Datos de ejemplo obtenidos de la API (reemplaza esto con los datos reales)
dispositivo = '2CF7F1C044300627'
fecha = '2024-01-11 10:30:00'
tipo_med = 4100
valor = 25.5

# Sentencia SQL para insertar datos en la tabla "mediciones"
sql = "INSERT INTO mediciones (dispositivo, fecha, tipo_med, valor) VALUES (%s, %s, %s, %s)"
values = (dispositivo, fecha, tipo_med, valor)

# Ejecutar la inserción
cursor.execute(sql, values)

# Hacer commit para guardar los cambios en la base de datos
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()