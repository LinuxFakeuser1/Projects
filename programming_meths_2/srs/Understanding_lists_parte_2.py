#Agregando elementos a una lista

motorcycles = ['honda', 'Mortalika', 'yamaha']
print(motorcycles[2].capitalize)

# Método Append
motorcycles.append("kawazaki")
print(motorcycles)

""" 
  El método append se yuda a crear listas fácilmente
  de manera dinámica
"""
message_2 = "Ducatti", "Alanmoto"
motorcycles_2 = ["Mortalika"]
motorcycles.append("honda")
motorcycles.append("Yamaha")
motorcycles.append("suzuki")
motorcycles.append(message_2)
print(motorcycles)

# Metodo insert
motorcycles_2.insert (1,"Harley")
print(motorcycles_2)

# Metodo Pop
""" 
  "PERMITE ELIMINAR EL ULTIMO ELEMENTO DE LA LISA
  PERO NOS PERMITE UTILIZARLO DESPUÉS DE ELLO"
"""
print("aquí aprendi a utilizar el pop".upper)

motorcycles_4 = ['honda', 'Mortalika', "hd", 'yamaha']
deleted_motorcycles = motorcycles_4.pop(-1)

print ( f"motocicleta borrada es: {deleted_motorcycles}")
print(motorcycles_4)
# Metodo remove

motorcycles.remove("Mortalika")
print(motorcycles)

# metodo reverse
motorcycles.reverse()
print(motorcycles)