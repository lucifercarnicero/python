# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:04:50 2023

@author: babei
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
import numpy as np

df=pd.read_csv(r"C:\csv\unsdg_2002_2021-2.csv")

df_nuevo = df.drop(columns=['region','dt_year','dt_date'])

df_nivel_desarrollo=df_nuevo[['country','level_of_development']]

df_nivel_desarrollo_valores_unicos = df_nivel_desarrollo.drop_duplicates()

df_nuevo=df_nuevo.groupby(by=["country"]).mean()

y=pd.DataFrame(df_nivel_desarrollo_valores_unicos["level_of_development"])

n_columnas=df_nuevo.columns.values
n_filas=np.arange(1,len(y.index)+1,1)

imp=SimpleImputer(missing_values=np.nan,strategy="mean")
imp=imp.fit(df_nuevo.values)
df_nuevo=imp.transform[df_nuevo.values]

estandarizacion=StandardScaler()

df_estandarizado=estandarizacion.fit_transform(df_nuevo)
print(df_estandarizado)

x=pd.DataFrame(df_estandarizado,index=n_filas,columns=n_columnas)
print(x.values)
print(y.values)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
print(x_train.values)
print(y_train.values)