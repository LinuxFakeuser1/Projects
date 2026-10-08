# Trabajando con listas
print( "\n\t el día de hoy voy a trbajar con listas\n".upper() )
# vamos  crear una litsa de puros strings con nombres de magos
magicians = ["Harry", "ron", "hermione", "snape", "voldemort"]
print(magicians) 

print("imprimir a la mala")
print(magicians[0], magicians[1], magicians[2], magicians[3], magicians[4])

# ciclo for
print("\n\timprimir con ciclo for\n".upper())
for magician in magicians:
    print(magician.upper(), end=" ")
print("\n")
# A esto se le conoce como looping
# for cat in cats
# for dog in dogs
# for magician in magicians

# magicians = ["Harry", "ron", "hermione", "snape", "voldemort"]
# Ahora vamos a imprimir un mensaje para cada mago
for magician in magicians:
    print( f"{magician.title()} ese fue un gran hechizo \n")
    print ( f"no puedo esperar a ver el siguiente hechizo, {magician.upper()}")
print("gracias a todos por su gran espectaculo".upper() + "\n")
#  Identacion
""" 
   python utiliza la identacion para determinar
   cuando una linea de codigo esta conectada a la 
   linea de codigo anterior
   
   Basicamrntr dr utilizan 4 espcios en blanco para
   obligarnos a escribir codigo ordenado y estruturado
"""
# No olvidemos identar - Traceback-IdentationError
magicians = ["alice", "david", "caroline"]
#for magician in magicians:
#print(magician.lower())

# Error de logica - logic error
for magician in magicians:
    print(magician)
print(f"no puedo esperar a ver el siguiente truco {magician}")

#Identación inesesaria
message = "Hello Python world!"
#    print(message)

#No olvidar los puntos - Syntax Error
#for magician in magicians
#    print(magician)