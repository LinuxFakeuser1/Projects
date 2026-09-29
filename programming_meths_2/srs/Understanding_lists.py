#Understanding_lists
"""
Las listas nos permiten almacenar información en un lugar la cantidad que se 
desee: ya sean pocos elementos o millones de elementos

Una lista es una colección de items (elementos)
que tiene un orden particular. se pueden crear 
listas que incluyen strings, enteros, floats,
los nombres de las personas de tu familia, etcétera,
podemos almacenar (los tipos de datos permitido en python)
lo que queramos en una lista.

Son elementos mutables:pueden modificarse su tamaño en la lista

Se recomienda nombrar una variable del tipo lista en plural

En python, los corchetes indican [] una lista,
sus elementos se separan por comas.
 
 Ejemplo:
"""
bycicles = ["treck","cannondale," 'redline', 'specialized', 'apache']
print(bycicles)

# ¿como podemos acceder a los elemento de una lista?

"""
   Las listas son colecciones ordenadas. se puede aceder
   a un elemento de una lista diciendole a Python la 
   posición o índice o del elemento deseado
   
   Para obtener el valor deseado se debe escribir 
   el nombre de la lista, seguido del índice del elemento 
   entre corchetes"""

print(bycicles[0], bycicles[1], bycicles[2], bycicles[3])

print(bycicles[0].upper())

#Los índiices comienzan en 0 no en 1
# Ejemplo:

print(bycicles[1])
print(bycicles[3])

message = f"My first bycicle was a {bycicles[-1].upper()}]"
print (message)