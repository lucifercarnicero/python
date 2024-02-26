import os
import pandas as pd

#Solucionando problemillas de rutilla
os.chdir('C:/Users/babei/OneDrive/Escritorio/Python/Sis Aprendizaje/Tema2/21titanic')

#Genero el dataframe
titanic = pd.read_csv('titanic.csv', index_col=0)
#print(titanic) #esto no hace falta pero así lo veo

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
#print('Dimensiones:', titanic.shape)
#print('Elemntos:', titanic.size)
#print('Columnas:', titanic.columns)
#print('Filas:', titanic.index)
#print('Tipos de datos:\n', titanic.dtypes)
#print('Primeras 10 filas:\n', titanic.head(10))
#print('Últimas 10 filas:\n', titanic.tail(10))

# Pasajero con identificador 148
#print(titanic.loc[148])

# Filas pares del DataFrame.
#print(titanic.iloc[range(0,titanic.shape[0],2)])

# Personas que iban en primera clase ordenadas alfabéticamente.
#print(titanic[titanic["Pclass"]==1]['Name'].sort_values())

# Porcentaje supervivientes y fallecidos
#print(titanic['Survived'].value_counts()/titanic['Survived'].count() * 100)

# % supervivientes por clase
#print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True))

# Eliminar pasajeros eddad desconocida
#titanic.dropna(subset=['Age'], inplace=True) #inplace=True para que lo haga sobre el mismo dataframe
#print(titanic['Age'])

# Media edad mujeres clase
#print(titanic.groupby(['Pclass','Sex'])['Age'].mean().unstack()['female'])


#print(titanic[['Age', 'Menor']])

# Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
#print(titanic.groupby(['Pclass', 'Young'])['Survived'].value_counts(normalize = True) * 100)


# Crear columna con booleano si es menor de edad
titanic['Menor'] = titanic['Age'] < 18

# Supervivientes por cada grupo
survival_rates = titanic.groupby(['Pclass', 'Menor'])['Survived'].mean() * 100

# Renombrar la serie para mayor claridad
survival_rates = survival_rates.rename('Percentage Survived')

print(survival_rates)