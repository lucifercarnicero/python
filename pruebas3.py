import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Suponiendo que tienes una variable 'ruta_archivo' definida
ruta_archivo = 'tu_archivo.csv'
df = pd.read_csv(ruta_archivo)

# Escalado con MinMaxScaler
escalado_minmax = MinMaxScaler()
datos_escalados_minmax = escalado_minmax.fit_transform(df['price'].values.reshape(-1, 1))
print("MinMaxScaler:")
print(datos_escalados_minmax)

# Escalado con StandardScaler
escalado_standard = StandardScaler()
datos_escalados_standard = escalado_standard.fit_transform(df['price'].values.reshape(-1, 1))
print("\nStandardScaler:")
print(datos_escalados_standard)
