def validar_expresion(expresion):
    pila = []
    pares_parentesis = {'(': ')', '{': '}', '[': ']'}

    for char in expresion:

        if char in pares_parentesis:  # Paréntesis de apertura
            pila.append(char)

        elif char in pares_parentesis.values():  # Paréntesis de cierre
            if not pila:
                return False

            ultimo_parentesis = pila.pop()

            if pares_parentesis[ultimo_parentesis] != char:
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
