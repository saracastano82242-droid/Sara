#codigo para validar un numero de celular
import re

3147249070
311-628-9027

def validar_celular(numero):
    telefono_valido = re.match(r"^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$", numero)#El patrón de expresión regular ^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2} 
    #se utiliza para validar números de celular en el formato colombiano. Aquí está la explicación del patrón:
    return bool (telefono_valido)

print(validar_celular("311-5523"))
print(validar_celular("21615016516"))

#codigo para validar una fecha
"12/03/2026"
def validar_fecha(fecha):
    fecha_valida = re.match(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20\d{2}$)",fecha)#estamos validando el dia
    #[-/](1[1-9]|2[0-9]): sirve para validar solo los dos ultimos dijitos del año "26"
    return bool(fecha_valida)

print(validar_fecha("12/03/2026"))

"""
TAREA:
hacer un codigo que valide si una contraseña es valida, que tenga caracteres "*,_,-,.,N.n"
"""
def validar_contraseña(contraseña):
    # Explicación del regex r"^[a-zA-Z0-9*_\-.]+ $":
    # ^ y $ : Inicio y fin de la cadena.
    # [a-zA-Z0-9*_\-.] : Permite letras, números y los caracteres *, _, -, .
    # + : Asegura que al menos haya un caracter y no esté vacía.
    
    patron = r"^[a-zA-Z0-9*_\-.]+$"
    
    contraseña_valida = re.match(patron, contraseña)
    return bool(contraseña_valida)

# Pruebas
print(f"¿Es válida: Contra_123* ? \n {validar_contraseña('Contra_123*')}") 
print(f"¿Es válida: Clave-45 ? \n{validar_contraseña('Clave-45')}")      
print(f"¿Es válida: 103625.Sa ? \n{validar_contraseña('103625.Sa')}")      # False (tiene espacio)
print(f"¿Es válida: 'Akira@!' ? \n{validar_contraseña('Akira@!')}")        # False (caracteres no permitidos)
