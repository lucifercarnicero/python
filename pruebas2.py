from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

# Crear DataFrame de ejemplo
df = pd.DataFrame([
    ['Levis', 32, 'Amarillo', 'pantalon largo'],
    ['Jack & Jones', 34, 'Verde', 'pantalon corto'],
    ['Koroshi', 34, 'Azul', 'pantalon largo']
], columns=['nombre', 'edad', 'color', 'etiqueta'])

# Inicializar codificador y generador One-Hot
codificador_etiq = LabelEncoder()
one_hot = OneHotEncoder(categories='auto')

# Añadir columna codificada al DataFrame original
df['color_cod'] = codificador_etiq.fit_transform(df['color'])
print("DataFrame Original:")
print(df)

# Generar nuevas columnas One-Hot y eliminar columna original
dfAuxiliar = pd.get_dummies(data=df, columns=['color_cod'], drop_first=True)
df = df.drop(['color_cod'], axis=1)
print("\nDataFrame Modificado:")
print(dfAuxiliar)

