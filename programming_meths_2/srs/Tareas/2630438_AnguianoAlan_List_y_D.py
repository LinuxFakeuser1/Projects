"""
COVER PAGE

Alumno: Alan Anguiano Ayala
Matrícula: 2630292
correo: 2630292@upv.edu.mx
grupo: IM-1-1
Tlabajo: Collections in Python (list, tuple and dict)
"""

"""
EXECUTIVE SUMMARY

Una lista es una colección ordenada que se puede cambiar: se le
agregan y se le quitan cosas. Una tupla también es ordenada pero no
se puede cambiar una vez creada, por eso sirve para datos fijos como
coordenadas. Un diccionario guarda parejas clave-valor y sirve para
buscar algo por su nombre, como un precio o un teléfono.
Aquí hay seis programas: lista de compras, puntos con tuplas,
catálogo de productos, calificaciones, frecuencia de palabras y
agenda de contactos. Cada uno trae descripción, entradas, salidas,
validaciones y tres casos de prueba.
"""

"""
GOOD PRACTICES

- Uso listas cuando voy a agregar o quitar elementos seguido.
- Uso tuplas para datos que no deben cambiar, como las coordenadas.
- Uso diccionarios cuando necesito buscar algo por una clave, como
  un nombre.
- No modifico una lista mientras la recorro con un for.
- Trato de que las claves de los diccionarios se entiendan.
- Escribo código legible y mensajes claros para quien lo use.
"""

# problem 1
"""
Problem 1: Shopping list basics (list operations)

Description: The program takes a list of items separated by commas, adds a
new item at the end, shows how many items there are and says if a searched
item is in the list.

Inputs:
- initial_items_text (string): items separated by commas, for example
  "mango,grape,lemon".
- new_item (string): item to add at the end of the list.
- search_item (string): item to look for in the list.

Outputs:
- "Items list: <clean_items_list>"
- "Total items: <total_items>"
- "Found item: True" or "Found item: False"
- "Error: invalid input" if the input fails the validations.

Validations:
- initial_items_text, new_item and search_item cannot be empty after strip().
- Extra spaces around each item are removed.
- An empty starting list is not accepted.

Test cases:
1) Normal: initial_items_text = "mango, grape ,lemon", new_item = "cheese",
   search_item = "grape"
   -> Items list: ['mango', 'grape', 'lemon', 'cheese']
      Total items: 4
      Found item: True

2) Border: initial_items_text = "mango", new_item = "cheese",
   search_item = "rice"
   -> Items list: ['mango', 'cheese']
      Total items: 2
      Found item: False

3) Error: initial_items_text = "mango,grape", new_item = "" (empty)
   -> Error: invalid input
"""

# Ask for the starting products (separated by commas)
initial_items_text = input("Add items to your list: ").strip()
raw_items = initial_items_text.split(",")
clean_items_list = []

# Review each product, remove the extra spaces and store it in the clean list
for raw_item in raw_items:
    trimmed_item = raw_item.strip()
    clean_items_list.append(trimmed_item)

# Ask for the product to add and for the one to look for
new_item = input("Add a new item: ").strip()
search_item = input("Type an item that you want to search: ").strip()

# Continue only if none of the texts is empty
if len(initial_items_text) > 0 and len(new_item) > 0 and len(search_item) > 0:
    # Put the new product at the end of the list
    clean_items_list.append(new_item)

    # Count the products and check if the searched one is inside the list
    total_items = len(clean_items_list)
    item_found = search_item in clean_items_list

    print(f"Items list: {clean_items_list}")
    print(f"Total items: {total_items}")
    print(f"Found item: {item_found}")
else:
    print("Error: invalid input")

# Problem2
"""
Problem 2: Points and distances with tuples

Description: The program takes two points on a plane, saves each one in a
tuple and shows the distance between them and the point in the middle.

Inputs:
- x1, y1, x2, y2 (float): coordinates of the two points.

Outputs:
- "Point A: (x1, y1)"
- "Point B: (x2, y2)"
- "Distance: <distance>"
- "Midpoint: (mx, my)"
- "Error: invalid input" if a value is not a number.

Validations:
- The four values have to be numbers.

Test cases:
1) Normal: (1, 1) and (4, 5)
   -> Distance: 5.0
      Midpoint: (2.5, 3.0)

2) Border: (7, 7) and (7, 7), same point
   -> Distance: 0.0
      Midpoint: (7.0, 7.0)

3) Error: "xyz" in x1
   -> Error: invalid input (and it asks again)
"""

# Keep asking until the four coordinates are valid numbers
while True:
    try:
        x1 = float(input("Type coords x1: "))
        y1 = float(input("Type coords y1: "))
        x2 = float(input("Type coords x2: "))
        y2 = float(input("Type coords y2: "))

        # Store each point inside its own tuple
        point_a = (x1, y1)
        point_b = (x2, y2)

        # Calculate the separation between both points and their center
        delta_x = x2 - x1
        delta_y = y2 - y1
        distance = (delta_x**2 + delta_y**2)**0.5
        middle_point = ((x1 + x2) / 2, (y1 + y2) / 2)

        print(f"Point A: {point_a}")
        print(f"Point B: {point_b}")
        print(f"Distance: {distance}")
        print(f"Midpoint: {middle_point}")

        break  # all good, exit the loop

    except ValueError:
        print("Error: invalid input")

"""
CONCLUSIONS

Usé listas cuando los datos cambian (la lista de compras), tuplas
para lo que no debe cambiar (los puntos) y diccionarios para buscar
por nombre (productos, alumnos, contactos).
Una lista deja agregar con append(). Una tupla no se puede modificar,
y eso evita cambiarla por error.
"""

"""
REFERENCES

1) Python documentation - Built-in Types: list, tuple
   https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
2) Python documentation - Built-in Types: dict
   https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
3) Python Tutorial - Data Structures
   https://docs.python.org/3/tutorial/datastructures.html
4) Real Python - Lists and Tuples in Python
   https://realpython.com/python-lists-tuples/
5) Real Python - Dictionaries in Python
   https://realpython.com/python-dicts/
6) W3Schools - Python Dictionaries
   https://www.w3schools.com/python/python_dictionaries.asp
"""