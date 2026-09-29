# Numbers
# Enteros + Integers
"""
     Los numeros enteros los podemos
    sumar (+), restar (-), multiplicar(*) y 
    dividir(/), Division entera(//), Potencia(**), Modulo(%)
"""
print(2+4)
print(2-4)
print(2*4)
print(2/4)
print(2//3)
print(2**3)
print(15%2)
number_1 = 5
number_2 = 10
number_3 = (number_1+number_2)
number_4 = (number_1/number_2)

age = 67

print(0.1 + 0.1)
print(0.2 - 0.2)
print(2*0.1)
print(2 + 0.1)
# Imprimir la edad de alguien
age = 34 # Variable del tipo int
# message = "charly tiene" + " " + age + " " + "años."(ERROR)
#print(message)
#(CORRECTO)
# STR convierte otras variables a strings, como las vriables numéricas.
message = "charly tiene" + " " + str(age) + " " + "años."
print(message)
message_f = f"charly tiene {age} años."
print(message_f)
#TYPE ERROR
"""
Type error es cuando python no puede reconocer la 
variable que estan usando"""
#Metodo build-in type()
print(type(message_f), type("hola"), type(0.54), type(True)) 