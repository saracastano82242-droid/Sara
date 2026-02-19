def fibonancci_normal(n):
    return fibonancci_normal(n - 1) + fibonancci_normal(n - 2)

def fibonancci_tall(n, actual=0, siguiente=1):
    """Función recursiva para calcular el número de Fibonacci utilizando recursión de cola (tail recursion).
    En esta función, 'actual' representa el número de Fibonacci actual y 'siguiente'
    representa el siguiente número de Fibonacci. La función se llama a sí misma con los valores actualizados
    hasta que n llegue a 0, momento en el cual se retorna el número de Fibonacci
    correspondiente.

    Args:
        n (int): El índice del número de Fibonacci a calcular.
        actual (int, optional): El número de Fibonacci actual. Por defecto es 0.
        siguiente (int, optional): El siguiente número de Fibonacci. Por defecto es 1.
    Returns:
        int: El número de Fibonacci correspondiente al índice n.
    """
    if n == 0:
        return actual
    return fibonancci_tall(n - 1, siguiente, actual + siguiente)
# Ejemplo de uso
import time
start_time = time.time()
print(fibonancci_tall(30))
print(fibonancci_tall(40))
end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
