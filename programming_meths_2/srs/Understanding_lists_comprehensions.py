"""
    Una list comprehension combina
    el for loop y la creacion de nuevos elementos
    en una sola línea y automaticamente agrega
    cada nuevo elemento a la lista, es decir,
    sin utilizar el metodo append.
"""
squares = [value**2 for value in range(1,11)]
print(squares)

# utilizando list_comprehensions

names = [ "renata", "peter", "sebas", "balam", "leo", "abanico"]
names_upv = [name+"@upv.edu.mx" for name in names]
print(names_upv)