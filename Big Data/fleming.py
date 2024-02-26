from sqlalchemy import create_engine
import pandas as pd

# Datos de conexión usando SQLAlchemy
engine = create_engine('mssql+pymssql://lector:oviedo.2023@serverfleming.database.windows.net/fleming2023')

# Crear una consulta SQL para obtener los datos deseados
query = """
SELECT *
FROM mediciones
WHERE fecha >= '2023-12-04' AND fecha <= '2023-12-10'
"""

# Usar pandas para leer la consulta SQL en un DataFrame
try:
    df = pd.read_sql(query, engine)
    print(df)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv('aula15.csv', index=False)
    print("Datos guardados en 'aula15.csv'")
except Exception as e:
    print("Error al ejecutar la consulta o al guardar en CSV: ", e)
finally:
    engine.dispose()
