from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame([
    ['Levis', 32, 'Amarillo', 'pantalon largo'],
    ['Jack & Jones', 34, 'Verde', 'pantalon corto'],
    ['Koroshi', 34, 'Azul', 'pantalon largo']
])

df.columns = ['nombre', 'edad', 'color', 'etiqueta']
codificador_etiq = LabelEncoder()
one_hot = OneHotEncoder(categories='auto')

# Creación de una columna donde convertir las categorías a números
df['color_cod'] = codificador_etiq.fit_transform(df.color)
print(df)

# Creamos las nuevas columnas a partir de la columna color_cod
datos_one_hot = one_hot.fit_transform(df.color_cod.values.reshape(-1, 1)).toarray()

# Añadimos las columnas
df_mod = pd.DataFrame(datos_one_hot, columns=['color_' + str(i) for i in range(len(df.color))])
df = pd.concat([df, df_mod], axis=1)
df = df.drop(['color', 'color_cod'], axis=1)  # Borramos las columnas que sobran
print(df)
