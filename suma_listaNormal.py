def suma_lista_normal(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista_normal(lista[1:])

def suma_lista_tall(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista_tall(lista[1:], acumulador + lista[0])
# Ejemplo de uso
print(suma_lista_normal([1, 2, 3, 4, 5]))
print(suma_lista_tall([8, 2, 5, 9, 1]))
