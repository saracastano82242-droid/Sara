def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b - 1)

def potencia_optimizado(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        mitad = potencia_optimizado(a, b//2)
        return mitad *  mitad
    else:
        return a * potencia_optimizado (a, b - 1)
def sumar_digitos(n):
    if n < 10:
        return n
    digito = n % 10
    return digito + sumar_digitos(n//10) 