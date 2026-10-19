# ==========================================
# COVER PAGE
# ==========================================
# Name: Alan Anguiano Ayala
# Matrícula: 2630292
# Email: 2630292@upv.edu.mx
# Group: IM-1-1
# Assignment: Collections in Python (list, tuple and dict)

# ==========================================
# EXECUTIVE SUMMARY
# ==========================================
# Una lista es una colección ordenada que se puede cambiar: se le
# agregan y se le quitan cosas. Una tupla también es ordenada pero no
# se puede cambiar una vez creada, por eso sirve para datos fijos como
# coordenadas. Un diccionario guarda parejas clave-valor y sirve para
# buscar algo por su nombre, como un precio o un teléfono.
# Aquí hay seis programas: lista de compras, puntos con tuplas,
# catálogo de productos, calificaciones, frecuencia de palabras y
# agenda de contactos. Cada uno trae descripción, entradas, salidas,
# validaciones y tres casos de prueba.

# ==========================================
# GOOD PRACTICES
# ==========================================
# - Uso listas cuando voy a agregar o quitar elementos seguido.
# - Uso tuplas para datos que no deben cambiar, como las coordenadas.
# - Uso diccionarios cuando necesito buscar algo por una clave, como
#   un nombre.
# - No modifico una lista mientras la recorro con un for.
# - Trato de que las claves de los diccionarios se entiendan.
# - Escribo código legible y mensajes claros para quien lo use.


# ==========================================
# Problem 1: Shopping list basics (list operations)
# ==========================================
# Description: Takes a list of items separated by commas, adds a new
# item at the end, shows how many items there are and says if a
# searched item is in the list.
#
# Inputs:
# - initial_items_text (string, for example "apple,banana,orange")
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list: <clean_items_list>"
# - "Total items: <total_items>"
# - "Found item: True/False"
#
# Validations:
# - The three texts cannot be empty after strip()
# - Extra spaces around each item are removed
# - My decision: an empty starting list is not accepted
#
# Test cases:
# 1) Normal: "apple, banana ,orange", "milk", "banana" ->
#    ['apple', 'banana', 'orange', 'milk'], Total 4, Found True
# 2) Border: "apple", "milk", "bread" ->
#    ['apple', 'milk'], Total 2, Found False
# 3) Error: "apple,banana", "" (empty new item) -> "Error: invalid input"

# Ask for the starting items (separated by commas)
initial_items_text = input("Add items to your list: ").strip()
initial_items = initial_items_text.split(",")
clean_items_list = []

# Go one by one removing the extra spaces and save each item in the clean list
for item in initial_items:
    clean_item = item.strip()
    clean_items_list.append(clean_item)

# Ask for the new item and for the one we want to search
new_item = input("Add a new item: ").strip()
search_item = input("Type an item that you want to search: ").strip()

# Only continue if nothing was left empty
if len(initial_items_text) > 0 and len(new_item) > 0 and len(search_item) > 0:
    # Add the new item at the end of the list
    clean_items_list.append(new_item)

    # Count the items and check if the searched one is in the list
    total_items = len(clean_items_list)
    is_in_list = search_item in clean_items_list

    print(f"Items list: {clean_items_list}")
    print(f"Total items: {total_items}")
    print(f"Found item: {is_in_list}")
else:
    print("Error: invalid input")


# ==========================================
# Problem 2: Points and distances with tuples
# ==========================================
# Description: Takes two points on a plane, saves each one in a tuple
# and shows the distance between them and the point in the middle.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A: (x1, y1)"
# - "Point B: (x2, y2)"
# - "Distance: <distance>"
# - "Midpoint: (mx, my)"
#
# Validations:
# - The four values have to be numbers
#
# Test cases:
# 1) Normal: (0, 0) and (3, 4) -> Distance 5.0, Midpoint (1.5, 2.0)
# 2) Border: (2, 2) and (2, 2), same point -> Distance 0.0, Midpoint (2.0, 2.0)
# 3) Error: "abc" in x1 -> "Error: invalid input" and it asks again

# Ask for the coordinates until all four are numbers
while True:
    try:
        x1 = float(input("Type coords x1: "))
        y1 = float(input("Type coords y1: "))
        x2 = float(input("Type coords x2: "))
        y2 = float(input("Type coords y2: "))

        # Each point goes in a tuple
        point_a = (x1, y1)
        point_b = (x2, y2)

        # Distance between the points and the point right in the middle
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        middle_point = ((x1 + x2) / 2, (y1 + y2) / 2)

        print(f"Point A: {point_a}")
        print(f"Point B: {point_b}")
        print(f"Distance: {distance}")
        print(f"Midpoint: {middle_point}")

        break  # everything went fine, so we leave the loop

    except ValueError:
        print("Error: invalid input")


# ==========================================
# Problem 3: Product catalog with dictionary
# ==========================================
# Description: Has a small catalog with the price of each product. It
# asks for a product and a quantity and shows the total to pay. If the
# product is not in the catalog it shows an error.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - "Unit price: <unit_price>"
# - "Quantity: <quantity>"
# - "Total: <total_price>"
# - "Error: product not found"
#
# Validations:
# - product_name cannot be empty after strip()
# - quantity has to be greater than 0
# - The product has to exist in the catalog
#
# Test cases:
# 1) Normal: Pokeball, 3 -> Unit price 200.0, Quantity 3, Total 600.0
# 2) Border: Ultraball, 1 -> Unit price 800.0, Quantity 1, Total 800.0
# 3) Error: Masterball, 2 -> "Error: product not found" and it asks again

# Catalog: the name of the product and its price
products = {
    "Pokeball": 200.0,
    "Superball": 600.0,
    "Ultraball": 800.0
}
print(products)

# Ask until we get a product from the catalog and a valid quantity
while True:
    try:
        product_name = input("Type a product name: ").strip()
        quantity = int(input("Type the quantity: "))

        # The name cannot be empty and the quantity has to be more than 0
        if len(product_name) == 0 or quantity <= 0:
            print("Error: invalid input")
            continue

        if product_name in products:
            unit_price = products[product_name]
            total_price = unit_price * quantity
            print(f"Unit price: {unit_price}")
            print(f"Quantity: {quantity}")
            print(f"Total: {total_price}")
            break  # done, we leave the loop
        else:
            print("Error: product not found")

    except ValueError:
        print("Error: invalid input")


# ==========================================
# Problem 4: Student grades with dict and list
# ==========================================
# Description: Has a dictionary where each student has a list of
# grades. It asks for a student, shows his grades and his average, and
# says if he passed (average of 70 or more).
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - "Grades: <grades_list>"
# - "Average: <average>"
# - "Passed: True/False"
# - "Error: student not found"
#
# Validations:
# - student_name is cleaned with strip()
# - The student has to exist in the dictionary
#
# Test cases:
# 1) Normal: Alan -> Grades [67, 80, 100], Average 82.33, Passed True
# 2) Border: "  Olaf  " (extra spaces) -> Grades [100, 100, 67],
#    Average 89.00, Passed True
# 3) Error: Marta -> "Error: student not found" and it asks again

# Each student has his list of grades
grades = {
    "Alan": [67, 80, 100],
    "Víctor": [90, 100, 67],
    "Olaf": [100, 100, 67]
}
print(grades)

# Ask for a student until we find one in the dictionary
while True:
    student_name = input("Type a name of a student: ").strip()

    if student_name in grades:
        # Average = sum of the grades divided by how many there are
        average = sum(grades[student_name]) / len(grades[student_name])

        # The student passes with 70 or more
        is_passed = False
        if average >= 70.0:
            is_passed = True

        print(f"Grades: {grades[student_name]}")
        print(f"Average: {average:.2f}")
        print(f"Passed: {is_passed}")
        break  # done, we leave the loop
    else:
        print("Error: student not found")


# ==========================================
# Problem 5: Word frequency counter (list + dict)
# ==========================================
# Description: Takes a sentence, separates it into words and counts how
# many times each word appears. At the end it shows the most repeated
# word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Words list: <words>"
# - "Frequencies: <freq_dict>"
# - "Most common word: <most_common>"
#
# Validations:
# - The sentence cannot be empty after split()
# - My decision: punctuation is not removed, so "hello," and "hello"
#   count as different words
# - If two words tie, the one that appears first is shown
#
# Test cases:
# 1) Normal: "the cat and the dog" -> Frequencies {'the': 2, 'cat': 1,
#    'and': 1, 'dog': 1}, Most common word the
# 2) Border: "Hello" -> Words ['hello'], Frequencies {'hello': 1},
#    Most common word hello
# 3) Error: "   " (only spaces) -> "Error: invalid input"

# Ask for a sentence in lowercase and cut it into words
words = input("Type a sentence: ").lower().split()
freq_dict = {}
most_common = ""
max_freq = 0

if len(words) <= 0:
    print("Error: invalid input")
else:
    # Count each word: if it is already there add 1, if not start it at 1
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    # Look for the word that appears the most
    for word, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            most_common = word

    print(f"Words list: {words}")
    print(f"Frequencies: {freq_dict}")
    print(f"Most common word: {most_common}")


# ==========================================
# Problem 6: Simple contact book (dictionary CRUD)
# ==========================================
# Description: A small contact book. It asks for an action: ADD saves
# or updates a contact, SEARCH shows the phone of a contact and DELETE
# removes a contact.
#
# Inputs:
# - action_text (ADD, SEARCH or DELETE)
# - name (string)
# - phone (string, only for ADD)
#
# Outputs:
# - "Contact saved: <name> <phone>"
# - "Phone: <phone>"
# - "Contact deleted: <name>"
# - "Error: contact not found"
# - "Error: invalid input"
#
# Validations:
# - The action is turned to uppercase and has to be one of the three
# - name (and phone for ADD) cannot be empty after strip()
#
# Test cases:
# 1) Normal: SEARCH, "Alan (FocaSlayer777)" -> Phone: 8347776667
# 2) Border: "add" in lowercase, "Marta", "8341234567" ->
#    Contact saved: Marta 8341234567
# 3) Error: "HELLO" -> "Error: invalid input"

# Contacts: the name and the phone number
contacts = {
    "Ángel": "8341676767",
    "Alan": "8347776667",
    "Olaf": "8346667749",
    "Mermilio": "8341806767"
}

print(contacts)

action_text = input("ADD, SEARCH or DELETE: ").strip().upper()

if action_text == "ADD":
    name = input("Type a name: ").strip()
    phone = input("Type the phone: ").strip()
    # Do not save a contact with an empty name or phone
    if len(name) == 0 or len(phone) == 0:
        print("Error: invalid input")
    else:
        contacts[name] = phone
        print(f"Contact saved: {name} {phone}")

elif action_text == "SEARCH":
    name = input("Type a contact to search: ").strip()
    phone = contacts.get(name)
    if phone is not None:
        print(f"Phone: {phone}")
    else:
        print("Error: contact not found")

elif action_text == "DELETE":
    name = input("Type a contact to delete: ").strip()
    deleted = contacts.pop(name, None)
    if deleted is not None:
        print(f"Contact deleted: {name}")
    else:
        print("Error: contact not found")

else:
    print("Error: invalid input")


# ==========================================
# CONCLUSIONS
# ==========================================
# Usé listas cuando los datos cambian (la lista de compras), tuplas
# para lo que no debe cambiar (los puntos) y diccionarios para buscar
# por nombre (productos, alumnos, contactos).
# Una lista deja agregar con append(). Una tupla no se puede modificar,
# y eso evita cambiarla por error.
# Con un diccionario buscar un nombre es directo, sin recorrerlo todo.
# Dos combinaciones se repitieron: un diccionario con listas dentro (las
# calificaciones) y una lista con un diccionario para contar palabras.

# ==========================================
# REFERENCES
# ==========================================
# 1) Python documentation - Built-in Types: list, tuple
#    https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 2) Python documentation - Built-in Types: dict
#    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# 3) Python Tutorial - Data Structures
#    https://docs.python.org/3/tutorial/datastructures.html
# 4) Real Python - Lists and Tuples in Python
#    https://realpython.com/python-lists-tuples/
# 5) Real Python - Dictionaries in Python
#    https://realpython.com/python-dicts/
# 6) W3Schools - Python Dictionaries
#    https://www.w3schools.com/python/python_dictionaries.asp