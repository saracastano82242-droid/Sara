#tarea de validar un correo
import re
def validar_correo(correo):
	
	patron_valido = re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", correo) #Guarda la expresión regular que valida el correo.
	return bool(patron_valido)

correo = input("Ingrese un correo: ")
print(f"¿es valido?: {validar_correo(correo)}")

"""
^ → inicio del texto

[\w.-]+ → letras, números, puntos o guiones antes del @

@ → símbolo obligatorio del correo

[\w.-]+ → nombre del dominio

\. → punto antes del dominio final

\w+ → extensión del dominio (com, org, edu, etc.)

$ → final del texto

"""