def fibonancci(n):
    """Calcula el n-ésimo número de Fibonacci."""
    # Casos base
    if n <= 1:
        return n
    # Caso recursivo (dos llamadas)
    return fibonancci(n - 1) + fibonancci(n - 2)
# Ejemplo de uso
print(fibonancci(5)) # Imprime el 5to número de Fibonacci
print(fibonancci(10)) # Imprime el 10mo número de Fibonacci

def fibonacci_memo(n, cache={}):
    """Calcula el n-ésimo número de Fibonacci usando memoización para optimizar."""
    # Casos base
    if n <= 1:
        return n
    # Verificar si el resultado ya está en cache
    if n in cache:
        return cache[n]
    # Caso recursivo con memoización
    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]
# Ejemplo de uso
print(fibonacci_memo(5)) # Imprime el 5to número de Fibonacci
print(fibonacci_memo(10)) # Imprime el 10mo número de Fibonacci

def fibonacci_iterativo(n):
    """Calcula el n-ésimo número de Fibonacci de forma iterativa."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
# Ejemplo de uso
print(fibonacci_iterativo(5)) # Imprime el 5to número de Fibonacci
print(fibonacci_iterativo(10)) # Imprime el 10mo número de Fibonacci

def fibonacci_clase(n):
    """Calcula el n-ésimo número de Fibonacci usando una clase para almacenar resultados."""
    class FibonacciCache:
        def __init__(self):
            self.cache = {0: 0, 1: 1}
        
        def fib(self, n):
            if n in self.cache:
                return self.cache[n]
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.cache[n]
    
    fib_cache = FibonacciCache()
    return fib_cache.fib(n)
# Ejemplo de uso
print(fibonacci_clase(5)) # Imprime el 5to número de Fibonacci
print(fibonacci_clase(10)) # Imprime el 10mo número de Fibonacci

def fibonancci_lista(n):
    """Calcula el n-ésimo número de Fibonacci usando una lista para almacenar resultados."""
    if n <= 1:
        return n
    fibs = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]
# Ejemplo de uso
print(fibonancci_lista(5)) # Imprime el 5to número de Fibonacci
print(fibonancci_lista(10)) # Imprime el 10mo número de Fibonacci

def fibonacci_lista_optimizada(n):
    """Calcula el n-ésimo número de Fibonacci usando una lista optimizada para reducir espacio."""
    if n <= 1:
        return n
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
        fibs.pop(0) # Mantener solo los últimos dos números en la lista
    return fibs[-1]

# Ejemplo de uso
print(fibonacci_lista_optimizada(5)) # Imprime el 5to número de Fibonacci
print(fibonacci_lista_optimizada(10)) # Imprime el 10mo número de Fibonacci