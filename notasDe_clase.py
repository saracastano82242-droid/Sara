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
"""import heapq" # La librería heapq proporciona una implementación de un heap en Python, que es una estructura de datos que permite almacenar elementos de manera eficiente, donde el elemento con la mayor prioridad se encuentra en la raíz del heap. La función heapq.heapify() se utiliza para convertir una lista en un heap, y las funciones heapq.heappush() y heapq.heappop() se utilizan para agregar y eliminar elementos del heap, respectivamente. Los heaps se utilizan comúnmente para implementar colas de prioridad y algoritmos de ordenamiento como heapsort.""
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

** NOTA: el heap lo usamos en caso de que necesitemos una estructura de datos que permita almacenar elementos de manera eficiente,
donde el elemento con la mayor prioridad se encuentra en la raíz del heap. 
Por ejemplo, si necesitamos implementar una cola de prioridad para gestionar tareas en un sistema operativo, podríamos utilizar un heap para almacenar las tareas y asegurarnos de que la tarea 
con la mayor prioridad se ejecute primero. Otro ejemplo podría ser en algoritmos de ordenamiento como heapsort, donde se utiliza un heap para ordenar una lista de elementos de manera eficiente. 

En resumen, el heap es útil cuando necesitamos gestionar elementos con prioridades o realizar operaciones de ordenamiento de manera eficiente.

cuando tenemos una lista de tuplas y queremos ordenarla por el segundo elemento de cada tupla, podemos utilizar la función sorted() con una función lambda como clave de ordenamiento. Por ejemplo:
lista_tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
print(f"Lista ordenada por segundo elemento: {lista_ordenada}")

#ejemplo de uso de heapq con tuplas
import heapq
def demo_heapq_con_tuplas():
    print("="*35)
    print("Ejemplo de heapq con tuplas")
    print("="*35)

    print("\n1. Crear un heap con tuplas:")
    print("-"*38)
    datos = [(2, 'tarea2'), (1, 'tarea1'), (3, 'tarea3')]
    print(f"Datos originales: {datos}")

    heapq.heapify(datos)
    print(f"Heap después de heapify: {datos}")
#ejemplo de uso
demo_heapq_con_tuplas()

heappop: elimina y retorna el elemento con la mayor prioridad (el mínimo en un min-heap o el máximo en un max-heap) del heap. Por ejemplo:
import heapq
heap = [(2, 'tarea2'), (1, 'tarea1'), (3, 'tarea3')]
heapq.heapify(heap)
print(f"Heap antes de heappop: {heap}")
elemento_con_prioridad = heapq.heappop(heap)
print(f"Elemento con mayor prioridad: {elemento_con_prioridad}")
print(f"Heap después de heappop: {heap}")


"""

#TAREA: nesecito un metodo que me indique si esta bien la exprecion que le ingrese que contenga "(,),{,},[,],45,12,3,4,5,6,7,8,9,+,-,*,/ y que me devuelta true o falce si esta bien o mal, lo evaluamos con pilas y colas
#ejemplo: valida: [(3 + 4) * 2 / (1 - 5)] -> true
#ejemplo: no valida: [(3 + 4) * 2 / (1 - 5] -> false
"""

def validar_expresion(expresion):
    pila = []
    pares_parentesis = {'(': ')', '{': '}', '[': ']'}
    
    for char in expresion:
        if char in pares_parentesis:  # Si el carácter es un paréntesis de apertura
            pila.append(char)  # Agrega el paréntesis a la pila
        elif char in pares_parentesis.values():  # Si el carácter es un paréntesis de cierre
            if not pila:  # Si la pila está vacía, no hay un paréntesis de apertura correspondiente
                return False
            ultimo_parentesis = pila.pop()  # Elimina el último paréntesis de apertura de la pila
            if pares_parentesis[ultimo_parentesis] != char:  # Verifica si el paréntesis de cierre corresponde al último paréntesis de apertura
                return False
    
    return len(pila) == 0  # Si la pila está vacía al final, la expresión es válida; de lo contrario, no lo es
# Ejemplo de uso
expresion_valida = "[(3 + 4) * 2 / (1 - 5)]"
expresion_no_valida = "[(3 + 4) * 2 / (1 - 5]"
print(f"Expresión: {expresion_valida} -> Válida: {validar_expresion(expresion_valida)}")
print(f"Expresión: {expresion_no_valida} -> Válida: {validar_expresion(expresion_no_valida)}")
"""

"""
09/03/2026
¿que son las expreciones regulares? 
R// Las expresiones regulares son patrones de búsqueda que se utilizan para encontrar y manipular texto. 
Permiten realizar búsquedas complejas y reemplazos en cadenas de texto utilizando una sintaxis específica. Las expresiones regulares 
son ampliamente utilizadas en programación para validar formatos de entrada, extraer información de texto, y realizar operaciones de búsqueda y reemplazo.

cosas clave:
* nos permine validar formatos de entrada (como correos electrónicos, números de teléfono, etc.)
* nos permite extraer información de texto (como direcciones IP, fechas, etc.)
* nos permite realizar operaciones de búsqueda y reemplazo en cadenas de texto.
* extraer información de texto utilizando grupos de captura, lo que nos permite obtener partes específicas 
de una cadena que coinciden con el patrón de búsqueda.
* las expresiones regulares son una herramienta poderosa para trabajar con texto y son ampliamente 
utilizadas en muchos lenguajes de programación, incluyendo Python, JavaScript, Java, entre otros.
* podemos reemplazar textos

¿para que se utilizan las expresiones regulares?
R// Las expresiones regulares se utilizan para validar formatos de entrada (como correos electrónicos,
números de teléfono, etc.), extraer información de texto (como direcciones IP, fechas, etc.),
y realizar operaciones de búsqueda y reemplazo en cadenas de texto.

lista: [1,2,3,4,5]
tupla: (1,2,3)


TAREA: explicar una exprecion regular que valide bien un correo electronico (hacer el codigo)

"""

"""
                            CONJUNTOS
Notacion: A = {1,2,3,4,5}
Cardinalidad: |A| = 5

pertenencia python: 2 in A -> True o false, preguntara si el elementi esta en el conjunto, el rendimiento cambia mucho ya sea en conjuntos o listas

union: A|B o A.union(B)
intersepcion: A & B o A.intercepcion(B)
diferencias: 
elementos A que NO estan en B

* A = {1.2.3}
* B = {3,4,5}
* A - B = {1,2}
* B - A = {4,5}

NOTA: A - B != B - A

Diferencia simetrica (A "triangulo")
elementos que A o B, pero NO en ambos

A = {1,2,3}
B = {3,4,5}
A triangulo B = {1,2,4,5}

Subconjuntos
todos los elementos pertenecen a A y estan en B

igualdal (A = B)

A c B y A != B

conjuntos disjuntos
A n B = !0

RETO: tengo una lista de n elementos y quiero eliminar todos los duplicados

"""

"""
19/03/26

  #return acciones_requeridoas <= permisos (subconjunto)
  

  OPERADOTES DE CONJUNTOS
- Unión (|): elementos en A o en B (o en ambos) (A|B)
- Intersección (&): elementos en A y en B (A&B)
- Diferencia (-): elementos en A que no están en B (A-B)
- Diferencia simétrica (△): elementos en A o B, pero no en ambos (A^B)
- Subconjunto (<=): A es un subconjunto de B si todos los elementos de A están en B (A <= B)
- Superconjunto (>=): A es un superconjunto de B si todos los elementos de B están en A (A >= B)
- Igualdad (==): A es igual a B si ambos conjuntos tienen los mismos elementos (A == B)
- No disjuntos: A y B no son disjuntos si tienen al menos un elemento en común (A n B != ∅)

DICCIONARIOS
- Un diccionario es una estructura de datos que almacena pares de clave-valor, donde cada clave es única y se utiliza para acceder a su valor 
correspondiente. En Python, los diccionarios se definen utilizando llaves {} y los pares de clave-valor se separan por dos
puntos (:). Por ejemplo: mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}.


"""