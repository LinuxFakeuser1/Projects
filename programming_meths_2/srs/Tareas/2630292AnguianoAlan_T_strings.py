# Control de Strings
# Alan Anguiuano Ayala
# Matricula: 2630292 
# correo: 2630292@upv.edu.mx

# Resumen ejecutivo
"""
==================================================
INTRODUCCIÓN
==================================================
Un string en Python es el tipo de dato (str) que se usa para almacenar
texto: una secuencia ordenada de caracteres. Los strings son inmutables,
es decir, ningún método cambia el valor original; cada operación devuelve
un nuevo string (Python Documentation, Text Sequence Type - str). Las
operaciones básicas son la concatenación (+ o f-strings), la longitud
(len()), la extracción de subcadenas con slicing (text[:30], text[::-1]),
la búsqueda de patrones (in, find(), count()) y el reemplazo de texto
(replace()), todas descritas en la documentación de String Methods. Es
importante validar y normalizar la entrada, como correos, nombres o
contraseñas, porque los usuarios escriben espacios extra, mayúsculas
mezcladas o datos inválidos, y esto causa comparaciones incorrectas o
datos basura (ver try/except en Errors and Exceptions). Este documento
cubre la descripción de cada problema, el diseño de entradas y salidas,
las validaciones aplicadas y los métodos de string usados, con casos de
prueba y el código, siguiendo las reglas de legibilidad de PEP 8.
==================================================
"""


# Principios y buenas prácticas 

"""
==================================================
PRINCIPIOS Y BUENAS PRÁCTICAS
==================================================
1. Los strings son inmutables: cualquier cambio (strip, lower, replace,
   slicing) crea un nuevo string. El original nunca se modifica, por lo
   que el resultado debe guardarse en una variable.

2. Normalizar la entrada con strip() y lower() antes de compararla, para
   que los espacios extra y las diferencias entre mayúsculas y minúsculas
   no afecten el resultado.

3. Evitar "números mágicos" en los índices. Usar variables o constantes
   con nombre (por ejemplo, LABEL_LENGTH = 30) y documentar qué extrae
   cada slice (por ejemplo, label[:30] -> los primeros 30 caracteres de
   la etiqueta).

4. Usar los métodos de string incorporados (strip, split, replace,
   isupper, isdigit, etc.) en lugar de reescribir a mano la lógica básica.

5. Diseñar validaciones claras: primero comprobar que la entrada no esté
   vacía y luego revisar su formato (longitud mínima, número válido, etc.).

6. Escribir código legible: usar nombres de variables claros (clean_name
   en lugar de x) y mensajes de error que expliquen qué salió mal y cómo
   corregirlo.
==================================================
"""

# Problemas

## Problem 1 
""" 
Problem 1: <short title>
Description: 
The program prompts for a full name, removes leading and trailing spaces with strip(), and splits it into 
a list of words with split(), which also eliminates extra internal spaces. It then verifiesthat the list 
contains at least two words, as defined by the constant MINIMAL_WORDS, and raises a ValueErrorotherwise,
which also covers empty or whitespace-only input. If the input is valid, the words are joined and converted
to Title Case, a loop prints each word and builds the initials from their first letters, and the program
finally displays the formatted name and the initials (for example, “Alan Anguiano Ayala” and “A.A.A”).

Inputs:

full_name = <The name wanted to correct>

Outputs:

completed_name = <The name, fully corrected with propper typing, example: "Alan Anguiano Ayala"> 
initials = <The initials of the completed_name value, example: "A.A.A." as the initials of:
"alan anguiano ayala"

Validations:

- when there's no word in the input the the program automatically
  raises up the ValueError and ends the program
- If there are int values in the input the program also count
  that as no words, so it also triggers the ValueError 

Test cases:
Test cases:
1 Normal: 
   Input:    "alan anguiano ayala"
   Output:   Formatted name: Juan Carlos Tovar
             Initials: J.C.T.

2 Border: 
   Input:    "   MeXICAN     LOPEZ   "  (minimum of two words, mixed case, extra spaces)
   Output:   Formatted name: Mexican Lopez
             Initials: M.L.

3 Error: 
   Input:    "Pedro"  (only one word; "" or "     " also fail)
   Output:   ValueError: Error: not enough words, name and surname required
"""
full_name = input("Please, enter your name: ")
name_precleaned = full_name.strip()
name_cleaned = name_precleaned.split()
MINIMAL_WORDS = 2
minimal_words_check = name_cleaned
if len(minimal_words_check) < MINIMAL_WORDS:
    raise ValueError("error, not enought words, name and surname required")
completed_name = " ".join(name_cleaned).title()
initials ="" 
for name_cleaned in completed_name.split():
    print(name_cleaned)
    initials += name_cleaned[0] + "."
print(f"your full name is {completed_name}")
print(f" initials: {initials}")
# AhuevoAlan

# problem 2

"""
Problem 2: <EmailVerificator>
Description: The program asks for an email address and checks that it has a
basic valid format: exactly one '@', at least one '.' after the '@', and no
spaces. If the email is valid, it also displays the domain.

Inputs:

emails = input("Enter your Email: ")

Outputs:

is a Valid Email and not valid email, prepare to die
if valid Email is true, also shows the "do_after_as"
variable

Validations:

- email_text must not be empty after strip().
- Exactly one '@' (count()).
- At least one '.' after the '@'.
- No spaces in the text.

Test cases:
1) Normal: "  user@gmail.com  "
   Output: Valid email: true / Domain: gmail.com
2) Border: "correofalso67@upv.edu.mx" (several dots in the domain)
   Output: Valid email: true / Domain: upv.edu.mx
3) Error: "user@@gmail" (two '@', no dot after it)
   Output: Valid email: false
"""
emails = input("Enter your Email: ")
# borrar espacios fuera del Email, para evitar fallos inecesarios
corrected_email = emails.strip()
# @ setting
AT_SIGN = "@"
DOT = "."
SPACES = " "
at_sign_present = corrected_email.find(AT_SIGN)
at_sign_cuantity = corrected_email.count(AT_SIGN)
#   Dots find
dot_position = corrected_email.find(DOT)
dot_after_as = corrected_email[at_sign_present+1:]
# Questioning
dot_is_present = at_sign_cuantity == 1
dot_position_questioning = DOT in dot_after_as
not_spaces = SPACES not in corrected_email
# Maquivelic if
if dot_is_present and dot_position_questioning and not_spaces:
    print(f"{dot_after_as} is a Valid Email")
else:
    print("not valid email, prepare to die")
# correofalso67@upv.edu.mx

# third problem

"""
Description: The program receives a phrase in the variable palindrome and
determines whether it is a palindrome, meaning it reads the same from left to
right and from right to left. It ignores spaces and differences between
uppercase and lowercase letters. It also displays the normalized version
of the phrase (palin_mes).

Inputs:
- palindrome (string): phrase entered by the user with input().

Outputs:
- "Is palindrome: true" or "Is palindrome: false" (from result)
- "Normalized: <palin_mes>" (phrase in lowercase and without spaces)
- Error message if the input fails the validations.

Validations:
- palin_scan (palindrome.strip().lower()) must not be empty.
- palin_mes (palin_scan without spaces) must have at least 3 characters.

Test cases:
1 Normal: palindrome = "Anita lava la tina"
   -> palin_mes = "anitalavalatina"
      palin_check = "anitalavalatina"
      Is palindrome: true
      Normalized: anitalavalatina

2 Border: palindrome = "Ana" (exactly 3 characters)
   -> palin_mes = "ana"
      palin_check = "ana"
      Is palindrome: true
      Normalized: ana

3 Error: palindrome = "   " (only spaces)
   -> Error: the phrase cannot be empty.

   Another error case: palindrome = "a"
   -> Error: the phrase must have at least 3 characters (not counting spaces).
"""
# input the palindrome
palindrome = input("enter palindrome ")

# clean the string
 
palin_scan = palindrome.strip().lower()

# Palindrome test
palin_mes = palin_scan.replace(" ","").lower()
palin_count = len(palin_mes) >= 3
if palin_count == False:
    print("Error, empty string")
else:
    palin_check = palin_mes[::-1]
    check_result = palin_mes == palin_check
    result = check_result and palin_count
    print(palin_mes)
    print(palin_check)
    print(f"this palindrome is: {result}")

# Problema 4
"""
Problem 4: Sentence analyzer

Description: The program receives a sentence, removes leading and trailing
spaces, splits it into words, and shows the word count, the first and last
words, and the shortest and longest words by length.

Inputs:
- sentence (string): sentence entered by the user with input().

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"
- Error message if the input fails the validations.

Validations:
- clean_sentence (sentence.strip()) must not be empty.
- words (clean_sentence.split()) must contain at least one word.

Test cases:
1 Normal: "  The quick brown fox  "
   -> Word count: 4
      First word: The
      Last word: fox
      Shortest word: The
      Longest word: quick

2 Border: "Hello" (a single word)
   -> Word count: 1
      First word: Hello
      Last word: Hello
      Shortest word: Hello
      Longest word: Hello

3 Error: "   " (only spaces)
   -> Error: the sentence cannot be empty.
"""
# input the sentence
sentence = input("Enter a sentence: ")

# clean the string
clean_sentence = sentence.strip()

# Validation 1: not empty
if clean_sentence == "":
    print("Error: the sentence cannot be empty.")
else:
    words = clean_sentence.split()

    # Validation process
    if len(words) == 0:
        print("Error: the sentence must contain at least one word.")
    else:
        shortest = words[0]
        longest = words[0]

        for word in words:
            if len(word) < len(shortest):
                shortest = word
            if len(word) > len(longest):
                longest = word

        print(f"Word count: {len(words)}")
        print(f"First word: {words[0]}")
        print(f"Last word: {words[-1]}")
        print(f"Shortest word: {shortest}")
        print(f"Longest word: {longest}")

# problem 5 

"""
Description: The program classifies a password as weak, medium or strong
based on its length and the types of characters it contains (uppercase,
lowercase, digits and symbols). The rules are documented in the code comments.

Inputs:
- password_input (string): password entered by the user with input().

Outputs:
- "Password strength: weak", "Password strength: medium" or
  "Password strength: strong"
- Error message if the password is empty.

Validations:
- password_input must not be empty.
- Length is checked with len() (minimum 8 to be medium or strong).

Test cases:
1 Normal: "Hello123"
   -> Password strength: medium

2 Border: "Abc123!x" (exactly 8 characters, all four types)
   -> Password strength: strong

   Other border: "Abc123!" (7 characters)
   -> Password strength: weak

3 Error: "" (empty)
   -> Error: the password cannot be empty.
"""
# input the password
password_input = input("Enter password: ")

# Validation: not empty
if password_input == "":
    print("Error: the password cannot be empty.")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for char in password_input:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_symbol = True

    types_count = 0
    if has_upper:
        types_count += 1
    if has_lower:
        types_count += 1
    if has_digit:
        types_count += 1
    if has_symbol:
        types_count += 1

    if len(password_input) < 8 or types_count == 1:
        strength = "weak"
    elif types_count == 4:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")

    # Problem 6
    """
    Problem 6: Product label generator

Description: The program receives a product name and a price and builds a
one-line label with the format "Product: <NAME> | Price: $<PRICE>". The label
is adjusted to exactly 30 characters: it is padded with spaces if shorter and
cut if longer.

Inputs:
- product_name (string): product name entered by the user with input().
- price_value (string): price entered by the user with input(), converted to
  a number only to validate it.

Outputs:
- "Label: "<exactly 30 characters>"" (shown between quotes so the spaces
  are visible)
- Error message if the input fails the validations.

Validations:
- clean_name (product_name.strip()) must not be empty.
- price_value must be convertible to a positive number.

Test cases:
1 Normal: product_name = "Pen", price_value = "2.5"
   -> Label: "Product: Pen | Price: $2.5   "

2 Border: product_name = "Notebook", price_value = "15.99"
   (the base label is longer than 30 characters and gets cut)
   -> Label: "Product: Notebook | Price: $15."

3 Error: product_name = "   " (only spaces)
   -> Error: the product name cannot be empty.

   Another error case: product_name = "Pen", price_value = "-5"
   -> Error: the price must be a positive number.
    """
#Conclusiones
"""
==================================================
CONCLUSIONES
==================================================
Trabajar con strings es esencial para la entrada y la salida de datos,
porque casi todo lo que el usuario escribe llega como texto y debe
limpiarse antes de usarse. Uso strip() para quitar espacios extra,
lower() para ignorar mayúsculas y minúsculas, split() para separar
palabras y join() para reconstruir un string a partir de una lista.
Normalizar el texto antes de compararlo es importante porque "Anita" y
"anita" son strings distintos para Python, y omitir este paso da
resultados incorrectos. Diseñar validaciones claras (primero que no esté
vacío, luego el formato) evita errores y datos basura en la lógica
principal. Aprendí que los strings son inmutables: cada método devuelve
un nuevo string, por lo que el resultado debe guardarse en una variable.
También aprendí que el slicing, como text[::-1] o label[:30], es una
forma simple de invertir o recortar texto.
==================================================
"""

# Referencias
"""
==================================================
Referencias
==================================================
1 Python Documentation - Built-in Types: Text Sequence Type - str
   https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

2 Python Documentation - String Methods (strip, lower, replace, split,
   isupper, islower, isdigit, isalnum)
   https://docs.python.org/3/library/stdtypes.html#string-methods

3 Python Tutorial - An Informal Introduction to Python: Strings
   (indexing and slicing)
   https://docs.python.org/3/tutorial/introduction.html#strings

4 Python Documentation - Errors and Exceptions (try/except, used to
   validate numeric input)
   https://docs.python.org/3/tutorial/errors.html

5 PEP 8 - Style Guide for Python Code (naming and readability)
   https://peps.python.org/pep-0008/

6 Sweigart, A. (2019). Automate the Boring Stuff with Python, 2nd ed.
   No Starch Press. Chapter 6: Manipulating Strings.
==================================================

"""
