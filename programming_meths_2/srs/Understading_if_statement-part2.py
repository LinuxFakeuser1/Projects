"""
    Realizar un ejercicio que determine el costo de
    un boleto a partir de las siguientes condiciones:
    
    - costo para una persona """
 
SIXSEVEN = "O7"
print("sistema de boletaje")
age = input("\n igresa tu edad: ")

print(age)
print(type(age))
age = int(age)
print(type(age))
if age < 0:
    print("Pon una edad de verdad baboso")
if age == 67: 
    print(SIXSEVEN)


if age <= 4 and age == 0:
    cost = 0
if age > 4 and age < 18:
    cost = 250 
if age >= 18:
    cost = 500

print(f"el costo por tu boleto es: {cost}")

# Tambien se puede hacer con un solo If: Bloque if/else

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200 
elif age >= 18:
    cost = 500
else: 
    cost = 0

print(" bloque if elif ")
print(f"El bloque if elif da:{cost}")