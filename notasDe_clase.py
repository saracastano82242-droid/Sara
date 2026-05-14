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
Para estudiar: ¿Que tengo que cambiarle al algoritmo para que funcione y sea eficiente, dependiendo si nececito bucket sort, radix sort, counting sort, quick sort, merge sort o heap sort?

"""