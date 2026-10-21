guisos = ["salsa verde", "deshebrada", "nopales"]

if "salsa verde" in guisos:
    print("si hay")
elif "desebrada" in guisos:
    print("si hay")
elif "nopales" in guisos:
    print("si hay")
else:
    print("no hay")

# listr vacía 

guisos_2 = ["salsa verde", "picadillo" "asado"]

if guisos_2:
    for guiso in guisos_2:
        print(guiso)
    else: 
        print("no hay guiso")
guisos_disponibles = ["salsa verde", "deshebrada", "picadillo", "asado"]
guisos_NO_disponibles = ["barbacoa", "deshebrada", "cabrito"]

for guiso in guisos_disponibles:
    print(f"si tenemos del guiso de:{guiso}")
else:
    print(f"no tenemos {guiso}, una disculpo")
    print(f"¿NO VIÓ EL MENU O QUÉ?")