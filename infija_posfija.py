def infija_a_postfija(expresion):
    precedencia = {'+': 1, 
                '-': 1,
                '*': 2, 
                '/': 2} # Define la precedencia de los operadores, donde '*' y '/' tienen una precedencia mayor que '+' y '-' siendo asi un diccionario que asigna un valor numérico a cada operador para indicar su precedencia en la evaluación de la expresión. En este caso, '*' y '/' tienen una precedencia de 2, mientras que '+' y '-' tienen una precedencia de 1. Esto se utiliza para determinar el orden en el que se deben evaluar los operadores al convertir una expresión infija a postfija.
    tokens = expresion.split() # Divide la expresión infija en tokens utilizando el espacio como delimitador
    salida = []
    pila = []
    
    for token in tokens: # type: ignore
        if token.isdigit():  # Si el token es un número
            salida.append(token)
            print(f" '{token}' (numero) -> salida")
        elif token == '(':  # Si el token es un paréntesis izquierdo
            pila.append(token)
            print(f" '{token}' (parentesis izquierdo) -> pila")
        elif token == ')':  # Si el token es un paréntesis derecho
            while not pila.esta_vacia() and pila.peek() != '(': #sirve para asegurarse de que se sigan procesando los operadores en la pila hasta que se alcance el paréntesis izquierdo correspondiente
                salida.append(pila.pop()) # El método pop() se utiliza para eliminar y retornar el último elemento de la pila, que es el operador que se va a agregar a la salida
            pila.pop()  # Eliminar el paréntesis izquierdo de la pila
            print(f" '{token}' -> pop hasta encontrar '('")
        elif token in precedencia:  # Si el token es un operador
            while (not pila.esta_vacia() and pila.peek() != '(' and pila.peek() in precedencia and precedencia[pila.peek()] >= precedencia[token]): # Verifica si la pila no está vacía, si el operador en la cima de la pila no es un paréntesis izquierdo y si la precedencia del operador en la cima de la pila es mayor o igual a la precedencia del operador actual
                salida.append(pila.pop()) # Si se cumplen las condiciones anteriores, se elimina el operador de la cima de la pila y se agrega a la salida
            pila.push(token) # Agrega el operador actual a la pila
            print(f" '{token}' (operador) -> pila") # Imprime el operador actual y su acción (agregar a la pila)

    while not pila.esta_vacia(): # Después de procesar todos los tokens, se verifica si aún quedan operadores en la pila
        salida.append(pila.pop()) # Si la pila no está vacía, se eliminan los operadores restantes de la pila y se agregan a la salida
    resultado = ' '.join(salida) # Une los elementos de la salida en una cadena separada por espacios
    print(f"exprecion postfija final: {resultado}") # Imprime la expresión postfija resultante


#ejemplo de uso
expresion_infija = "3 + 4 * 2 / ( 1 - 5 )"
expresion_postfija = infija_a_postfija(expresion_infija)
print("Expresión infija:", expresion_infija)
print("Expresión postfija:", expresion_postfija)


