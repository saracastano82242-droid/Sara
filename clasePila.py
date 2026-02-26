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
    
    def operador_suma(self, valor):
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