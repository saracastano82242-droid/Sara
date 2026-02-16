def caso_factorial(n,):
    if n == 0: #condicion de parada
        return 1
    else:
        return n * caso_factorial(n - 1) #llamada recursiva con n-1 para acercarnos a la condicion base
    
    #caso base: factorial(0) = 1, factorial(1) = 1
    #caso recursivo: factorial(n) = n * factorial(n-1)

    
print(caso_factorial(8))