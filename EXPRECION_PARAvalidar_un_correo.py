import re

correo = input("Ingrese un correo: ")

patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(patron, correo):
    print("Correo válido")
else:
    print("Correo inválido")