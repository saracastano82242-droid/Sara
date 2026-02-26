class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    #ingresando valores a la pila con un operador de suma
    def __init__(self, suma=0):
        self.suma = suma
        self.elementos = []
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def operadores_suma(self, valor):
        self.suma += valor
    
    def push(self, elemento):
        self.elementos.append(elemento)
        self.suma += elemento

    def pop(self):
        if not self.esta_vacia():
            elemento = self.elementos.pop()
            self.suma -= elemento
            return elemento
        raise IndexError("La pila está vacía")

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        raise IndexError("La pila está vacía")

    def size(self):
        return len(self.elementos) 
# Ejemplo de uso
pila = Pila()
pila.push(3)
pila.push(4)
pila.push(2)
print(pila.suma)  # Imprime 10 (3 + 4 + 2)

print(pila.pop())  # Imprime 3
print(pila.peek()) # Imprime 4
print(pila.size()) # Imprime 2
print(pila.suma)  # Imprime 7 (4 + 2)

#correccion del ejercicio de la pila con operadores de suma, ahora se actualiza la suma cada vez que se agrega o se elimina un elemento de la pila.

def evaluar_postfija(expresion):
    pila = Pila()
    
    for token in expresion.split():
        if token.isdigit():  # Si el token es un número, lo agregamos a la pila #isdiigt verifica si el token es un dígito (número) antes de agregarlo a la pila
            pila.push(int(token))
        else:  # Si el token es un operador, aplicamos la operación a los dos últimos números en la pila
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                resultado = a / b
            else:
                raise ValueError(f"Operador desconocido: {token}")
            pila.push(resultado)  # Agregamos el resultado de la operación de vuelta a la pila
    return pila.pop()  # El resultado final estará en la cima de la pila
# Ejemplo de uso
expresion = "3 4 2 * 1 5 - 2 3  / +"
resultado = evaluar_postfija(expresion)
print(resultado)  # Imprime el resultado de la expresión postfija
