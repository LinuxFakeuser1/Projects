# 
# Alan Anguiuano Ayala
# Matricula: 2630292 
# correo: 2630292@upv.edu.mx

# Resumen ejecutivo
"""

==================================================
INTRODUCTION
==================================================

"""
# buenas prácticas
"""

==================================================
PRINCIPIOS Y BUENAS PRÁCTICAS
==================================================
1. Usar tipos de datos apropiados: int para contadores (por ejemplo, el
   número de palabras o de caracteres) y float para cantidades con
   decimales (por ejemplo, un precio). Convertir la entrada con int() o
   float() hace explícito el tipo y evita mezclar texto con números.

2. Evitar duplicar expresiones complejas: guardar los resultados
   intermedios en variables. Por ejemplo, guardar una sola vez
   clean_sentence = sentence.strip() y reutilizarla, en lugar de repetir
   sentence.strip() en varios lugares.

3. Validar los datos antes de operar con ellos. Comprobar que la entrada
   no esté vacía, que los números sean válidos y que valores como horas,
   salarios o precios no sean negativos o cero cuando eso no tiene
   sentido.

4. Usar nombres de variables descriptivos y mensajes claros para el
   usuario. Nombres como clean_name o price_number explican su contenido,
   y un error como "el precio debe ser un número positivo" le indica al
   usuario qué debe corregir.

5. Documentar claramente cómo se interpretan los booleanos. Por ejemplo,
   en el verificador de palíndromos, result = True significa que el texto
   normalizado es igual a su inverso, y False significa que no lo es. En
   el clasificador de contraseñas, has_upper = True significa que la
   contraseña contiene al menos una letra mayúscula, y False significa
   que no contiene ninguna.
==================================================
"""

# problem1

"""
Problem 1: Temperature converter

Description: The program receives a temperature in Celsius and converts it
to Fahrenheit and Kelvin. It also determines the boolean is_high_temperature,
which is true when the temperature is greater than or equal to 30.0 °C.
Physically impossible temperatures are rejected.

Inputs:
- temperature_n (string): temperature in °C entered with input(),
  converted to float in the variable temperature.

Outputs:
- "<temp_f> farenheit"
- "<temp_k> kelvin"
- "high temperature?<is_high_temperature>"
- "Fisically imposible, dummy" if the temperature is out of range.

Validations:
- temp_k must not be below 0.0 (absolute zero).
- temp_k must not be above plank_t (Planck temperature).

"""
#Captures the and checks temperature in celsius
temperature_n = input("enter the room temperature, (On Celsius): ")
temperature = float(temperature_n)

temperature = float(temperature_n)
#plank temperature
plank_t = (1.416784 * 10**32) 
# temperature covertions

temp_f = temperature * 9 / 5 + 32
 
temp_k = temperature + 273.15

is_high_temperature = (temperature >= 30.0)
if temp_k <0.0 or temp_k > plank_t:
    print("Fisically imposible, dummy")
else:

    print(f"high temperature?{is_high_temperature} ")
    print(f"{temp_f} farenheit")
    print(f"{temp_k} kelvin")

# problem2
# problem 2
"""
Problem 2: Weekly pay calculator

Description: The program calculates the total weekly pay of a worker. Hours
up to 40 are paid at hourly_rate, and overtime hours (more than 40) are paid
at 150% of the regular rate. It also determines the boolean has_overtime,
which is true when the worker did overtime.

Inputs:
- hours_worked (float): hours worked in the week, read with input().
- hourly_rate (float): pay per hour, read with input().

Outputs:
- "Regular pay: <regular_pay>"
- "Overtime pay: <overtime_pay>"
- "Total pay: <total_pay>"
- "Has overtime: true" or "Has overtime: false"
- "Error: invalid input" if the input fails the validations.

Validations:
- hours_worked and hourly_rate must be convertible to float.
- hours_worked must be >= 0.
- hourly_rate must be > 0.

Test cases:
1 Normal: hours_worked = "45", hourly_rate = "10"
   -> Regular pay: 400.00
      Overtime pay: 75.00
      Total pay: 475.00
      Has overtime: true

2 Border: hours_worked = "40", hourly_rate = "10" (exactly 40 hours)
   -> Regular pay: 400.00
      Overtime pay: 0.00
      Total pay: 400.00
      Has overtime: false

3 Error: hours_worked = "-5", hourly_rate = "10"
   -> Error: invalid input

   Another error case: hours_worked = "abc", hourly_rate = "10"
   -> Error: invalid input
"""
# Boolean interpretation:
# has_overtime = True  -> hours_worked is greater than 40
# has_overtime = False -> hours_worked is 40 or less

WEEKLY_HOURS = 40
OVERTIME_MULTIPLIER = 1.5

hours_worked = input("Enter worked hours: ")
hourly_rate = input("Enter the salary per hour: ")

try:
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)
except ValueError:
    print("Error: invalid input")
else:
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, WEEKLY_HOURS)
        overtime_hours = max(hours_worked - WEEKLY_HOURS, 0)

        # pay calculations
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > WEEKLY_HOURS

        print(f"Regular pay: {regular_pay:.2f}")
        print(f"Overtime pay: {overtime_pay:.2f}")
        print(f"Total pay: {total_pay:.2f}")
        print(f"Has overtime: {str(has_overtime).lower()}")
# problem3
"""
Problem 3: Discount eligibility with booleans

Description: The program determines whether a customer gets a 10% discount.
The customer is eligible if is_student is true, or is_senior is true, or
purchase_total is greater than or equal to 1000.0. It also calculates the
final total to pay.

Inputs:
- purchase_total (float): total of the purchase, read with input().
- is_student_text (string): "YES" or "NO", read with input().
- is_senior_text (string): "YES" or "NO", read with input().

Outputs:
- "Discount eligible: true" or "Discount eligible: false"
- "Final total: <final_total>"
- "Error: invalid input" if the input fails the validations.

Validations:
- purchase_total must be convertible to float and be >= 0.0.
- is_student_text and is_senior_text are normalized with strip() and
  upper(), and must be "YES" or "NO".

Test cases:
1 Normal: purchase_total = "500", is_student_text = "yes", is_senior_text = "no"
   -> Discount eligible: true
      Final total: 450.00

2 Border: purchase_total = "1000", is_student_text = "NO", is_senior_text = "NO"
   (exactly the limit, no student or senior)
   -> Discount eligible: true
      Final total: 900.00

   Other border: purchase_total = "999.99", is_student_text = "NO", is_senior_text = "NO"
   -> Discount eligible: false
      Final total: 999.99

3 Error: purchase_total = "500", is_student_text = "maybe", is_senior_text = "NO"
   -> Error: invalid input

   Another error case: purchase_total = "-10", is_student_text = "NO", is_senior_text = "NO"
   -> Error: invalid input
"""

# Boolean interpretation:
# is_student = True        -> the customer answered "YES" as a student
# is_senior = True         -> the customer answered "YES" as a senior
# discount_eligible = True -> at least one of the three conditions is met

DISCOUNT_LIMIT = 1000.0
DISCOUNT_MULTIPLIER = 0.9

# capture the inputs
purchase_input = input("Enter purchase total: ").strip()
is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

# Validation 1: purchase_total must be convertible to float
try:
    purchase_total = float(purchase_input)
except ValueError:
    print("Error: invalid input")
else:
    # Validation 2: purchase_total >= 0.0 and texts must be YES or NO
    if (purchase_total < 0.0
            or is_student_text not in ("YES", "NO")
            or is_senior_text not in ("YES", "NO")):
        print("Error: invalid input")
    else:
        # convert texts to booleans
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        # eligibility and final total
        discount_eligible = is_student or is_senior or (purchase_total >= DISCOUNT_LIMIT)

        if discount_eligible:
            final_total = purchase_total * DISCOUNT_MULTIPLIER
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total:.2f}")

# problem 4

"""
Problem 4: Three numbers statistics

Description: The program reads three integers and calculates their sum,
average (float), maximum and minimum values. It also determines the boolean
all_even, which is true when the three numbers are even.

Inputs:
- n1 (int): first integer, read with input().
- n2 (int): second integer, read with input().
- n3 (int): third integer, read with input().

Outputs:
- "Sum: <sum_value>"
- "Average: <average_value>"
- "Max: <max_value>"
- "Min: <min_value>"
- "All even: true" or "All even: false"
- "Error: invalid input" if the input fails the validation.

Validations:
- n1, n2 and n3 must be convertible to int.
- No additional restrictions (negative numbers are allowed).

Test cases:
1 Normal: n1 = "10", n2 = "20", n3 = "30"
   -> Sum: 60
      Average: 20.00
      Max: 30
      Min: 10
      All even: true

2 Border: n1 = "-2", n2 = "-4", n3 = "-6" (all negative)
   -> Sum: -12
      Average: -4.00
      Max: -2
      Min: -6
      All even: true

3 Error: n1 = "abc", n2 = "5", n3 = "7"
   -> Error: invalid input
"""

# Boolean interpretation:
# all_even = True  -> n1, n2 and n3 are all even numbers
# all_even = False -> at least one of them is odd

n1 = input("Enter the first integer: ")
n2 = input("Enter the second integer: ")
n3 = input("Enter the third integer: ")

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
except ValueError:
    print("Error: invalid input")
else:
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value:.2f}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

# problem 5

"""
Problem 5: Loan eligibility (income and debt ratio)

Description: The program determines whether a person is eligible for a loan.
It calculates debt_ratio (monthly_debt / monthly_income) and the person is
eligible if monthly_income is at least 8000.0, debt_ratio is at most 0.4
and credit_score is at least 650.

Inputs:
- monthly_income (float): monthly income, read with input().
- monthly_debt (float): monthly debt payments, read with input().
- credit_score (int): credit score, read with input().

Outputs:
- "Debt ratio: <debt_ratio>"
- "Eligible: true" or "Eligible: false"
- "Error: invalid input" if the input fails the validations.

Validations:
- monthly_income, monthly_debt and credit_score must be convertible
  (float, float and int).
- monthly_income must be > 0.0 (avoids division by zero).
- monthly_debt must be >= 0.0.
- credit_score must be >= 0.

Test cases:
1 Normal: monthly_income = "10000", monthly_debt = "3000", credit_score = "700"
   -> Debt ratio: 0.30
      Eligible: true

2 Border: monthly_income = "8000", monthly_debt = "3200", credit_score = "650"
   (exactly every limit: income 8000, ratio 0.4, score 650)
   -> Debt ratio: 0.40
      Eligible: true

   Other border: monthly_income = "10000", monthly_debt = "4001", credit_score = "700"
   -> Debt ratio: 0.40
      Eligible: false

3 Error: monthly_income = "0", monthly_debt = "100", credit_score = "700"
   -> Error: invalid input

   Another error case: monthly_income = "abc", monthly_debt = "100", credit_score = "700"
   -> Error: invalid input
"""

# Boolean interpretation:
# eligible = True  -> income >= 8000.0, debt_ratio <= 0.4 and credit_score >= 650
# eligible = False -> at least one of the three conditions is not met

monthly_income = input("Enter monthly income: ")
monthly_debt = input("Enter monthly debt payments: ")
credit_score = input("Enter credit score: ")

try:
    monthly_income = float(monthly_income)
    monthly_debt = float(monthly_debt)
    credit_score = int(credit_score)
except ValueError:
    print("Error: invalid input")
else:
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print(f"Debt ratio: {debt_ratio:.2f}")
        print(f"Eligible: {str(eligible).lower()}")

# problem 6

"""
Problem 6: Body Mass Index (BMI) and category flag

Description: The program calculates the Body Mass Index (BMI) of a person
with the formula weight_kg / (height_m * height_m). It also determines three
booleans: is_underweight (bmi < 18.5), is_normal (18.5 <= bmi < 25.0) and
is_overweight (bmi >= 25.0).

Inputs:
- weight_kg (float): weight in kilograms, read with input().
- height_m (float): height in meters, read with input().

Outputs:
- "BMI: <bmi_rounded>"
- "Underweight: true" or "Underweight: false"
- "Normal: true" or "Normal: false"
- "Overweight: true" or "Overweight: false"
- "Error: invalid input" if the input fails the validations.

Validations:
- weight_kg and height_m must be convertible to float.
- weight_kg must be > 0.0.
- height_m must be > 0.0.

Test cases:
1 Normal: weight_kg = "70", height_m = "1.75"
   -> BMI: 22.86
      Underweight: false
      Normal: true
      Overweight: false

2 Border: weight_kg = "56.25", height_m = "1.5" (BMI exactly 25.0)
   -> BMI: 25.0
      Underweight: false
      Normal: false
      Overweight: true

   Other border: weight_kg = "41.625", height_m = "1.5" (BMI exactly 18.5)
   -> BMI: 18.5
      Underweight: false
      Normal: true
      Overweight: false

3 Error: weight_kg = "70", height_m = "0"
   -> Error: invalid input

   Another error case: weight_kg = "abc", height_m = "1.75"
   -> Error: invalid input
"""

# Boolean interpretation:
# is_underweight = True -> bmi is less than 18.5
# is_normal = True      -> bmi is 18.5 or more, and less than 25.0
# is_overweight = True  -> bmi is 25.0 or more
# Only one of the three booleans can be true at the same time.

weight_kg = input("Enter weight in kg: ")
height_m = input("Enter height in meters: ")

try:
    weight_kg = float(weight_kg)
    height_m = float(height_m)
except ValueError:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")

# problem 6

"""
Problem 6: Body Mass Index (BMI) and category flag

Description: The program calculates the Body Mass Index (BMI) of a person
with the formula weight_kg / (height_m * height_m). It also determines three
booleans: is_underweight (bmi < 18.5), is_normal (18.5 <= bmi < 25.0) and
is_overweight (bmi >= 25.0).

Inputs:
- weight_kg (float): weight in kilograms, read with input().
- height_m (float): height in meters, read with input().

Outputs:
- "BMI: <bmi_rounded>"
- "Underweight: true" or "Underweight: false"
- "Normal: true" or "Normal: false"
- "Overweight: true" or "Overweight: false"
- "Error: invalid input" if the input fails the validations.

Validations:
- weight_kg and height_m must be convertible to float.
- weight_kg must be > 0.0.
- height_m must be > 0.0.

Test cases:
1 Normal: weight_kg = "70", height_m = "1.75"
   -> BMI: 22.86
      Underweight: false
      Normal: true
      Overweight: false

2 Border: weight_kg = "56.25", height_m = "1.5" (BMI exactly 25.0)
   -> BMI: 25.0
      Underweight: false
      Normal: false
      Overweight: true

   Other border: weight_kg = "41.625", height_m = "1.5" (BMI exactly 18.5)
   -> BMI: 18.5
      Underweight: false
      Normal: true
      Overweight: false

3 Error: weight_kg = "70", height_m = "0"
   -> Error: invalid input

   Another error case: weight_kg = "abc", height_m = "1.75"
   -> Error: invalid input
"""

# Boolean interpretation:
# is_underweight = True -> bmi is less than 18.5
# is_normal = True      -> bmi is 18.5 or more, and less than 25.0
# is_overweight = True  -> bmi is 25.0 or more
# Only one of the three booleans can be true at the same time.

weight_kg = input("Enter weight in kg: ")
height_m = input("Enter height in meters: ")

try:
    weight_kg = float(weight_kg)
    height_m = float(height_m)
except ValueError:
    print("Error: invalid input")
else:
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")

# Conclusiones 

"""

==================================================
CONCLUSIONS
==================================================
Integers and floats are used together in real calculations: int for
counters and scores (credit_score, n1, n2, n3) and float for money, hours
and measurements (hourly_rate, monthly_income, bmi), as in the average
sum_value / 3, which turns integers into a float. Comparisons such as
hours_worked > 40 or bmi < 18.5 produce booleans, and those booleans let
the program decide what to do with if/else. It is important to validate
ranges and avoid division by zero: checking monthly_income > 0.0 or
height_m > 0.0 before dividing prevents crashes and meaningless results.
I learned to combine conditions with and, or and not: "and" requires all
conditions (loan eligibility), "or" requires at least one (discounts),
and a wrong choice, like using "and" instead of "or", lets invalid data
through. These patterns repeat in payroll, discounts, loans and BMI.

"""

# Referencias 

"""

==================================================
REFERENCES
==================================================
1) Python Documentation - Built-in Types: Numeric Types - int, float,
   complex
   https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

2) Python Documentation - Built-in Types: Boolean Type - bool
   https://docs.python.org/3/library/stdtypes.html#boolean-type-bool

3) Python Documentation - Boolean Operations (and, or, not) and
   Comparisons
   https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

4) Python Tutorial - An Informal Introduction to Python: Using Python as
   a Calculator (numbers and arithmetic operators)
   https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

5) Python Tutorial - Errors and Exceptions (try/except, used to validate
   numeric input)
   https://docs.python.org/3/tutorial/errors.html

6) Sweigart, A. (2019). Automate the Boring Stuff with Python, 2nd ed.
   No Starch Press. Chapter 2: Flow Control.

"""