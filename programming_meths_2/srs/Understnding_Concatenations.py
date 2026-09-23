#Conbinación o concatenación de strings
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)
print(full_name. title())
print(full_name.upper())
print("hola". upper(),first_name + " " + last_name)

# Whitespace

"""
    whitespace se refiere a cualquier espcio 
    que no se imprime, es decir, un espacio ( )
    tabuladores(\t) y g¿fianles de linea (\n)
    
    """

print("\tPython")
print("\t\tPython")
print("lenguajes:\n\tPython\nC\nJavaScript")

# F-strings
charly_is_true = "Six seven"
famous_person = "charly mercury"
message = F" {famous_person.upper()} una vez dijo: python is love {charly_is_true}"
print(message)
