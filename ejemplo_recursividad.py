#invertir un string usando recursividad
#hola -> aloh

def invertir_string(s):
    if len(s) <= 0:
        return s
    return invertir_string(s[1:]) + s[0]

# Ejemplo de uso
cadena = "reconocer"
cadena_invertida = invertir_string(cadena)
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {cadena_invertida}")
