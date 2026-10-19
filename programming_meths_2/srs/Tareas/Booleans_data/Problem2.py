# problem 2
"""
Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano 
has_overtime que indique si el trabajador hizo horas extra.

Entradas:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Salidas:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Operaciones clave sugeridas:
- Uso de min() y max() para separar horas regulares y extra.
- Cálculo: overtime_pay = overtime_hours * hourly_rate * 1.5
- Booleano: has_overtime = (hours_worked > 40)
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