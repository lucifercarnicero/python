# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:27:13 2023

@author: babei
"""

class Nodo:
    def __init__(self,datos,hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)

    def set_hijos(self,hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre
    
    def set_datos(self,datos):
        self.datos = datos

    def get_datos(self):
        return self.datos
    
    def set_coste(self,coste):
        self.coste = coste

    def get_coste(self):
        return self.coste
    
    def igual(self,nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
        
    def en_lista(self,lista_nodos):
        en_la_lista = False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista = True
        return en_la_lista
    
    def __str__(self):
        return str(self.get_datos())

# Crear nodos de prueba
nodo_A = Nodo("A")
nodo_B = Nodo("B")
nodo_C = Nodo("C")
nodo_D = Nodo("D")
nodo_E = Nodo("E")
nodo_F = Nodo("F")

# Establecer la relación padre-hijo
nodo_A.set_hijos([nodo_B, nodo_C])
nodo_B.set_hijos([nodo_D, nodo_E])
nodo_C.set_hijos([nodo_F])

# Imprimir información de los nodos
print("Nodo A:", nodo_A)
print("Nodo B:", nodo_B)
print("Nodo C:", nodo_C)
print("Nodo D:", nodo_D)
print("Nodo E:", nodo_E)
print("Nodo F:", nodo_F)

# Comprobar si un nodo está en una lista
lista_nodos = [nodo_A, nodo_B, nodo_C]
nodo_para_comprobar = Nodo("B")

if nodo_para_comprobar.en_lista(lista_nodos):
    print(f"\nEl nodo {nodo_para_comprobar} está en la lista.")
else:
    print(f"\nEl nodo {nodo_para_comprobar} no está en la lista.")

