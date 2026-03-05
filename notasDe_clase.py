#lifo: ultimo en entrar, primero en salir
#ejemplo de lifo: una pila de platos, una pila de libros, una pila de papeles, una pila de cartas, una pila de documentos, una pila de archivos, una pila de objetos, una pila de elementos, etc.
#fifo: primero en entrar, primero en salir
#ejemplo de fifo: una fila de personas, una fila de coches, una fila de clientes, una fila de mensajes, una fila de eventos, una fila de procesos, una fila de hilos (threads), una fila de recursos, una fila de errores, una fila de eventos pendientes, etc.

#front: el primer elemento de la cola
#ejemplo de front: el primer cliente en la fila, el primer mensaje en la bandeja de entrada, el primer evento en la cola de eventos, el primer proceso en la cola de procesos, el primer hilo (thread) en la cola de hilos, el primer recurso en la cola de recursos, el primer error en la cola de errores, el primer evento pendiente en la cola de eventos pendientes, etc.
#back: el último elemento de la cola
#ejemplo de back: el último cliente en la fila, el último mensaje en la bandeja de entrada, el último evento en la cola de eventos, el último proceso en la cola de procesos, el último hilo (thread) en la cola de hilos, el último recurso en la cola de recursos, el último error en la cola de errores, el último evento pendiente en la cola de eventos pendientes, etc.

#notacion postfija: el operador se coloca después de los operandos (ejemplo: 3 4 + en lugar de 3 + 4)
#notacion infija: el operador se coloca entre los operandos (ejemplo: 3 + 4)
#notacion prefija: el operador se coloca antes de los operandos (ejemplo: + 3 4)

#append: agregar un elemento al final de una lista
#pop: eliminar y retornar el último elemento de una lista
#empyt: verificar si una lista está vacía
#len: obtener la longitud de una lista
#peek: obtener el último elemento de una lista sin eliminarlo
#size: obtener el número de elementos en una lista
#enqueue: agregar un elemento al final de una cola
#dequeue: eliminar y retornar el primer elemento de una cola
#push: agregar un elemento al tope de una pila
#rize: eliminar y retornar el elemento en el tope de una pila
#lambda: función anónima, es decir, una función sin nombre que se define en una sola línea utilizando la palabra clave "lambda" (ejemplo: lambda x: x + 1)


#implementacion de una pila utilizando una lista
"""
class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return self.tope is None
    
    def push(self, elemento): #Agrega un elemento a la pila
        self.elementos.append(elemento) # Agrega un elemento al final de la lista, que representa el tope de la pila
    
    def pop(self): #Elimina y retorna el elemento en el tope de la pila
        if not self.is_empty(): # Verifica si la pila no está vacía antes de intentar eliminar un elemento
            return self.elementos.pop()
        raise IndexError("La pila está vacía")
    
    def peek(self): #Retorna el elemento en el tope de la pila sin eliminarlo
        if not self.is_empty(): # Verifica si la pila no está vacía antes de intentar acceder al elemento en el tope
            return self.elementos[-1]
        raise IndexError("La pila está vacía")
    
    def is_empty(self): # Verifica si la pila está vacía
        return len(self.elementos) == 0 # Retorna True si la longitud de la lista es 0, lo que indica que la pila está vacía
    
    def size(self): # Retorna el número de elementos en la pila
        return len(self.elementos) # Retorna la longitud de la lista, que representa el número de elementos en la pila
# Ejemplo de uso
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.pop())  # Imprime 3
print(pila.peek()) # Imprime 2
print(pila.size()) # Imprime 2
print(pila.is_empty()) # Imprime False


"""

#solid: Responsabilidad única, open/close, sustitución de Liskov, segregación de interfaz, inversión de dependencia

#TAREA: investigar: algoritmo Shunting Yard, algoritmo ( Dijkstra, 1967) para convertir expresiones infijas a postfijas y evaluar expresiones postfijas utilizando una pila.
#teniendo encuenta que estos tienen parentesis, operadores de suma, resta, multiplicacion y division, y numeros enteros. EXPLICAR EL ALGORITMO Y MOSTRAR UN EJEMPLO DE CÓDIGOS EN PYTHON PARA CONVERTIR UNA EXPRESIÓN INFIX A POSTFIX Y EVALUARLA.

#05/03/2026
#lstrip: eliminar los caracteres en blanco al inicio de una cadena
#rstrip: eliminar los caracteres en blanco al final de una cadena
#strip: eliminar los caracteres en blanco al inicio y al final de una cadena
#split: dividir una cadena en una lista de subcadenas utilizando un separador (ejemplo: "hola mundo".split() devuelve ["hola", "mundo"])
#join: unir una lista de cadenas en una sola cadena utilizando un separador (ejemplo: " ".join(["hola", "mundo"]) devuelve "hola mundo")
#replace: reemplazar una subcadena por otra en una cadena (ejemplo: "hola mundo".replace("mundo", "python") devuelve "hola python")
#isdigit: verificar si una cadena es un número entero (ejemplo: "123".isdigit() devuelve True, mientras que "abc".isdigit() devuelve False)

#para yo encontrar un elemento en una lista tengo que recorrer toda la lista, lo que tiene una complejidad de O(n), donde n es el número de elementos en la lista. Si el elemento se encuentra al final de la lista, tendré que recorrer toda la lista para encontrarlo. Si el elemento no se encuentra en la lista, también tendré que recorrer toda la lista para verificar que no está presente. Por lo tanto, la complejidad de buscar un elemento en una lista es O(n).
#para yo encontar un elemento en una pila tengo que recorrer toda la pila, lo que tiene una complejidad de O(n), donde n es el número de elementos en la pila. Si el elemento se encuentra al final de la pila, tendré que recorrer toda la pila para encontrarlo. Si el elemento no se encuentra en la pila, también tendré que recorrer toda la pila para verificar que no está presente. Por lo tanto, la complejidad de buscar un elemento en una pila es O(n).

#heap: estructura de datos que permite almacenar elementos de manera eficiente, donde el elemento con la mayor prioridad se encuentra en la raíz del heap. 
# Un heap puede ser un max-heap (donde el elemento con la mayor prioridad es el máximo) o un min-heap (donde el elemento con la mayor prioridad es el mínimo). Los heaps se utilizan comúnmente para implementar colas de prioridad y algoritmos de ordenamiento como heapsort.

#esta es la libreria para importar el heap en python

import heapq
def demo_operaciones_basicas():
    print("="*35)
    print("Operaciones básicas con heapq")
    print("="*35)

    print("\n1. crear un heap(heapify):")
    print("-"*38)
    datos = [5, 3, 8, 1, 2]
    print(f"Datos originales: {datos}")

    heapq.heapify(datos)
    print(f"Heap después de heapify: {datos}")

#ejemplo de uso
demo_operaciones_basicas()


