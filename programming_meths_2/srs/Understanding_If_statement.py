# if statement
cars = ["audi", "bmw", "subaru", 'Toyota']
for car in cars:
    if car == "audi":
        print(car.upper())
    else:
        print(car)


# el condicional es el corazon del if

# Para determinar igualdad utilizamos el doble igual "=="
# condicional true
#condicional verdadero
print("condicional verdadero")
truck = "ford"
print(truck == "ford")

# condicional false
#condicional falso
print("condicional falso")
print(truck == "cheyenne")


# Condicional != para determinar desigualdad
print("condicional de desigualdad")
print(truck!="tacoma") # True
print(truck!="ford")   # False

# Comparaciones numericas
age = 34
print(age==34) # true
print(age==18) # false
print(age=="34") #false

answer = 17
if answer != 42:
    print("esa respuesta no es la correcta")


age = 19
# simbolo menor que
print (age < 21) # True
print (age <= 21)# True
print (age > 21) # True
print (age >= 21)# True