def fibonancci(n): # Función recursiva para calcular el número de Fibonacci
    if n <= 1: # Caso base: si n es 0 o 1, el número de Fibonacci es igual a n
        return n # Retorna n para los casos base
    else:
        return fibonancci(n - 1) + fibonancci(n - 2) # Llamada recursiva para calcular el número de Fibonacci
# Ejemplo de uso    

print(fibonancci(5))
print(fibonancci(10))