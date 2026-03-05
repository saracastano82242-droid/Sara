def infija_a_postfija(expresion):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    salida = []
    pila = []
    
    for token in expresion.split():
        if token.isalnum():  # Si el token es un operando (número o variable)
            salida.append(token)
        elif token in precedencia:  # Si el token es un operador
            while (pila and pila[-1] != '(' and
                   precedencia[pila[-1]] >= precedencia[token]):
                salida.append(pila.pop())
            pila.append(token)
        elif token == '(':  # Si el token es un paréntesis de apertura
            pila.append(token)
        elif token == ')':  # Si el token es un paréntesis de cierre
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar el paréntesis de apertura
    
    while pila:  # Vaciar la pila al final
        salida.append(pila.pop())
    
    return ' '.join(salida)

def evaluar_postfija(expresion):
    pila = []
    
    for token in expresion.split():
        if token.isdigit():  # Si el token es un número
            pila.append(int(token))
        else:  # Si el token es un operador
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
    
    return pila[0]  # El resultado final estará en la cima de la pila
# Ejemplo de uso
expresion_infija = "3 + 4 * 2 / ( 1 - 5 )"
expresion_postfija = infija_a_postfija(expresion_infija)
print("Expresión infija:", expresion_infija)
print("Expresión postfija:", expresion_postfija)
resultado = evaluar_postfija(expresion_postfija)
print("Resultado de la evaluación:", resultado)
