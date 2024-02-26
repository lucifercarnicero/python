import os
import pandas as pd
import numpy as np
import datetime as dt

# Solucionando problemillas de rutilla
os.chdir('C:/Users/babei/OneDrive/Escritorio/Python/Sis Aprendizaje/Tema2/22emisiones')

# Dataframe de los 4 ficheros
import pandas as pd 

emisiones2016 = pd.read_csv('emisiones2016.csv', sep = ';')
emisiones2017 = pd.read_csv('emisiones2017.csv', sep = ';')
emisiones2018 = pd.read_csv('emisiones2018.csv', sep = ';')
emisiones2019 = pd.read_csv('emisiones2019.csv', sep = ';')
emisiones = pd.concat([emisiones2016, emisiones2017, emisiones2018, emisiones2019])
emisiones

# Comprensión de lista con las columnas
# Incluimos 'ESTACION', 'MAGNITUD', 'ANO', 'MES' y cualquier columna que comience con 'D'
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + [col for col in emisiones.columns if col.startswith('D')]

# Filtramos el DataFrame para incluir solo las columnas deseadas
emisiones_filtradas = emisiones[columnas]
emisiones_filtradas
#print(emisiones_filtradas)

# Valores de los contaminantes de las columnas de los días aparezcan en una única columna.
emisiones_filtradas = emisiones_filtradas.melt(id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='DIA', value_name='VALOR')
emisiones_filtradas


# Nueva colum fechas
emisiones_filtradas['DIA'] = emisiones_filtradas['DIA'].str.strip('D') #elimino D al inicio
# Concatenamos año, mes y día en un formato de fecha
emisiones_filtradas['FECHA'] = emisiones_filtradas['ANO'].astype(str) + '/' + emisiones_filtradas['MES'].astype(str) + '/' + emisiones_filtradas['DIA'].astype(str)
# Columna fecha convertir a fecha
emisiones_filtradas['FECHA'] = pd.to_datetime(emisiones_filtradas['FECHA'], format='%Y/%m/%d', errors='coerce')
emisiones_filtradas

#Eliminar fecha no validas con isnan
emisiones_filtradas = emisiones_filtradas[~np.isnan(emisiones_filtradas['FECHA'])]
# Ordenar el DataFrame por estaciones, contaminantes y fecha
emisiones_filtradas = emisiones_filtradas.sort_values(by=['ESTACION', 'MAGNITUD', 'FECHA'])

#Mostrar por pantalla las estaciones y los contaminantes disponibles en el DataFrame. 
#print(emisiones_filtradas['ESTACION'].unique())
#print(emisiones_filtradas['MAGNITUD'].unique())

# Función que devuelve las emisiones de un contaminante dado en una estación y rango de fechas dado.
def evolucion(estacion, contaminante, desde, hasta):
    return emisiones_filtradas[(emisiones_filtradas.ESTACION == estacion) & (emisiones_filtradas.MAGNITUD == contaminante) & (emisiones_filtradas.FECHA >= desde) & (emisiones_filtradas.FECHA <= hasta)].sort_values('FECHA').VALOR

#print(evolucion(60, 8, dt.datetime.strptime('2016/3/26', '%Y/%m/%d'), dt.datetime.strptime('2019/03/26', '%Y/%m/%d')))

#h.	Mostrar un resumen descriptivo (mínimo, máximo, media, etc.) para cada contaminante. 


#print(emisiones_filtradas.groupby('MAGNITUD').VALOR.describe())

#supongo estaciones en distintos distritos
#print(emisiones_filtradas.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()) 

#j.	Crear una función que reciba una estación y un contaminante y devuelva un resumen descriptivo de las emisiones del contaminante indicado en la estación indicada. 

def resumen(estacion, contaminante):
    return emisiones_filtradas[(emisiones_filtradas.ESTACION == estacion) & (emisiones_filtradas.MAGNITUD == contaminante)].VALOR.describe()

#print(resumen(60, 8))

#k.	Crear una función que devuelva las emisiones medias mensuales de un contaminante y un año dados para todas las estaciones. 

def evolucion_mensual(contaminante, ano):
    return emisiones_filtradas[(emisiones_filtradas.MAGNITUD == contaminante) & (emisiones_filtradas.ANO == ano)].groupby('MES').VALOR.mean()

#print(evolucion_mensual(8, 2019))

#l.	Crear una función que reciba una estación de medición y devuelva un DataFrame con las medias mensuales de los distintos tipos de contaminantes. 

def evolucion_mensual_estacion(estacion):
    return emisiones_filtradas[emisiones_filtradas.ESTACION == estacion].groupby(['MES', 'MAGNITUD']).VALOR.mean()

#print(evolucion_mensual_estacion(60))

#m.	Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla un diagrama de líneas con la evolución de las ventas.

import matplotlib.pyplot as plt

def evolucion_ventas():
    # Preguntar por el rango de años
    inicio = int(input('Introduce año de inicio: '))
    fin = int(input('Introduce año de fin: '))
    # Filtrar por ese rango de años
    evolucion = emisiones_filtradas[(emisiones_filtradas.ANO >= inicio) & (emisiones_filtradas.ANO <= fin)]
    # Agrupar por año y contaminante y calcular la media
    evolucion = evolucion.groupby(['ANO', 'MAGNITUD']).VALOR.mean()
    # Mostrar diagrama de líneas
    evolucion.unstack().plot(kind='line', subplots=True)
    plt.show()

evolucion_ventas()
    








# Función que devuelve un resumen descriptivo de un contaminante dado.
def resumen_contaminante(contaminante):
    return emisiones_filtradas[emisiones_filtradas.MAGNITUD == contaminante].VALOR.describe()

#print(resumen_contaminante(8))


