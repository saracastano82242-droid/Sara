def longitud(nodo):
#Cuenta nodos de forma recursiva."""
# Caso base: llegamos al final
    if nodo is None:
        return 0
# Caso recursivo: 1 + longitud del resto
    return 1 + longitud(nodo.siguiente)

# Como método de la clase:
class ListaEnlazada:
    def longitud_recursiva(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return 0
        return 1 + self.longitud_recursiva(nodo.siguiente)

# Ejemplo de uso
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def longitud_recursiva(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
        if nodo is None:
            return 0
        return 1 + self.longitud_recursiva(nodo.siguiente)
# Crear lista y agregar elementos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
print(lista.longitud_recursiva()) # Imprime 3

#buscar
def buscar_recursivo(nodo, dato):
#Busca un dato en la lista de forma recursiva."""
# Caso base 1: lista vacía, no encontrado
    if nodo is None:
        return False
# Caso base 2: encontrado
    if nodo.valor == dato:
        return True
# Caso recursivo: buscar en el resto
    return buscar_recursivo(nodo.siguiente, dato)
# Uso:
encontrado = buscar_recursivo(lista.cabeza, 42)
print(encontrado) # Imprime False

def imprimir_lista(nodo):
#Imprime la lista de forma recursiva."""
    if nodo is None:
        print("None")
        return
print(f"{nodo.valor} -> ", end="") # type: ignore
imprimir_lista(nodo.siguiente) # type: ignore # Llamada recursiva para imprimir el resto de la lista
# Ejemplo de uso
imprimir_lista(lista.cabeza) # Imprime 3 -> 2 -> 1 -> None

def imprimir_inverso(nodo):
#Imprime la lista en orden inverso."""
    if nodo is None:
        return
# Primero procesar el resto (llegar al final)
imprimir_inverso(Nodo.siguiente)
# Luego imprimir este nodo (al volver)
print(Nodo.valor, end=" ")
# Ejemplo de uso
imprimir_inverso(lista.cabeza) # Imprime 1 2 3  

#limite de la recursión
import sys
# Ver límite actual (por defecto ~1000)
print(sys.getrecursionlimit())
# Cambiar límite (¡con cuidado!)
sys.setrecursionlimit(2000)
# Esto causará RecursionError:
def infinita(n):
    return infinita(n + 1)
# infinita(1) # RecursionError: maximum recursion depth exceeded

#ejemplo de Fibonacci con memoización
def fibonacci_memo(n, memo={}):
    #Fibonacci con memoización (caché)."""
    # Si ya lo calculamos, retornar del caché
    if n in memo:
        return memo[n]
    # Casos base
    if n <= 1:
        return n
    # Calcular y guardar en caché
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
# Ahora es O(n) en vez de O(2^n)
print(fibonacci_memo(50)) # ¡Instantáneo!

