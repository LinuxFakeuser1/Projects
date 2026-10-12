""" 
    TUPLAS

    las tuplas son listas de elemento que no cambian de tamaño.
    las tuplas son listas inmutables
    
    
    Se utilizan los paréntesis () para definir una tupla

    Ejemplo:
        
        Si tenemos un rectángulo (largo, ancho) que siempre va 
        a tener el mismo tamaño, podemos aegurar que sus dimensiones
        no van a cambiarsi colocamos sus valores en una tupla.

"""
dimensions = (200, 50) # 200 de largo x 50 de ancho
print("tupla original:", dimensions)

# vamos a imprimir elementos de una tupla
# se realizade la misma forma que en una lista
print(dimensions [0])
print(dimensions [1])
print(dir(dimensions))

# vamos  modificar el valor de una lista
names = ["carlos", "charly", "juan", "wendy"]
print (names)
names[0] = "Mercury"
names[1] = "Mercury"
names[2] = "Mercury"
names[3] = "Mercury"
print(names)

# dimensions[0] = 500 #esta operacion no está permitida


# Looping en tuplas
#dimensions_2 = (1, 11, 111, 1111, 11111)
#for dimension in dimensions_2 (1,3):
#    print(dimension)

for dimension in dimensions:
    print(dimension)

"""
    No podemos modificar una tupla
    lo que si podemos hacer es cambiar
    la asignacion de una variable que
    almacena una tupla
"""
dimensions = (500, 1000, 20)
print("tupla re-definida:", dimensions)

# Tipos de datos booleanos
answer = True
print(answer)
