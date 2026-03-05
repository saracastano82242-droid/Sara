def fibonancci(n): # Función recursiva para calcular el número de Fibonacci
    if n <= 1: # Caso base: si n es 0 o 1, el número de Fibonacci es igual a n
        return n # Retorna n para los casos base
    else:
        return fibonancci(n - 1) + fibonancci(n - 2) # Llamada recursiva para calcular el número de Fibonacci
# Ejemplo de uso    

print(fibonancci(5))
print(fibonancci(10))

#otro ejemplo de Fibonacci
def fibonacci(n):
#Calcula el n-ésimo número de Fibonacci."""
# Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1
# Caso recursivo (dos llamadas)
    return fibonacci(n - 1) + fibonacci(n - 2)
# Prueba
for i in range(10):
    print(fibonacci(i), end=" ")
# Salida: 0 1 1 2 3 5 8 13 21 34

# Ejemplo de uso
print(fibonacci(5)) # Imprime el 5to número de Fibonacci
print(fibonacci(10)) # Imprime el 10mo número de Fibonacci
