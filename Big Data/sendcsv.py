from hdfs import InsecureClient

# Conexión al cliente HDFS
client = InsecureClient('http://192.168.47.130:50070', user='maria_dev')

# Ruta del archivo CSV en tu sistema local
local_path = 'aula15.csv'

# Ruta en HDFS (ruta relativa a /user/maría_dev)
hdfs_path = 'aula15.csv'

# Subir el archivo a HDFS
try:
    client.upload(hdfs_path, local_path)
    print(f"Archivo '{local_path}' subido a HDFS en '{hdfs_path}'")
except Exception as e:
    print("Error al subir el archivo a HDFS: ", e)

# Listar los archivos en la carpeta /user/maría_dev
try:
    files = client.list('/')
    print("Archivos en /user/maría_dev:")
    for file in files:
        print(file)
except Exception as e:
    print("Error al listar los archivos en HDFS: ", e)
