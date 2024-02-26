import numpy as np
import skfuzzy as fuzz


import matplotlib.pyplot as plt

# Rango de la edad
x_edad = np.arange(18, 76, 1)
# Rango Uso del Vehículo
x_vehiculo = np.arange(0, 101, 1)
# Rango del riesgo financero (0% al 100%)
x_riesgo = np.arange(0, 101, 1)

figura = plt.figure()
fig_edad = figura.add_subplot(1,3,1)
fig_edad.set_title("Edad")
fig_edad.plot(range(18,76), x_edad)


fig_vehiculo = figura.add_subplot(1,3,2)
fig_vehiculo.set_title("Uso Vehículo")
fig_vehiculo.plot(range(0,101), x_vehiculo)

fig_riesgo = figura.add_subplot(1,3,3)
fig_riesgo.set_title("Riesgo")
fig_riesgo.plot(range(0,101), x_riesgo)

# Edad
joven = fuzz.trapmf(x_edad,[18,18,25,30] )
adulto = fuzz.trapmf(x_edad,[20,35,35,50] )
mayor = fuzz.trapmf(x_edad, [40,60,75,75] )

# Vehículo
vehiculo_bajo = fuzz.trapmf(x_vehiculo,[0,0,10,20])
vehiculo_medio = fuzz.trapmf(x_vehiculo,[10,40,40,60])
vehiculo_alto = fuzz.trapmf(x_vehiculo,[50,75,100,100])

# Riesgo
riesgo_bajo = fuzz.trapmf(x_riesgo,[0,0,10,20])
riesgo_medio = fuzz.trapmf(x_riesgo,[10,30,30,45])
riesgo_alto = fuzz.trapmf(x_riesgo,[40,55,100,100])

figura = plt.figure(figsize=(25,5))
edad = figura.add_subplot(1,3,1)
edad.plot(x_edad, joven, color="blue", label="Joven")
edad.plot(x_edad,adulto, color="orange", label="Adulto")
edad.plot(x_edad,mayor, color="green", label="Mayor")
edad.legend()
edad.set_xlabel("Edad")

vehiculo = figura.add_subplot(1,3,2)
vehiculo.plot(x_vehiculo, vehiculo_bajo, color="blue", label="Bajo")
vehiculo.plot(x_vehiculo,vehiculo_medio, color="orange", label="Medio")
vehiculo.plot(x_vehiculo,vehiculo_alto, color="green", label="Alto")
vehiculo.legend()
vehiculo.set_xlabel("Uso Vehículo")

riesgo = figura.add_subplot(1,3,3)
riesgo.plot(x_riesgo, riesgo_bajo, color="blue", label="Bajo")
riesgo.plot(x_riesgo,riesgo_medio, color="orange", label="Medio")
riesgo.plot(x_riesgo,riesgo_alto, color="green", label="Alto")
riesgo.legend()
riesgo.set_xlabel("Riesgo")

# Introducimos valores para las variables de entrada
edad_persona = 25
uso_vehiculo = 50

# Calculamos el grado de membresía de cierto valor de entrada para la variable 'edad'
edad_joven = fuzz.interp_membership(x_edad, joven, edad_persona)
edad_adulto = fuzz.interp_membership(x_edad, adulto, edad_persona)
edad_mayor = fuzz.interp_membership(x_edad, mayor, edad_persona)
print("Persona Joven:", edad_joven)
print("Persona Adulta:", edad_adulto)
print("Persona Mayor:", edad_mayor)



plt.plot(x_edad, joven, label="Joven")
plt.plot(x_edad, adulto, label="Adulto")
plt.plot(x_edad, mayor, label="Mayor")
plt.plot([edad_persona, edad_persona], [0.0, 1.0], linestyle="--")
plt.plot(edad_persona, edad_joven, 'x')
plt.plot(edad_persona, edad_adulto, 'x')
plt.plot(edad_persona, edad_mayor, 'x')
plt.legend(loc='best')
plt.xlabel('EDAD')
plt.ylabel('$\mu (e)$')
plt.show()

# Calculamos el grado de membresía de cierto valor de entrada para la variable 'uso_vehiculo'
bajo = fuzz.interp_membership(x_vehiculo, vehiculo_bajo, uso_vehiculo)
medio = fuzz.interp_membership(x_vehiculo, vehiculo_medio, uso_vehiculo)
alto = fuzz.interp_membership(x_vehiculo, vehiculo_alto, uso_vehiculo)
print("Uso vehículo Bajo:", bajo)
print("Uso vehículo Medio:", medio)
print("Uso vehículo Alto:", alto)



plt.plot(x_vehiculo, vehiculo_bajo, label="Bajo")
plt.plot(x_vehiculo, vehiculo_medio, label="Medio")
plt.plot(x_vehiculo, vehiculo_alto, label="Alto")
plt.plot([uso_vehiculo, uso_vehiculo], [0.0, 1.0], linestyle="--")
plt.plot(uso_vehiculo, bajo, 'x')
plt.plot(uso_vehiculo, medio, 'x')
plt.plot(uso_vehiculo, alto, 'x')
plt.legend(loc='best')
plt.xlabel('Uso Vehículo')
plt.ylabel('$\mu (e)$')
plt.show()

# Regla 1: "Para el riesgo alto cuando edad es joven y el uso es medio

# Usamos el mínimo para las operaciones de intersección ( y )
antecedente_1 = np.fmin(edad_joven, medio )
regla_1 = np.fmin(antecedente_1, riesgo_alto)

# Regla 2: " Para el riesgo medio cuando edad es adulto y el uso es medio"
antecedente_2 = np.fmin(edad_adulto, medio)
regla_2 = np.fmin(antecedente_2, riesgo_medio)

# Se hace la unión de los conjuntos resultantes de la aplicación de reglas
# Usamos el máximo ya que es una unión

union = np.fmax(regla_1, regla_2)

figura = plt.figure(figsize=(7,5))
axes = figura.add_subplot()

axes.plot(x_riesgo, union)
axes.plot([0,0], [0, 1], linestyle="")

# Defusificación
centroide = fuzz.defuzz(x_riesgo,union,'centroid')
bisector = fuzz.defuzz(x_riesgo,union,'bisector')
mom = fuzz.defuzz(x_riesgo,union,'mom')
som = fuzz.defuzz(x_riesgo,union,'som')
lom = fuzz.defuzz(x_riesgo,union,'lom')

print("Centroide:" , centroide)
print("Bisector:" , bisector)
print("MOM:" , mom)
print("SOM:" , som)
print("LOM:" , lom)


figura = plt.figure(figsize=(7,5))
axes = figura.add_subplot()
axes.plot(x_riesgo,union)
axes.plot([centroide,centroide], [0,1], color="red", label="Centroide")
axes.plot([bisector,bisector], [0,1], color="green", label="Bisector")
axes.plot([mom,mom], [0,1], color="blue", label="MOM")
axes.plot([som,som], [0,1], color="black", label="SOM")
axes.plot([lom,lom], [0,1], color="orange", label="LOM")
axes.set_title("Riesgo Según Edad y Uso (" + str(edad_persona) + " años " + str(uso_vehiculo) + "%)" )
axes.set_xlabel('Riesgo')
axes.legend()

