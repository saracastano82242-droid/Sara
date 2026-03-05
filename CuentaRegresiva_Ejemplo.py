def cuenta_regresiva(n):
#Imprime números de n hasta 1.

    if n <= 0: # CASO BASE
        print("¡Despegue!")
        return
    print(n) # Acción
    cuenta_regresiva(n - 1) # CASO RECURSIVO (n se reduce)
# Llamada
cuenta_regresiva(5) 

# Salida: 5, 4, 3, 2, 1, ¡Despegue!