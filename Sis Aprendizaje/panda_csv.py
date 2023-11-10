# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:21:16 2023

@author: babei
"""

import pandas as pd

df=pd.read_csv(r"C:\csv\unsdg_2002_2021.csv")
print(df)
print(df.head())
#print(df.describe())
#print(df.columns.values)
#print(df.index)

#print(df.sort_values("dt_year",ascending=True))
#print(df[df["dt_year"]>2010])

#print(df.iloc[4])
#print(df.iloc[:30])
#print(df.iloc[[0,1],0:5])
#print(df.loc[2,'country'])
#print(df.loc[0:5,'dt_year':'country'])

print(df.index)
#drop_duplicates() sin parámetros podemos eliminar todos los duplicados del conjunto de datos
#dropna() dropea nan o desconocidos
print(df.drop_duplicates().index)
print(df.dropna(how="all"))
print(df.dropna(subset=["mortality_rate_perc"]))
print(df.dropna())


#fillna() sustituye NaN por otros (en caso de que haya nan en todo no te dropea todo)

n_columnas=df.columns.values
print(df["mortality_rate_perc"])
media=df["mortality_rate_perc"].mean()
df["mortality_rate_perc"]=df["mortality_rate_perc"].fillna(media)
print(df["mortality_rate_perc"])

#Alternativa el uso de SimpleImputer, paquete impute de Scikit-learn. Tiene
#2 parametros missing_values y strategy (se refiere al tipo de valor por el que se va a sustituir)
#por otro lado eliminamos los datos originales con drop()



