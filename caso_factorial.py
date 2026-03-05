def caso_factorial(n,):
    if n == 0: #condicion de parada
        return 1
    else:
        return n * caso_factorial(n - 1) #llamada recursiva con n-1 para acercarnos a la condicion base
    
    #caso base: factorial(0) = 1, factorial(1) = 1
    #caso recursivo: factorial(n) = n * factorial(n-1)

    
print(caso_factorial(8))

#otro ejemplo de factorial
def factorial(n):
#Calcula n! de forma recursiva."""
# Caso base
    if n <= 1:
        return 1
# Caso recursivo
    return n * factorial(n - 1)
# Ejemplo de ejecución:
# factorial(4)
# = 4 * factorial(3)
# = 4 * (3 * factorial(2))
# = 4 * (3 * (2 * factorial(1)))
# = 4 * (3 * (2 * 1))
# = 4 * (3 * 2) = 4 * 6 = 24