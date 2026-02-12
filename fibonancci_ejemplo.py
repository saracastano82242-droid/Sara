def fibonancci(n):
    if n <= 1:
        return n
    else:
        return fibonancci(n - 1) + fibonancci(n - 2)
# Ejemplo de uso    

print(fibonancci(5))
print(fibonancci(10))