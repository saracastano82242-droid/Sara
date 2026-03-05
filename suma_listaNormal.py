def suma_lista_normal(lista): # Función recursiva para sumar los elementos de una lista utilizando recursión normal
    if len(lista) == 0: # Caso base: si la lista está vacía, la suma es 0
        return 0
    return lista[0] + suma_lista_normal(lista[1:]) # Llamada recursiva para sumar el primer elemento de la lista con la suma del resto de la lista

def suma_lista_tall(lista, acumulador=0): # Función recursiva para sumar los elementos de una lista utilizando recursión de cola (tail recursion)
    if len(lista) == 0: # Caso base: si la lista está vacía, se retorna el acumulador que contiene la suma total
        return acumulador # Retorna el acumulador con la suma total
    return suma_lista_tall(lista[1:], acumulador + lista[0]) # Llamada recursiva para sumar el primer elemento de la lista al acumulador y continuar con el resto de la lista

# Ejemplo de uso
print(suma_lista_normal([1, 2, 3, 4, 5]))
print(suma_lista_tall([8, 2, 5, 9, 1]))

def potencia_normal(base, exponente): # Función recursiva para calcular la potencia de un número utilizando recursión normal
    if exponente == 0: # Caso base: cualquier número elevado a la potencia de 0 es 1
        return 1
    return base * potencia_normal(base, exponente - 1) # Llamada recursiva para multiplicar la base por la potencia de la base con el exponente reducido en 1

def potencia_tall(base, exponente, acumulador=1): # Función recursiva para calcular la potencia de un número utilizando recursión de cola (tail recursion)
    if exponente == 0: # Caso base: cualquier número elevado a la potencia de 0 es 1, se retorna el acumulador que contiene el resultado final
        return acumulador # Retorna el acumulador con el resultado final
    return potencia_tall(base, exponente - 1, acumulador * base) # Llamada recursiva para multiplicar la base al acumulador y continuar con el exponente reducido en 1

#acumulador: es una variable que se utiliza para almacenar el resultado parcial de la potencia a medida que se va calculando. En cada llamada recursiva, el acumulador se multiplica por la base, y cuando el exponente llega a 0, el acumulador contiene el resultado final de la potencia.
# Ejemplo de uso
print(potencia_normal(2, 5))
print(potencia_tall(3, 4))

def invertir_lista_normal(lista): # Función recursiva para invertir una lista utilizando recursión normal
    if len(lista) == 0: # Caso base: si la lista está vacía, se retorna una lista vacía
        return [] # Retorna una lista vacía
    return [lista[-1]] + invertir_lista_normal(lista[:-1]) # Llamada recursiva para agregar el último elemento de la lista al resultado de invertir el resto de la lista

def invertir_lista_tall(lista, acumulador=[]): # Función recursiva para invertir una lista utilizando recursión de cola (tail recursion)
    if len(lista) == 0: # Caso base: si la lista está vacía, se retorna el acumulador que contiene la lista invertida
        return acumulador # Retorna el acumulador con la lista invertida
    return invertir_lista_tall(lista[:-1], acumulador + [lista[-1]]) # Llamada recursiva para agregar el último elemento de la lista al acumulador y continuar con el resto de la lista
# Ejemplo de uso
print(invertir_lista_normal([1, 2, 3, 4, 5]))
print(invertir_lista_tall([8, 2, 5, 9, 1]))