# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:48:26 2023

@author: babei
"""

import numpy as np

A = np.array([1, 2, 3])
print(A)
B = np.array([[1, 2, 3], [4, 5, 6]])
print(B)

print(A.shape) #puedo ver las dimensiones de la matriz
print(B.shape)

C = np.arange(1, 10, 2) #crea un vector con los valores del 1 al 10, con saltos de 2
print(C)
print(np.zeros((3, 3))) #crea una matriz de 3x3 con ceros

#arrays random
E=np.random.random((2,4))

print(E)

print(np.random.randint(1,10,5))

#array de identidad
print(np.ones((4,4)))

F=np.array([[1,2],[3,4]])
G=np.array([[5,6],[7,8]])

print (F*G)

#Producto escala
print(np.dot(F, G))


#Libreria gráfica

import matplotlib.pyplot as plt
import numpy as np

#mirate el subplot2grid porque tela 

plt.plot([1,2,3,4,5,6,7,8],[1,4,9,16,21,25,28,29],label="y=")
plt.title("grafica de y=m**2")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()



