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

"""
analisis asintactico: es el proceso de analizar la estructura gramatical de una expresión o programa para determinar si es sintácticamente correcto.
En el contexto de expresiones matemáticas, el análisis sintáctico se utiliza para verificar si una expresión está bien formada, es decir, 
si los paréntesis están correctamente balanceados y si los operadores y operandos están en el orden correcto. El análisis sintáctico se puede r
ealizar utilizando pilas para verificar el balance de los paréntesis y la correcta secuencia de operadores y operandos.

EJEMPLO DE ANALISIS SINTACTICO CON PILAS
def analizar_expresion(expresion):
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
expresion_no_valida = "[(3 + 4) *   
2 / (1 - 5]"
print(f"Expresión: {expresion_valida} -> Válida: {analizar_expresion(expresion_valida)}")
print(f"Expresión: {expresion_no_valida} -> Válida: {analizar_expresion(expresion_no_valida)}") 

OTRO EJEMPLO DE ANALISIS SINTACTICO CON PILAS
def analizar_expresion(expresion):
    pila = []
    operadores = set(['+', '-', '*', '/'])
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
        elif char in operadores:  # Si el carácter es un operador
            if not pila or pila[-1] in operadores:  # Verifica si el operador está en una posición válida (no puede estar al inicio o después de otro operador)
                return False

    return len(pila) == 0  # Si la pila está vacía al final, la expresión es válida; de lo contrario, no lo es
# Ejemplo de uso
expresion_valida = "[(3 + 4) * 2 / (1 - 5)]"
expresion_no_valida = "[(3 + 4) *   2 / (1 - 5]"
print(f"Expresión: {expresion_valida} -> Válida: {analizar_expresion(expresion_valida)}")
print(f"Expresión: {expresion_no_valida} -> Válida: {analizar_expresion(expresion_no_valida)}")

mas ejemplos de análisis sintáctico con pilas se pueden encontrar en la implementación de algoritmos como el algoritmo Shunting Yard de Dijkstra, que se utiliza para convertir expresiones infijas a postfijas y evaluar expresiones postfijas utilizando una pila. Este algoritmo utiliza una pila para manejar los operadores y paréntesis mientras procesa la expresión, asegurando que la sintaxis sea correcta y que los operadores se apliquen en el orden correcto.

def contar (n): 
    contador = 0
    for i in range(n):
        contador += 1
        print(i)

    return contador

    
"2n" = el dos simbolisa el numero de lineas (es una constante) y la n sera cuantas veces se ejecuta el ciclo, entonces la complejidad de este algoritmo es O(2n) = O(n) 
porque se ejecuta el ciclo n veces y cada vez se realiza una operación constante (contador += 1 y print(i)). 
Por lo tanto, la complejidad del algoritmo es lineal con respecto a n.

ejemplo:
f(n) = 1+1+2n
     = 2n + 2 // significa que se ejecuta el ciclo n veces y cada vez se realiza una operación constante (contador += 1 y print(i))
        = O(n)

    2n + 2 = n + 2 // se elimina el 2 porque es una constante 
    0(n)= y se elimina el 2 porque es una constante, quedando O(n)

    notacion Big-O simplificada y generalizada
    0(5n + 10) = 0(n)
    0(n + 10) = 0(n)
    10

    #ejemplos de diccionarios en python
diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}

#ejemplpos cortos 
print(diccionario["clave1"]) # Imprime "valor1"
print(diccionario.get("clave2")) # Imprime "valor2"
print(diccionario.get("clave4", "Valor predeterminado")) # Imprime "Valor predeterminado" porque "clave4" no existe en el diccionario


"""

def contador_operaciones(n):
    contador = 0
    for i in range(n):
        contador += 1
        print(i)
    return contador

#ejercicio del profesor

def contador_mayoritario(arr): #complejidad cuadratica
    mayor = 0
    valor = 0
    for i in range(len(arr)):
        contador = 0 
        for j in range (len(arr)):
            if arr[j] == arr[i]:
                contador += 1
        if contador > valor:
            valor = contador
            mayor = i
    return mayor, valor

#forma de realizarlo menos complejo

def contador_mayoritario(arr): #complejidad lineal
    contador = {}
    mayor = 0
    valor = 0
    for i in range(len(arr)): #recorre la lista una sola vez, lo que tiene una complejidad de O(n), donde n es el número de elementos en la lista.
        if arr[i] in contador: # verifica si el elemento actual ya está en el diccionario contador. Si es así, incrementa su conteo en 1.
            contador[arr[i]] += 1 # Si el elemento no está en el diccionario, lo agrega con un conteo inicial de 1.
        else:
            contador[arr[i]] = 1 # Después de actualizar el conteo del elemento actual, verifica si su conteo es mayor que el valor
            #máximo registrado hasta ahora. Si es así, actualiza el valor máximo y el elemento mayoritario.
        
        if contador[arr[i]] > valor: # Verifica si el conteo del elemento actual es mayor que el valor máximo registrado hasta ahora. 
            #Si es así, actualiza el valor máximo y el elemento mayoritario.
            valor = contador[arr[i]]
            mayor = arr[i]
    return mayor, valor

#arr: significa arreglo, osea que es el nombre de la variable. 

#ejercicio hecho por el profesor

def elemento_mayoritario(arr):

    conteos = {}
    for elemento in arr:
        conteos[elemento] = conteos.get(elemento, 0) + 1 # El método get() del diccionario se utiliza para obtener el valor asociado a la clave elemento. Si la clave no existe en el diccionario, devuelve un valor predeterminado (en este caso, 0). Luego, se incrementa el conteo de ese elemento en 1.

    resultado = None
    mayor_conteo = 0
    for elemento, conteo in conteos.items(): # El método items() del diccionario devuelve una vista de los pares clave-valor del diccionario. En este caso, se itera sobre cada elemento y su conteo correspondiente.
        if conteo > mayor_conteo: # Se compara el conteo actual con el mayor conteo registrado hasta ahora. Si el conteo actual es mayor, se actualiza el mayor conteo y se establece el resultado como el elemento actual.
            mayor_conteo = conteo
            resultado = elemento

    return resultado

def menor_diferencia(arr):
    n = len(arr)
    min_diff = float('inf') # Se inicializa la variable min_diff con infinito para asegurarse de que cualquier diferencia encontrada sea menor que este valor inicial.

    for i in range (n):
        for j in range(i + 1, n): # Se itera sobre cada par de elementos en el arreglo utilizando dos bucles anidados. El segundo bucle comienza desde i + 1 para evitar comparar el mismo elemento consigo mismo y para evitar comparaciones redundantes.
            diff = abs(arr[i] - arr[j]) # Se calcula la diferencia absoluta entre los dos elementos actuales.
            min_diff = min(min_diff, diff) # Se actualiza min_diff con la menor diferencia encontrada hasta ahora utilizando la función min().

    return min_diff

"""
TAREA: mejorar este algoritmo para que tenga una complejidad menor de log n o si hay una mas eficiente mejor, y explicar como lo hiciste.

"""
def menor_diferencia(arr):
    arr.sort() # Se ordena el arreglo de menor a mayor utilizando el método sort(), lo que tiene una complejidad de O(n log n).
    min_diff = float('inf') # Se inicializa la variable min_diff con infinito para asegurarse de que cualquier diferencia encontrada sea menor que este valor inicial.

    for i in range(1, len(arr)): # Se itera sobre el arreglo ordenado comenzando desde el segundo elemento (índice 1) hasta el final del arreglo. Esto se hace para comparar cada elemento con su vecino inmediato.
        diff = abs(arr[i] - arr[i - 1]) # Se calcula la diferencia absoluta entre el elemento actual y su vecino inmediato anterior.
        min_diff = min(min_diff, diff) # Se actualiza min_diff con la menor diferencia encontrada hasta ahora utilizando la función min().

    return min_diff
"""
n^2: es un algoritmo poco eficiente ya que es bueno utilizarlo con datos pequeños.
complejidad espacial: no dice cuanta memoria usa, osea que esta relacionado con que va a ir revisando el codigo.
complejidad temporal: dice cuanto tiempo va a tardar el algoritmo en ejecutarse, osea que esta relacionado con el numero de operaciones que va a realizar el algoritmo.



def dubble_sort(arr):
    n = len(arr)
     #son los ultimos i elementos que ya estan ordenados
    for i in range(n):
        #Intercambia si el elemento encontrado es menor o mayor
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


#a implementar:
#ordenar a estudiantes por nota utilizando el ordenamiendo por burbuga y que me diga cuantos intercambios tuvo que hacer para poder ordenar a los estudiantes por su nota

def bubble_sort(arr):
    n = len(arr)
    contador = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]["nota"] > arr[j + 1]["nota"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                contador += 1
    return arr, contador

estudiantes = [
    {"nombre": "Juan", "nota": 3.8},
    {"nombre": "María", "nota": 4.5},
    {"nombre": "Pedro", "nota": 2.9},
    {"nombre": "Ana", "nota": 4.2},
    {"nombre": "Sara", "nota": 3.0}
]
estudiantes_ordenados, intercambios = bubble_sort(estudiantes)
print("Estudiantes ordenados:")
print(estudiantes_ordenados)

print(f"Cantidad de intercambios realizados: {intercambios}")

def bubble_sort(arr):
    n = len(arr)
    conteo = 0
    intercambios = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            conteo+= 1
            if arr[j]["nota"] > arr[j + 1]["nota"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
    return arr, conteo, intercambios



def dubble_sort(arr):
    n = len(arr)
    cont = 0
    intercambios = 0
     #son los ultimos i elementos que ya estan ordenados
    for i in range(n):
        #Intercambia si el elemento encontrado es menor o mayor
        for j in range(0, n - i - 1):
            cont += 0
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
    return arr, cont, intercambios

import time
import random

for n in [10, 100, 500, 1000, 3000, 10000]:
    aleatoria = [random.randint(1, 1000) for _ in range(n)]
    inicio = time.time()
    _,conteo, intercambios = dubble_sort(aleatoria.copy())
    tiempo = time.time() - inicio
    print(f"lista de {n} posiciones. Tiempo: {tiempo}, comparaciones: {conteo}, intercambios: {intercambios}")
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr [i]
        j = i - 1

        while j >= 0 and key < arr [j]:
            arr [j + 1] = arr [j]
            j -= 1
        arr [j + 1] = key
    return arr

nombres = ["Luis", "Ana", "Mario", "Andrea", "Carla", "Alberto", "Beatriz", "Sara"]

#organizar los nombres de manera alfabeticamente 
nombres_ordenadosAlfabeticamente = insertion_sort(nombres)
print("Nombres ordenados alfabéticamente:")
print(nombres_ordenadosAlfabeticamente)

"""
04/03/2026
burbuja: tiene una complejidad temporal 0(n^2), espacial 0(1),estable
insercion: tiene una complejidad temporal 0(n^2), espacial 0(1),estable
seleccion: tiene una complejidad temporal 0(n^2), espacial 0(1),no estable
estos solo son buenos para datos pequeños osea que no se recomienda utilizarlos para ordenar grandes cantidades de datos debido a su ineficiencia. 
"""

def merge (arr,left, middle, right):

    n1 = middle - left + 1
    n2 = right - middle

    L = arr[left:middle + 1]
    R = arr[middle + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right): #esto es una complejidad lineal porque se divide el arreglo en dos partes y se ordena cada parte de manera recursiva, lo que tiene una complejidad de O(n log n) debido a la división del arreglo y la combinación de las partes ordenadas.
    #[T(n)= 2T(n/2) + n -> O(n) =  log n -> n log n]
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)

import random
import time

for i in [100, 500, 1000, 3000]:
    lista = [random.randint(1, 1000) for _ in range(i)]

    inicio = time.time()
    merge_sort(lista, 0, i - 1)
    tiempo = time.time() - inicio
    print(f"Lista de {i} posiciones. Tiempo de ejecución: {tiempo}")

    """
    07/05/2026

    merge sort y heap sort son = n log n.
    bubble sort, insertion sort y selection sort son = n^2.
    counting sort = 0(n) este solo ordena numeros enteros.
    
    """

    def quicksort(arr, low, high):
        if low < high:
            #Encuentra el indicice de la partición
            pi = partition(arr, low, high)
            #Ordena los elementos antes y después de la partición
            quicksort(arr, low, pi - 1) # Ordena los elementos antes de la partición
            quicksort(arr, pi + 1, high) # Ordena los elementos después de la partición

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
#ejemplo de uso
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array:", arr)

"""
si tengo este arreglo[100,205,2,1503,10,55] no es recomendable utilizar quick sort por que el pivote elegido (en este caso, 
el último elemento del arreglo) es 55, lo que puede llevar a una partición desequilibrada. 
En este caso, el pivote 55 es mayor que la mayoría de los elementos del arreglo,

Radix sort es un algoritmo de ordenamiento no comparativo que ordena números enteros procesando cada dígito individualmente.
Es eficiente para ordenar grandes cantidades de números enteros, especialmente cuando el rango de los números es limitado. 
Sin embargo, no es adecuado para ordenar números con una gran cantidad de dígitos o para ordenar datos que no son enteros.
Y si tengo este arreglo[100,205,2,1503,10,55] el radix sort sería una buena opción para ordenar este arreglo, ya que todos los elementos son números enteros 
y el rango de los números es relativamente pequeño (de 0 a 1503). 
ya que el radix sort ordena los números procesando cada dígito individualmente, sería eficiente para ordenar este arreglo en particular.

counting sort es un algoritmo de ordenamiento no comparativo que ordena números enteros contando el número de ocurrencias de cada valor en el arreglo.
Es eficiente para ordenar grandes cantidades de números enteros, especialmente cuando el rango de los números es
limitado. Sin embargo, no es adecuado para ordenar números con una gran cantidad de dígitos o para ordenar datos que no son enteros.
Y si tengo este arreglo[100,205,2,1503,10,55] el counting sort sería una buena opción para ordenar este arreglo, ya que todos los elementos son números enteros
y el rango de los números es relativamente pequeño (de 0 a 1503).

"""

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10): #Este ciclo acumula los conteos para que el count[i] contenga la posición final de este dígito en el arreglo de salida.
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_element = max(arr)

    exp = 1
    while max_element // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

#ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)

"""
Radix sort: no sirve con decimales ni con string, solo sirve con numeros enteros
caracteristicas: en espacio 0(n)
tiempo: 0(n + k )(n)
es estable.

bucket sort: es un algoritmo de ordenamiento que distribuye los elementos de un arreglo en un número finito de "cubetas" o "baldes", y 
luego ordena cada cubeta individualmente utilizando otro algoritmo de ordenamiento (como insertion sort) o aplicando recursivamente el bucket sort.
 Es eficiente para ordenar números flotantes en un rango específico, pero no es adecuado para ordenar números enteros o datos que no son flotantes.

"""
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr
#ejemplo de uso
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)

#ejemplo de buket que no se deberia implementar por que no es eficiente para ordenar numeros enteros
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    max_value = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_value) / (max_value - min_value) * (bucket_count - 1))
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr
#ejemplo de uso
arr = [100, 205, 2, 1503, 10, 55]
sorted_arr = bucket_sort(arr)
print(sorted_arr)   

"""
Para estudiar: ¿Que tengo que cambiarle al algoritmo para que funcione y sea eficiente, dependiendo si nececito bucket sort, radix sort, counting sort,
quick sort, merge sort o heap sort?

"""

"""
# 🎯 Elección del Algoritmo de Ordenamiento

## Tabla de referencia

| Algoritmo      | Mejor    | Promedio  | Peor      | Espacio  | Estable | Notas |
|----------------|----------|-----------|-----------|----------|---------|-------|
| Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | ✅ Sí   | Garantiza n log n siempre |
| Quick Sort     | O(n log n) | O(n log n) | O(n²)     | O(log n) | ❌ No   | Rápido en práctica, in-place |
| Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | ❌ No   | In-place, sin peor caso malo |
| Counting Sort  | O(n + k) | O(n + k)  | O(n + k)  | O(n + k) | ✅ Sí   | Solo enteros con rango limitado k |
| Radix Sort     | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n + k) | ✅ Sí   | Para enteros/strings de d dígitos |
| Bucket Sort    | O(n + k) | O(n + k)  | O(n²)     | O(n + k) | ✅ Sí*  | Datos uniformemente distribuidos |

---

## 🧩 10 Casos para que los estudiantes decidan

Para cada caso analiza:
1. ¿Cuál es el mejor algoritmo? ¿Por qué?
2. ¿Qué algoritmos descartas y por qué?
3. Considera complejidad temporal, espacial y estabilidad
4. ¿Qué pasaría si cambian alguna restricción del problema?

---

### Caso 1: Sistema de notas finales de un semestre universitario

**Contexto del problema:**
La universidad necesita generar el listado oficial de calificaciones al final
del semestre. Tienes una base de datos con 200 estudiantes de un curso, cada
uno con una nota final en escala 0-100 (números enteros). El sistema debe
imprimir el listado ordenado de menor a mayor para publicarlo en la cartelera
oficial.

**Datos clave:**
- Tamaño: n = 200 estudiantes
- Tipo de dato: enteros entre 0 y 100
- Rango: k = 101 valores posibles (muy pequeño)
- Restricción: si dos estudiantes tienen la misma nota, deben quedar en el
  orden en que aparecen en la lista original (orden alfabético previo).
- No hay limitación de memoria.

**Pregunta:**
¿Qué algoritmo eliges? Justifica considerando complejidad temporal, espacial
y la necesidad de estabilidad. ¿Cambiaría tu respuesta si fueran 10 millones
de estudiantes en lugar de 200?

---

### Caso 2: Cierre diario de un sistema bancario

**Contexto del problema:**
Un banco mediano procesa cerca de 1 millón de transacciones diarias. Al cierre
del día, el equipo de auditoría necesita una lista ordenada por monto para
detectar anomalías y generar reportes regulatorios. El servidor que ejecuta
este proceso es compartido con otros sistemas críticos, por lo que **NO puede
consumir más de 500 MB de RAM extra** durante el ordenamiento.

**Datos clave:**
- Tamaño: n = 1,000,000 transacciones
- Tipo de dato: números reales (decimales) en pesos colombianos
- Rango: desde 100 hasta 10,000,000,000 (10^10) → rango enorme
- Restricción de memoria: poca RAM extra disponible
- Restricción de tiempo: el reporte debe estar listo en menos de 5 minutos
- No se requiere estabilidad (cada transacción tiene un ID único)
- El proceso se ejecuta en producción, por lo que **NO se aceptan sorpresas
  con peores casos malos**.


---

### Caso 3: Limpieza de archivos en un servidor de producción

**Contexto del problema:**
Eres administrador de un servidor con 50,000 archivos. Necesitas ordenarlos
por tamaño para identificar los más grandes y liberar espacio. El servidor
ejecuta este proceso durante la madrugada como tarea programada y **debe
terminar en una ventana fija de 30 minutos**, sin importar la distribución de
los datos. No puedes permitir que el algoritmo se demore más de lo previsto.

**Datos clave:**
- Tamaño: n = 50,000 archivos
- Tipo de dato: enteros (bytes), desde 1KB (1024) hasta 10GB (10^10)
- Distribución: muy variada e impredecible
- Restricción crítica: garantía de tiempo en el peor caso
- Memoria: disponible (servidor de producción con buena RAM)
- Estabilidad: no requerida



---

### Caso 4: Reportes de RRHH ordenados por dos criterios

**Contexto del problema:**
El área de Recursos Humanos te pide un reporte de empleados ordenado por
DEPARTAMENTO. El detalle: dentro de cada departamento, los empleados deben
aparecer ordenados por SALARIO (de mayor a menor). Tú ya tienes la lista
ordenada por salario (descendente). Lo único que falta es agruparlos por
departamento manteniendo el orden previo.

**Datos clave:**
- Tamaño: n = 5,000 empleados
- La lista de entrada YA está ordenada por salario descendente
- Necesitas reordenar por departamento, **manteniendo el orden por salario
  dentro de cada departamento**
- Departamentos: aproximadamente 15 distintos
- Memoria: disponible

---

### Caso 5: Detección de cédulas duplicadas en una base nacional

**Contexto del problema:**
La Registraduría te entrega un archivo con 10 millones de cédulas (números
enteros) y te pide ordenarlas para detectar duplicados. Las cédulas
colombianas tienen hasta 10 dígitos (1 a 9,999,999,999). Tienes que procesar
todo en una máquina con 16 GB de RAM: el
proceso anterior tardaba más de una hora y se
necesita reducirlo significativamente.

**Datos clave:**
- Tamaño: n = 10,000,000 cédulas
- Tipo de dato: enteros de hasta 10 dígitos (d = 10)
- Rango: hasta 10^10 → demasiado grande para Counting Sort directo
- Memoria: amplia (16 GB)
- Estabilidad: deseable para auditoría


---

### Caso 6: Sensor IoT de temperatura en un microcontrolador

**Contexto del problema:**
Estás programando el firmware de un sensor de temperatura para uso industrial.
El microcontrolador tiene **apenas 4 KB de RAM total** y debe almacenar 100
mediciones de temperatura del último día para luego ordenarlas y enviar la
mediana al servidor central. Cualquier algoritmo que use memoria extra
significativa hará que el dispositivo falle por desbordamiento de memoria.

**Datos clave:**
- Tamaño: n = 100 mediciones
- Tipo de dato: enteros (la temperatura va de -40 a 85, multiplicada por 100)
- Rango: ~12,500 valores posibles
- Estabilidad: no relevante


**Pregunta:**
¿Qué algoritmo eliges considerando que la memoria es la restricción más dura?
¿Por qué Merge Sort no funciona aquí? ¿Por qué Counting Sort tampoco es buena
idea aunque los datos sean enteros? ¿Qué algoritmo es completamente in-place
y aún así garantiza O(n log n)?

---

### Caso 7: Stream de datos de un sensor en tiempo real

**Contexto del problema:**
Tienes un sistema de monitoreo ambiental que recibe 1 medición por segundo
durante todo el día. Cada medición es un valor entero entre 0 y 100 (índice
de calidad del aire). Al final del día (86,400 segundos ≈ 86,400 mediciones)
debes ordenar todo el batch para generar estadísticas. Como las mediciones se
repetirán mucho (rango pequeño), buscas el algoritmo más rápido posible.

**Datos clave:**
- Tamaño: n ≈ 86,400 mediciones por día
- Tipo de dato: enteros entre 0 y 100
- Rango: k = 101 (muy pequeño comparado con n)
- Memoria: disponible (es un servidor)
- Estabilidad: deseable para mantener orden temporal

**Pregunta:**
¿Qué algoritmo permite ordenar en tiempo lineal O(n)? ¿Por qué los algoritmos
basados en comparación (Merge/Heap/Quick) son innecesariamente lentos aquí?
Si el rango fuera 0 a 1,000,000 en lugar de 0 a 100, ¿cambiarías de
algoritmo? ¿Cuál escogerías?

---

### Caso 8: Distribución de paquetes en una empresa de logística

**Contexto del problema:**
Una empresa de envíos como Servientrega tiene 500,000 paquetes que llegan a
un centro de distribución y deben clasificarse por código postal para enviarse
a la región correcta. Los códigos postales en Colombia son enteros de 6
dígitos (000000 a 999999). El equipo de operaciones ha verificado que la
**distribución de paquetes por código postal es bastante uniforme**: ningún
código concentra más del 1% de los paquetes.

**Datos clave:**
- Tamaño: n = 500,000 paquetes
- Tipo de dato: enteros de 6 dígitos
- Rango: 0 a 999,999 → k = 1,000,000
- Distribución: **uniforme** (información clave del problema)
- Memoria: disponible
- Estabilidad: no requerida

**Pregunta:**
¿Qué algoritmo aprovecha específicamente la "distribución uniforme"? ¿Por qué
NO es buena idea Counting Sort aunque sean enteros (pista: compara n vs k)?
¿Qué pasa si la distribución NO fuera uniforme y todos los paquetes vinieran
de unos pocos códigos? ¿A qué algoritmo te cambiarías?

---

### Caso 9: Cola de procesos en un sistema operativo

**Contexto del problema:**
Estás implementando el planificador de procesos de un sistema operativo
sencillo. Tienes 10,000 procesos en cola, cada uno con:
- Una **prioridad** (entero del 1 al 10, donde 10 es lo más urgente)
- Un **nombre** del proceso
- Un **timestamp** de cuándo llegó

Necesitas ordenarlos por prioridad descendente. Cuando dos procesos tienen la
misma prioridad, deben atenderse **en el orden de llegada** (FIFO dentro de
cada prioridad).

**Datos clave:**
- Tamaño: n = 10,000 procesos
- Tipo de dato: prioridades enteras 1-10 (k = 10)
- Restricción crítica: estabilidad obligatoria (orden de llegada)
- Memoria: disponible
- Tiempo: lo más rápido posible (es un planificador en tiempo real)

**Pregunta:**
¿Qué algoritmo te da O(n) y mantiene el orden de llegada? Mucha gente respondería
"Heap Sort porque es una cola de prioridad", pero esa respuesta es incorrecta
para este caso. ¿Por qué? ¿Cuál es la diferencia entre "ordenar un batch de
prioridades" y "mantener una cola de prioridad dinámica"?

---

### Caso 10: Catálogo de productos en una plataforma e-commerce

**Contexto del problema:**
Mercado Libre necesita ordenar alfabéticamente 100,000 nombres de productos
para mostrar el catálogo en la sección "navegar por nombre". Los nombres son
strings de hasta 50 caracteres con tildes y caracteres especiales. El catálogo
se actualiza una vez al día y se cachea, por lo que el tiempo no es crítico
pero sí debe ser predecible. Tienes memoria de sobra en el servidor.

**Datos clave:**
- Tamaño: n = 100,000 productos
- Tipo de dato: strings de hasta 50 caracteres
- Memoria: amplia
- Restricción: tiempo predecible (no se aceptan picos de O(n²))
- Estabilidad: deseable (los productos vienen pre-ordenados por categoría)

**Pregunta:**
¿Por qué Counting Sort, Radix Sort y Bucket Sort no son la primera opción para
strings largos? Entre Merge Sort, Heap Sort y Quick Sort: ¿cuál combina
estabilidad + garantía de O(n log n)? ¿Qué desventaja tiene Quick Sort cuando
los strings ya vienen casi ordenados (por ejemplo, ordenados por categoría)?

---

# ═════════════════════════════════════════════════════════════════════════════
# 💡 SOLUCIONES DETALLADAS
# ═════════════════════════════════════════════════════════════════════════════

## ✅ Caso 1: Notas finales — **Counting Sort**

**Análisis del problema:**
Tenemos n = 200 enteros en un rango muy pequeño (k = 101). Estamos en un
escenario perfecto para los algoritmos NO comparativos.

**¿Por qué Counting Sort?**
- Tiempo: O(n + k) = O(200 + 101) ≈ O(n). Lineal y muy rápido.
- Espacio: O(n + k), aceptable porque k es pequeño (101 contadores).
- Estabilidad: ✅ es estable, lo que respeta el orden alfabético previo cuando
  hay empates en la nota.

**¿Por qué NO los demás?**
- Merge/Quick/Heap Sort son O(n log n). Funcionan, pero son innecesariamente
  lentos cuando el rango es pequeño.
- Radix Sort funcionaría pero es overkill: las notas tienen pocos dígitos y
  Counting Sort es más simple y rápido.
- Bucket Sort también funcionaría, pero al ser enteros con rango fijo,
  Counting Sort es la elección más natural.

**¿Y si fueran 10 millones de estudiantes?**
La respuesta NO cambia: Counting Sort sigue siendo O(n + k) = O(10^7 + 101) ≈
O(n). Mientras k siga siendo pequeño respecto a n, Counting Sort es imbatible.
Solo cambiaría si las notas fueran reales con muchos decimales (ahí
necesitaríamos Bucket Sort o Quick/Merge).

---

## ✅ Caso 2: Sistema bancario — **Heap Sort**

**Análisis del problema:**
1 millón de números reales con rango enorme (10^10), memoria limitada y
necesidad de garantía de tiempo en producción. Las restricciones eliminan
varios candidatos.

**¿Por qué Heap Sort?**
- Tiempo: O(n log n) **garantizado** en peor caso (~20 millones de
  comparaciones para n = 10^6).
- Espacio: O(1) → es **in-place**, no consume RAM extra.
- Sin sorpresas en producción: nunca degrada a O(n²).

**¿Por qué NO los demás?**
- **Counting/Radix/Bucket**: descartados porque los datos son reales con rango
  enorme. No se pueden usar directamente.
- **Merge Sort**: tiempo bueno pero usa O(n) de memoria extra → 1 millón de
  flotantes ocupan más RAM de la disponible.
- **Quick Sort**: en promedio es más rápido, pero su peor caso O(n²) es
  inaceptable en producción. Si el dataset trae un patrón que cae en su peor
  caso (datos casi ordenados), el cierre del día se haría lentísimo.

**Comparación práctica:**
- Merge Sort: ~20M operaciones + 1M de RAM extra (no hay)
- Heap Sort: ~20M operaciones + 0 RAM extra → ¡gana!
- Quick Sort: ~20M operaciones promedio, pero hasta 10^12 en peor caso → riesgo

---

## ✅ Caso 3: Limpieza de archivos — **Heap Sort** (o Merge Sort)

**Análisis del problema:**
La palabra clave es **"predecibilidad"**. El proceso debe terminar en tiempo
fijo sin importar la entrada.

**¿Por qué Heap Sort o Merge Sort?**
Ambos garantizan O(n log n) en el peor caso. Para n = 50,000:
- ~50,000 × log2(50,000) ≈ 50,000 × 16 ≈ 800,000 operaciones.
- Esto es muy rápido y predecible.

**¿Cuál de los dos elegir?**
| Criterio | Merge Sort | Heap Sort |
|----------|------------|-----------|
| Tiempo | O(n log n) | O(n log n) |
| Espacio | O(n) extra | O(1) in-place |
| Estabilidad | ✅ | ❌ |
| Velocidad real | Suele ser más rápido | Un poco más lento por saltos en memoria |

Como **NO se requiere estabilidad** y la memoria está disponible, ambos son
válidos. **Heap Sort** gana ligeramente por usar menos memoria, pero **Merge
Sort** suele ser un poco más rápido en la práctica por mejor uso del caché.

**¿Por qué NO Quick Sort?**
Aunque suele ser el más rápido en promedio, tiene peor caso O(n²). Si los
archivos ya vienen casi ordenados por tamaño (caso común con archivos de un
mismo tipo), Quick Sort se cae a O(n²). Para n = 50,000 eso sería 2,500
millones de operaciones → minutos de demora extra. Inaceptable cuando hay
ventana fija.

---

## ✅ Caso 4: RRHH por dos criterios — **Merge Sort**

**Análisis del problema:**
Este es un caso clásico de "ordenamiento por múltiples claves usando
estabilidad". La estrategia es:
1. Ya está ordenado por la clave secundaria (salario).
2. Se aplica un algoritmo **estable** sobre la clave primaria (departamento).
3. Como es estable, los empates en departamento mantienen el orden por salario.

**¿Por qué Merge Sort?**
- ✅ Es **estable** → respeta el orden previo cuando hay empates.
- O(n log n) garantizado.
- Memoria disponible, así que el O(n) extra no es problema.

**¿Por qué NO Quick Sort y Heap Sort?**
Ambos son **inestables**. Si los aplicas, dentro de cada departamento el orden
por salario puede romperse y los empleados aparecerían en orden aleatorio.
Esto rompe el requisito del reporte.

**¿Counting Sort funcionaría?**
Sí, sería incluso mejor. Como solo hay ~15 departamentos (k = 15 muy pequeño
comparado con n = 5,000), Counting Sort sería O(n + k) ≈ O(n) y es estable.
La respuesta más completa es: **"Counting Sort si el número de departamentos
es pequeño y conocido, sino Merge Sort"**.

**Truco mnemotécnico:** "Si el problema dice 'ordenar manteniendo el orden
previo', necesitas un algoritmo ESTABLE. Punto."

---

## ✅ Caso 5: Cédulas duplicadas — **Radix Sort**

**Análisis del problema:**
Tenemos enteros con rango enorme (10^10) y cantidad gigante (10^7). Counting
Sort directo necesitaría un array de 10^10 contadores → imposible. Pero
Counting Sort aplicado **dígito por dígito** sí funciona: ese es Radix Sort.

**¿Por qué Radix Sort?**
- Tiempo: O(d × (n + k)) donde d=10 dígitos y k=10 (base decimal)
  = O(10 × (10^7 + 10)) ≈ O(10^8) → unas 100 millones de operaciones.
- Comparado con O(n log n) = 10^7 × 23 ≈ 2.3 × 10^8 operaciones.
- Radix es ~2x más rápido en este caso, **y es estable**.

**¿Por qué NO Counting Sort directo?**
Counting Sort necesita un array auxiliar de tamaño k. Con k = 10^10,
necesitaríamos 80 GB de memoria solo para los contadores. Imposible.

**¿Por qué NO Quick/Heap Sort?**
Funcionan, pero son O(n log n) sin la posibilidad de bajar más. Radix Sort
explota la estructura de los datos (que son enteros con pocos dígitos) para
romper esa barrera.

**Cálculo real:**
- O(n log n) ≈ 10^7 × 23 = 230 millones de comparaciones
- O(d × n) ≈ 10 × 10^7 = 100 millones de operaciones simples
- Radix gana incluso considerando las constantes ocultas.

---

## ✅ Caso 6: Sensor IoT — **Heap Sort**

**Análisis del problema:**
La restricción crítica es **memoria**: 4 KB de RAM. Cualquier algoritmo que
use O(n) extra está descartado.

**¿Por qué Heap Sort?**
- Es **in-place** → O(1) memoria extra. Es decir, no necesita un segundo
  arreglo, modifica el original.
- Garantiza O(n log n). Para n=100, eso es ~700 operaciones, instantáneo.
- No tiene peor caso malo.

**¿Por qué NO los demás?**
- **Counting Sort**: necesita un array de 12,500 contadores (rango k). Si cada
  entero ocupa 2 bytes, son 25 KB → no caben en 4 KB.
- **Merge Sort**: usa O(n) memoria extra para el buffer de merge → si bien para
  n=100 son solo 200 bytes, en este tipo de hardware todo cuenta y Heap Sort
  no necesita absolutamente nada.
- **Bucket/Radix**: necesitan memoria para las cubetas, descartados.
- **Quick Sort**: usa O(log n) por la pila de recursión y tiene peor caso
  malo. Para sistemas embebidos donde todo debe ser predecible, no se usa.

**Curiosidad:** Heap Sort es el algoritmo preferido en sistemas embebidos y
en kernels de sistemas operativos justamente por estas razones (memoria
mínima + peor caso garantizado).

---

## ✅ Caso 7: Stream de datos — **Counting Sort**

**Análisis del problema:**
86,400 valores enteros con rango k = 101. Caso ideal para Counting Sort.

**¿Por qué Counting Sort?**
- Tiempo: O(n + k) = O(86,500) ≈ O(n). Lineal.
- Como las mediciones SE REPITEN MUCHO (k=101 pero n=86,400), Counting Sort
  agrupa todo en 101 contadores sin tener que comparar.
- Es estable → mantiene el orden temporal de las mediciones.

**¿Por qué los algoritmos comparativos son innecesariamente lentos?**
- Merge/Heap/Quick Sort: O(n log n) = 86,400 × 17 ≈ 1.5 millones de
  comparaciones.
- Counting Sort: ~86,500 operaciones simples (incrementos en un array).
- ~17x más rápido. Para un sistema que se ejecuta diariamente, esa diferencia
  importa.

**¿Y si el rango fuera 0 a 1,000,000?**
Entonces n = 86,400 y k = 10^6 → k > n. Counting Sort se vuelve ineficiente
(usa más memoria que el propio dataset). En ese caso usaría:
- **Radix Sort** si los datos son enteros (sigue siendo O(n) si d es pequeño).
- **Bucket Sort** si la distribución es uniforme.
- **Heap/Merge Sort** si nada de lo anterior aplica → O(n log n).

---

## ✅ Caso 8: Logística — **Bucket Sort** (o Radix Sort)

**Análisis del problema:**
La pista crítica es **"distribución uniforme"**. Bucket Sort fue diseñado
exactamente para este caso.

**¿Por qué Bucket Sort?**
- Tiempo promedio: O(n + k) cuando la distribución es uniforme.
- Estrategia: divide los códigos postales en cubetas (por ejemplo, 1000
  cubetas de 1000 códigos cada una). Como la distribución es uniforme, cada
  cubeta queda con ~500 elementos. Ordenas cada cubeta con un algoritmo simple
  (insertion sort) y concatenas.
- Es estable.

**¿Por qué NO Counting Sort directo?**
- Necesitaría 1,000,000 contadores (uno por cada código postal posible).
- Comparar n=500,000 vs k=1,000,000: k > n, ineficiente. Más memoria gastada
  en contadores que en los datos mismos.

**¿Y si la distribución NO fuera uniforme?**
Bucket Sort se degrada a O(n²) en el peor caso (todos los elementos en una
sola cubeta). Por eso la pista de "distribución uniforme" es clave.

Si NO supiéramos si es uniforme, la mejor opción sería **Radix Sort**:
O(d × n) = O(6 × 500,000) ≈ O(n), garantizado sin importar la distribución.
Es la opción "segura" para enteros.

**Decisión final:**
- "Distribución uniforme" mencionada → **Bucket Sort** (aprovecha la pista).
- "Sin información sobre distribución" → **Radix Sort** (más seguro).


## ✅ Caso 9: Cola de procesos — **Counting Sort**

**Análisis del problema:**
Trampa del enunciado: muchos estudiantes responden "Heap Sort" porque la
palabra "prioridad" hace pensar en heaps. **Esa respuesta es incorrecta** para
ordenar un batch.

**¿Por qué Counting Sort?**
- Las prioridades son enteros 1-10 → k = 10, muy pequeño.
- Tiempo: O(n + k) = O(10,010) ≈ O(n). Lineal.
- Es **estable** → mantiene el orden de llegada (FIFO) cuando hay empates.

**¿Por qué Heap Sort NO es la respuesta correcta aquí?**
Esta es la diferencia clave que confunde a muchos:

| Cola de prioridad dinámica | Ordenar batch de prioridades |
|---------------------------|------------------------------|
| Insertar/extraer continuamente | Ordenar todo de una vez |
| Heap Sort / Priority Queue (heapq) | Counting Sort (si k pequeño) |
| O(log n) por operación | O(n + k) total |
| **NO es estable** | **Sí es estable** |

Para "tener procesos llegando y atendiéndolos uno por uno" usarías un heap
(estructura de datos). Pero para "ordenar 10,000 procesos de una vez", Counting
Sort es más rápido.

Además, Heap Sort no es estable → rompería el orden FIFO entre procesos con
la misma prioridad. Inaceptable según el enunciado.

**Para descartar Quick/Merge:**
- Quick Sort: no estable + O(n²) peor caso. Doble descarte.
- Merge Sort: estable y O(n log n). Funciona, pero Counting Sort es más
  rápido aprovechando que k=10.

---

## ✅ Caso 10: Strings largos — **Merge Sort**

**Análisis del problema:**
100,000 strings con potencial pre-orden por categoría. Necesitamos algo
estable, predecible y que aproveche el pre-orden si existe.

**¿Por qué Merge Sort?**
- O(n log n) garantizado: 100,000 × 17 ≈ 1.7M comparaciones (cada comparación
  de strings cuesta hasta 50 caracteres → 85M comparaciones de char).
- ✅ Es **estable** → mantiene el orden previo por categoría dentro de
  empates.
- Memoria disponible, así que el O(n) extra no es problema.
- Sin peor caso malo.

**¿Por qué NO los algoritmos no comparativos?**
- **Counting Sort**: solo para enteros, no aplica directamente a strings.
- **Radix Sort para strings**: existe (lexicographic radix sort), pero con
  d=50 caracteres y k=256 (ASCII) o más (Unicode), su rendimiento de
  O(d × (n + k)) = O(50 × (100,000 + 256)) ≈ 5 millones de operaciones puede
  ser comparable o peor que Merge Sort en la práctica, sobre todo por las
  constantes ocultas.
- **Bucket Sort**: requeriría definir cubetas por la primera letra y luego
  ordenar dentro. Funciona pero la distribución de letras NO es uniforme en
  español (más palabras con "a", "c", "p" que con "x", "k", "w").

**¿Por qué NO Quick Sort?**
Doble problema:
1. Peor caso O(n²) cuando los datos vienen casi ordenados → es exactamente lo
   que ocurre aquí (los productos vienen ordenados por categoría).
2. No es estable.

**¿Y Heap Sort?**
Funciona y garantiza O(n log n). El único problema es que **NO es estable**,
así que se pierde el pre-orden por categoría. Si la estabilidad no fuera
importante, Heap Sort es una opción válida con menor uso de memoria.

---

# 📊 Reglas heurísticas rápidas

| Si el caso menciona... | Probablemente uses... |
|------------------------|------------------------|
| Enteros con rango pequeño (k pequeño respecto a n) | **Counting Sort** |
| Enteros con muchos dígitos (k grande, d pequeño) | **Radix Sort** |
| Distribución uniforme conocida | **Bucket Sort** |
| Memoria muy limitada / sistemas embebidos | **Heap Sort** |
| Estabilidad requerida + memoria disponible | **Merge Sort** |
| Rendimiento promedio óptimo y datos aleatorios | **Quick Sort** |
| Garantía de peor caso obligatoria | NO uses Quick Sort |
| Datos casi ordenados | NO uses Quick Sort básico |
| Strings sin estructura aprovechable | Merge Sort o Heap Sort |
| Cola de prioridad DINÁMICA (insertar/extraer) | Heap (estructura) |
| Ordenar BATCH con prioridades pequeñas | Counting Sort (no Heap) |

---

# 🧠 Estrategia para responder estos casos

Cuando enfrentes un caso similar, sigue estos pasos:

1. **¿Los datos son enteros?**
   - Sí, y k pequeño → Counting Sort
   - Sí, y k grande pero d pequeño → Radix Sort
   - Sí, y distribución uniforme → Bucket Sort
   - No (reales/strings) → continúa al paso 2

2. **¿Hay restricción de memoria?**
   - Sí, severa → Heap Sort (O(1) extra)
   - No → continúa al paso 3

3. **¿Se requiere estabilidad?**
   - Sí → Merge Sort
   - No → continúa al paso 4

4. **¿Se acepta el peor caso O(n²)?**
   - Sí (datos aleatorios y rendimiento promedio importa) → Quick Sort
   - No (producción, datos potencialmente patológicos) → Heap Sort o Merge Sort

5. **Verifica casos extremos:**
   - ¿Hay pre-orden? → evita Quick Sort
   - ¿Datos repetidos masivos? → Counting Sort si son enteros """

"""
algoritmos de ordenamiento organizados por el mejor y el peor caso, dependiendo de las caracteristicas del arreglo a ordenar, como el tipo de dato, el rango de los datos, la cantidad de datos, la memoria disponible y si se requiere estabilidad o no.

Merge sort:Es eficiente para ordenar grandes cantidades de datos, pero requiere espacio adicional para almacenar 
los subarreglos durante el proceso de fusión. Es estable y tiene una complejidad temporal de O(n log n) en el mejor, promedio y peor caso. 

Quick sort: Es eficiente para ordenar grandes cantidades de datos, pero su rendimiento puede degradarse a O(n²) en el peor caso, 
especialmente si el arreglo ya está ordenado o casi ordenado. No es estable y tiene una complejidad temporal de O(n log n) en el mejor y promedio caso.

Heap sort: Es eficiente para ordenar grandes cantidades de datos, pero no es estable y tiene una complejidad temporal de O(n log n) en el mejor, 
promedio y peor caso. Es in-place, lo que significa que no requiere espacio adicional para almacenar subarreglos.

Counting sort: Es eficiente para ordenar enteros con un rango limitado, pero no es adecuado para ordenar números reales o datos que no son enteros. 
Es estable y tiene una complejidad temporal de O(n + k) en el mejor, promedio y peor caso, donde n es el número de elementos a ordenar y k es el rango de 
los enteros.

Radix sort: Es eficiente para ordenar enteros o cadenas de caracteres con un número limitado de dígitos, pero no es adecuado para ordenar 
números reales o datos que no son enteros. Es estable y tiene una complejidad temporal de O(d(n + k)) en el mejor, promedio y peor caso, donde d es el número
de dígitos, n es el número de elementos a ordenar y k es el rango de los enteros.

Bucket sort: Es eficiente para ordenar números flotantes en un rango específico, pero no es adecuado para ordenar números
 enteros o datos que no son flotantes. Es estable y tiene una complejidad temporal de O(n + k) en el mejor y promedio caso, pero puede degradarse a
O(n²) en el peor caso si los datos no están distribuidos uniformemente.



"""