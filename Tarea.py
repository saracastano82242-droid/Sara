def validar_expresion(expresion):
    pila = [] # Pila para almacenar los paréntesis de apertura
    simbolos = {'(': ')', '{': '}', '[': ']'}

    for char in expresion:

        if char in simbolos:  # Paréntesis de apertura
            pila.append(char)

        elif char in simbolos.values():  # Paréntesis de cierre
            if not pila:
                return False

            ultimo_simbolo = pila.pop()

            if simbolos[ultimo_simbolo] != char:
                return False

    return len(pila) == 0


# ----- Programa interactivo -----
while True:

    print("\n--- VALIDADOR DE EXPRESIONES ---")
    print("1. Validar una expresión")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        expresion = input("Ingrese la expresión que desea validar:\n")

        if validar_expresion(expresion):
            print("✅ La expresión es válida.")
        else:
            print("❌ La expresión no es válida.")
        

    elif opcion == "2":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida, intente nuevamente.")
