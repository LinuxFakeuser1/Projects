players = ["peter", "mercado", "aron", "fatima", 'renata'] 
print("lista original: ", players)

# Slicing
print(players[3:5]) #fatima y renata



# El sñicing me permite trabajar con un grupo 
# especifico de una lista: al resultado se le conoce como
# un "slice"
# players = ["peter", "mercado", "aron", "fatima", 'renata'] 
print("1:4",players[1:4])
print(":3",players[:3])
print("2:",players[2:])
print("[-3:]",players[-3:])





# players = ["peter", "mercado", "aron", "fatima", 'renata'] 
# casos especiales de slicing
print("casos especiales")
print(players)
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[:0])
# caso NO especial:
print(players[0:1])

# Looping through a slice
print("looping through a slice")
players = ["peter", "mercado", "aron", "fatima", 'renata'] 

#Slicing [::] tarea
for student in players[3:5]:
    print(f"El estudiante {student},va a pasar la materia.")

print(players)

# ¿Cómo podemos opiar una lista?
my_food = ["pizza, tacos, hamburguesa"]

#tres manera de copiar una lista}
# metodo 1 utilizar un slicing

my_friend_food_2 = my_food[:]

friend_food_3 = my_food.copy()

my_friend_food_4 = list(my_food)
