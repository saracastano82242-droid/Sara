#ejemplo de clase de algoritmo de Fibonacci con lista
def cambio(cantidad, monedas):
    """Calcula el número mínimo de monedas necesarias para dar el cambio."""
    if cantidad == 0: # Caso base: si la cantidad es 0, no se necesitan monedas
        return 0
    if cantidad < 0: # Caso base: si la cantidad es negativa, no es posible dar cambio
        return float('inf') # No es posible dar cambio negativo
    min_monedas = float('inf') # Inicializa el número mínimo de monedas como infinito

    for moneda in monedas: # Itera sobre cada tipo de moneda disponibles
        resultado = cambio(cantidad - moneda, monedas) # Llamada recursiva para calcular el número de monedas necesarias para la cantidad restante después de usar una moneda
        if resultado != float('inf'): # Si el número de monedas no es infinito, actualiza el número mínimo de monedas
            min_monedas = min(min_monedas, resultado + 1) # Compara el número mínimo de monedas actual con el número de monedas calculado en la llamada recursiva más una moneda adicional (la moneda que se acaba de usar)
    return min_monedas # Retorna el número mínimo de monedas necesarias para dar el cambio de la cantidad dada con las monedas disponibles
# Ejemplo de uso
monedas = [1, 78, 20, 25] # Lista de monedas disponibles para dar el cambio
cantidad = 6 # Cantidad para la cual se desea calcular el cambio
print(cambio(cantidad, monedas)) # Imprime el número mínimo de monedas para dar el cambio de 6 con las monedas disponibles

def cambio_memo(cantidad, monedas, memo={}):
    """Calcula el número mínimo de monedas necesarias para dar el cambio usando memoización."""
    if cantidad in memo: # Verifica si el resultado para la cantidad ya está en el diccionario de memoización
        return memo[cantidad] # Retorna el resultado almacenado en el diccionario de memoización
    
    if cantidad == 0: # Caso base: si la cantidad es 0, no se necesitan monedas
        return 0
    if cantidad < 0: # Caso base: si la cantidad es negativa, no es posible dar cambio
        return float('inf') # No es posible dar cambio negativo
        
    min_monedas = float('inf') # Inicializa el número mínimo de monedas como infinito

    for moneda in monedas: # Itera sobre cada tipo de moneda disponibles
        resultado = cambio_memo(cantidad - moneda, monedas, memo) # type: ignore # Llamada recursiva para calcular el número de monedas necesarias para la cantidad restante después de usar una moneda, pasando el diccionario de memoizaciónmin_monedas = min(min_monedas, resultado + 1) # Compara el número mínimo de monedas actual con el número de monedas calculado en la llamada recursiva más una moneda adicional (la moneda que se acaba de usar)
        min_monedas = min(min_monedas, resultado + 1) # Compara el número mínimo de monedas actual con el número de monedas calculado en la llamada recursiva más una moneda adicional (la moneda que se acaba de usar)

    memo[cantidad] = min_monedas # type: ignore # Almacena el resultado calculado en el diccionario de memoización para la cantidad dada
    return min_monedas # type: ignore # Retorna el número mínimo de monedas necesarias para dar el cambio de la cantidad dada con las monedas disponibles usando memoización  

# Ejemplo de uso
monedas = [1, 78, 20, 25] # Lista de monedas
cantidad = 6 # Cantidad para la cual se desea calcular el cambio
print(cambio_memo(cantidad, monedas)) # Imprime el número mínimo de monedas para dar el cambio de 6 con las monedas disponibles usando memoización
