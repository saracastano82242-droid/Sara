# DATOS
manana = {"Juan", "Sara", "Diana", "Carlos", "Luis"}
tarde = {"Sara", "Pedro", "Luis", "Ana", "Marta"}

# RETOS (Resuélvelos usando una sola línea de código por punto):
# 1. ¿Quiénes estuvieron en AMBOS turnos?
# 2. ¿Quiénes estuvieron TODO el día (unión de ambos)?
# 3. ¿Quiénes solo estuvieron en la mañana?
# 4. ¿Quiénes estuvieron en UN SOLO turno (sin repetir)?
"""
REQUERIMIENTOS:
1. Usa una COLA para el abordaje del bus (Primero en llegar, primero en subir).
2. Usa una PILA para el maletero del bus (Última maleta en entrar, primera en salir).
3. Usa REGEX para validar el tiquete: "BUS-" seguido de 3 números y el destino "GUE" o "MAR".
   Ejemplo: BUS-102GUE
"""

import re

# Escribe aquí tu simulación:
# a) Función validar_tiquete(codigo)
# b) Lista para cola_pasajeros y métodos para subir uno.
# c) Lista para pila_maletas y métodos para sacar la última.
"""
═══════════════════════════════════════════════════════════════════════════════
                 PARCIAL FINAL - ESTRUCTURAS DE DATOS II
═══════════════════════════════════════════════════════════════════════════════
PUNTO 1: DISEÑO
Crea la clase Nodo (Dato) y la clase ConjuntoManual (Lista Enlazada).

PUNTO 2: AGREGAR SIN REPETIR (RECURSIVO)
Implementa el método agregar(dato). Si el dato ya existe, no se agrega.
OBLIGATORIO: Recursividad.

PUNTO 3: UNIÓN DE LISTAS (RECURSIVO)
Implementa un método que reciba otra Lista Enlazada y retorne una NUEVA 
con los elementos de AMBAS, sin duplicados.

PUNTO 4: MEMORIZACIÓN
Crea una función recursiva con memorización que calcule el costo de envío
basado en el peso 'n', donde costo(n) = costo(n-1) * 1.05.
═══════════════════════════════════════════════════════════════════════════════
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ConjuntoManual:
    def __init__(self):
        self.cabeza = None
        self.memo_costos = {} # Para el Punto 4

    # PUNTO 2: Agregar sin duplicados (Recursivo)
    def agregar(self, valor):
        if not self._existe(self.cabeza, valor):
            self.cabeza = self._agregar_rec(self.cabeza, valor)

    def _existe(self, nodo, valor):
        if nodo is None: return False
        if nodo.valor == valor: return True
        return self._existe(nodo.siguiente, valor)

    def _agregar_rec(self, nodo, valor):
        if nodo is None: return Nodo(valor)
        nodo.siguiente = self._agregar_rec(nodo.siguiente, valor)
        return nodo

    # PUNTO 4: Recursividad con Memorización
    def calcular_costo(self, n):
        if n == 0: return 1000 # Costo base
        if n in self.memo_costos: return self.memo_costos[n]
        
        self.memo_costos[n] = self.calcular_costo(n-1) * 1.05
        return self.memo_costos[n]

# PUNTO 3: Unión de Listas (Lógica externa para simplificar)
def union_listas(lista1, lista2):
    nueva_lista = ConjuntoManual()
    # Recorrer lista 1 y agregar (el método agregar ya evita duplicados)
    actual = lista1.cabeza
    while actual:
        nueva_lista.agregar(actual.valor)
        actual = actual.siguiente
    # Recorrer lista 2 y agregar
    actual = lista2.cabeza
    while actual:
        nueva_lista.agregar(actual.valor)
        actual = actual.siguiente
    return nueva_lista

manana = {"Juan", "Sara", "Diana", "Carlos", "Luis"}
tarde = {"Sara", "Pedro", "Luis", "Ana", "Marta"}

# 1. Ambos turnos (Intersección)
ambos = manana & tarde 
# Res: {'Sara', 'Luis'}

# 2. Todo el día (Unión)
todos = manana | tarde 
# Res: {'Juan', 'Sara', 'Diana', 'Carlos', 'Luis', 'Pedro', 'Ana', 'Marta'}

# 3. Solo mañana (Diferencia)
solo_manana = manana - tarde 
# Res: {'Juan', 'Diana', 'Carlos'}

# 4. Un solo turno (Diferencia Simétrica)
un_solo_turno = manana ^ tarde 
# Res: {'Juan', 'Diana', 'Carlos', 'Pedro', 'Ana', 'Marta'}


import re

# a) Validación con Regex
def validar_tiquete(codigo):
    # Formato: BUS- (literal), \d{3} (3 números), (GUE|MAR) (Una de las dos opciones)
    patron = r"^BUS-\d{3}(GUE|MAR)$"
    return bool(re.match(patron, codigo))

# b) COLA de Pasajeros (FIFO)
cola_pasajeros = []
def subir_pasajero(nombre, tiquete):
    if validar_tiquete(tiquete):
        cola_pasajeros.append(nombre)
        print(f"{nombre} subió al bus.")
    else:
        print("Tiquete inválido.")

def bajar_pasajero():
    if cola_pasajeros:
        # pop(0) saca al primero que entró (Concepto de COLA)
        print(f"Bajando a: {cola_pasajeros.pop(0)}")

# c) PILA de Maletas (LIFO)
pila_maletas = []
def agregar_maleta(dueno):
    pila_maletas.append(f"Maleta de {dueno}")

def sacar_maleta():
    if pila_maletas:
        # pop() sin índice saca la última (Concepto de PILA)
        print(f"Entregando: {pila_maletas.pop()}")


        import re

# a) Validación con Regex
def validar_tiquete(codigo):
    # Formato: BUS- (literal), \d{3} (3 números), (GUE|MAR) (Una de las dos opciones)
    patron = r"^BUS-\d{3}(GUE|MAR)$"
    return bool(re.match(patron, codigo))

# b) COLA de Pasajeros (FIFO)
cola_pasajeros = []
def subir_pasajero(nombre, tiquete):
    if validar_tiquete(tiquete):
        cola_pasajeros.append(nombre)
        print(f"{nombre} subió al bus.")
    else:
        print("Tiquete inválido.")

def bajar_pasajero():
    if cola_pasajeros:
        # pop(0) saca al primero que entró (Concepto de COLA)
        print(f"Bajando a: {cola_pasajeros.pop(0)}")

# c) PILA de Maletas (LIFO)
pila_maletas = []
def agregar_maleta(dueno):
    pila_maletas.append(f"Maleta de {dueno}")

def sacar_maleta():
    if pila_maletas:
        # pop() sin índice saca la última (Concepto de PILA)
        print(f"Entregando: {pila_maletas.pop()}")



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ConjuntoManual:
    def __init__(self):
        self.cabeza = None
        self.memo_costos = {}

    # --- PUNTO 2: AGREGAR SIN REPETIR (RECURSIVO) ---
    def agregar(self, valor):
        # Primero buscamos si ya existe para no romper la regla del conjunto
        if not self._existe_rec(self.cabeza, valor):
            self.cabeza = self._insertar_final_rec(self.cabeza, valor)

    def _existe_rec(self, actual, valor):
        if actual is None: return False
        if actual.valor == valor: return True
        return self._existe_rec(actual.siguiente, valor)

    def _insertar_final_rec(self, actual, valor):
        if actual is None: return Nodo(valor)
        actual.siguiente = self._insertar_final_rec(actual.siguiente, valor)
        return actual

    # --- PUNTO 3: UNIÓN DE LISTAS (Lógica recursiva) ---
    def unir_con(self, otra_lista):
        nueva = ConjuntoManual()
        # Metemos todos los de esta lista
        self._copiar_a_nueva(self.cabeza, nueva)
        # Metemos todos los de la otra (el método agregar evita duplicados)
        self._copiar_a_nueva(otra_lista.cabeza, nueva)
        return nueva

    def _copiar_a_nueva(self, actual, nueva_lista):
        if actual is not None:
            nueva_lista.agregar(actual.valor)
            self._copiar_a_nueva(actual.siguiente, nueva_lista)

    # --- PUNTO 4: MEMORIZACIÓN ---
    def calcular_costo_envio(self, peso):
        if peso == 0: return 1000  # Caso base: costo inicial
        if peso in self.memo_costos:
            return self.memo_costos[peso] # Retorno rápido si ya se calculó
        
        # Guardamos en el diccionario antes de retornar
        self.memo_costos[peso] = self.calcular_costo_envio(peso - 1) * 1.05
        return self.memo_costos[peso]

# --- PRUEBA FINAL ---
c1 = ConjuntoManual()
c1.agregar("A")
c1.agregar("B")
c1.agregar("A") # No se agrega

c2 = ConjuntoManual()
c2.agregar("B")
c2.agregar("C")

union = c1.unir_con(c2)
# Resultado esperado en la lista 'union': A, B, C (sin repetir B)

"""
Diferencia de pop(): Si el profe te pregunta por qué usas pop(0) en colas y pop() en pilas, dile que pop(0) es FIFO (atención por turnos) y pop() es LIFO (apilar objetos).
Recursividad con Memorización: La clave es el Diccionario. Siempre verifica si el dato ya está en el diccionario al principio de la función.
Recursividad en Nodos: Recuerda que al insertar o eliminar, debes retornar el nodo (return actual o return Nodo(valor)) para que la cadena de punteros no se rompa.
"""

"""
═══════════════════════════════════════════════════════════════════════════════
                    QUIZ - ESTRUCTURAS DE DATOS II
                                EXAMEN D
                    Sistema de Gestión de Suscriptores
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Una plataforma de streaming necesita gestionar suscriptores de dos planes:
"Plan Básico" y "Plan Premium". Debes realizar análisis de usuarios.

INSTRUCCIONES:
--------------
1. Usar CONJUNTOS NATIVOS de Python para el análisis rápido (Punto 1).
2. Implementar una LISTA ENLAZADA que funcione como un CONJUNTO (no permite 
   duplicados) para el almacenamiento principal (Puntos 2-5).
3. Usar RECURSIVIDAD donde se indique.
4. Tiempo: 90 minutos.

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): ANÁLISIS RÁPIDO (CONJUNTOS SIN LISTAS)
-----------------------------------------------------
Dados los siguientes conjuntos de IDs de usuarios:
basico = {101, 102, 105, 108}
premium = {105, 108, 110, 112}

Escribe el código para:
a) Obtener los IDs que están en AMBOS planes.
b) Obtener los IDs que están en Premium pero NO en Básico.


PUNTO 2 (1.0): DISEÑO DE CONJUNTO ENLAZADO
------------------------------------------
Diseña la clase Nodo y la clase ConjuntoEnlazado. 
- El método agregar(id) debe ser RECURSIVO y garantizar que NO se 
  inserten IDs duplicados. Si el ID ya existe, no hace nada.


PUNTO 3 (1.0): INTERSECCIÓN MANUAL - RECURSIVO
----------------------------------------------
Implementa un método que reciba otra lista enlazada y retorne cuántos 
elementos tienen en común.
- OBLIGATORIO usar recursividad.


PUNTO 4 (1.0): PERTENENCIA - RECURSIVO
--------------------------------------
Implementa un método 'existe(id)' que busque un ID en la lista.
- OBLIGATORIO usar recursividad.


PUNTO 5 (1.0): DIFERENCIA DE CONJUNTOS - RECURSIVO
--------------------------------------------------
Implementa un método que elimine de la lista original todos los IDs 
que se encuentren en un conjunto (set) de "IDs Baneados".
- OBLIGATORIO usar recursividad.

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""
# PUNTO 1: Conjuntos nativos (Sin listas enlazadas)
basico = {101, 102, 105, 108}
premium = {105, 108, 110, 112}

ambos = basico & premium
solo_premium = premium - basico

print(f"Punto 1a (Intersección): {ambos}")
print(f"Punto 1b (Diferencia): {solo_premium}")


# --- ESTRUCTURAS PARA LOS DEMÁS PUNTOS ---

class Nodo:
    def __init__(self, id_user):
        self.id_user = id_user
        self.siguiente = None

class ConjuntoEnlazado:
    def __init__(self):
        self.cabeza = None

    # PUNTO 2: Agregar sin duplicados (Recursivo)
    def agregar(self, id_user):
        # Primero verificamos si ya existe para cumplir la regla de conjunto
        if not self.existe(id_user):
            self.cabeza = self._agregar_rec(self.cabeza, id_user)

    def _agregar_rec(self, actual, id_user):
        if actual is None:
            return Nodo(id_user)
        actual.siguiente = self._agregar_rec(actual.siguiente, id_user)
        return actual

    # PUNTO 4: Pertenencia (Recursivo) - Se necesita para el Punto 2
    def existe(self, id_user, actual=None):
        # La primera vez que se llama, empezamos por la cabeza
        if actual is None and self.cabeza is not None:
            actual = self.cabeza
        
        if actual is None: # Si la lista está vacía o llegamos al final
            return False
        if actual.id_user == id_user:
            return True
        return self.existe(id_user, actual.siguiente)

    # PUNTO 3: Intersección Manual (Contar comunes)
    def contar_comunes(self, otra_lista):
        return self._contar_rec(self.cabeza, otra_lista)

    def _contar_rec(self, actual, otra_lista):
        if actual is None:
            return 0
        
        # Si el ID del nodo actual existe en la otra lista enlazada
        valor = 1 if otra_lista.existe(actual.id_user) else 0
        return valor + self._contar_rec(actual.siguiente, otra_lista)

    # PUNTO 5: Diferencia con Baneados (Eliminar Recursivo)
    def eliminar_baneados(self, set_baneados):
        self.cabeza = self._eliminar_rec(self.cabeza, set_baneados)

    def _eliminar_rec(self, nodo, baneados):
        if nodo is None:
            return None
        
        # Vamos al fondo de la lista
        nodo.siguiente = self._eliminar_rec(nodo.siguiente, baneados)
        
        # Al regresar, comprobamos si el ID está en el conjunto de baneados
        if nodo.id_user in baneados:
            return nodo.siguiente # Borramos el nodo
        return nodo

# --- PRUEBAS ---
lista_a = ConjuntoEnlazado()
lista_a.agregar(101)
lista_a.agregar(105)
lista_a.agregar(101) # No debería agregarse (duplicado)

lista_b = ConjuntoEnlazado()
lista_b.agregar(105)
lista_b.agregar(110)

print(f"¿Existe el 101?: {lista_a.existe(101)}")
print(f"Elementos en común entre listas: {lista_a.contar_comunes(lista_b)}")

baneados = {101, 999}
lista_a.eliminar_baneados(baneados)
print("Limpieza de baneados realizada.")


"""
═══════════════════════════════════════════════════════════════════════════════
                 SIMULACRO DE PARCIAL FINAL: ESTRUCTURAS DE DATOS
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
La tienda "Eco-Store" maneja productos orgánicos. Debes gestionar el stock 
usando conjuntos de Python para análisis rápido y Listas Enlazadas para 
la estructura permanente.

REQUERIMIENTOS:
---------------
PUNTO 1 (1.0): ANÁLISIS DE CATEGORÍAS (Conjuntos Nativos)
Dadas dos categorías de productos:
frutas = {"Manzana", "Banano", "Fresa", "Uva"}
organicos = {"Manzana", "Lechuga", "Fresa", "Zanahoria"}

a) Encuentra los productos que son frutas Y también son orgánicos.
b) Encuentra los productos que son frutas pero NO están en la categoría orgánicos.

PUNTO 2 (1.0): DISEÑO Y REGEX (Listas Enlazadas)
Crea la clase Producto (Nodo) y la clase Inventario (Lista).
- El código del producto debe validarse con REGEX: 3 letras y 2 números (Ej: PRO12).

PUNTO 3 (1.0): INSERCIÓN SIN DUPLICADOS (Recursivo)
Implementa el método agregar_producto(). 
- OBLIGATORIO: Si el nombre del producto ya existe, no se agrega.
- OBLIGATORIO: Usar recursividad.

PUNTO 4 (1.0): DIFERENCIA SIMÉTRICA MANUAL (Recursivo)
Implementa un método que reciba otra Lista Enlazada y retorne una NUEVA 
con los productos que están en una o en otra, pero NO en ambas.

PUNTO 5 (1.0): PREDICCIÓN DE VENTAS (Memorización)
Implementa la serie de Fibonacci con memorización para predecir las ventas 
del mes 'n', donde ventas(n) = ventas(n-1) + ventas(n-2).
═══════════════════════════════════════════════════════════════════════════════
"""
import re

# ==========================================
# PUNTO 1: Conjuntos Nativos
# ==========================================
frutas = {"Manzana", "Banano", "Fresa", "Uva"}
organicos = {"Manzana", "Lechuga", "Fresa", "Zanahoria"}

interseccion = frutas & organicos # En ambos
solo_frutas = frutas - organicos   # Frutas que no son orgánicas

print(f"1a. Intersección: {interseccion}")
print(f"1b. Diferencia: {solo_frutas}")


# ==========================================
# PUNTO 2 y 3: Nodos y Conjunto Enlazado
# ==========================================
class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.cabeza = None
        self.memo = {} # Para Punto 5

    # Validación Regex
    def validar_codigo(self, codigo):
        patron = r"^[A-Z]{3}\d{2}$"
        return bool(re.match(patron, codigo))

    # Agregar sin duplicados RECURSIVO
    def agregar(self, nombre, codigo):
        if not self.validar_codigo(codigo):
            return print(f"Código {codigo} inválido.")
        
        # Primero buscamos si ya existe el nombre (Regla de Conjunto)
        if not self._buscar_nombre(self.cabeza, nombre):
            self.cabeza = self._insertar_rec(self.cabeza, nombre, codigo)

    def _buscar_nombre(self, nodo, nombre):
        if nodo is None: return False
        if nodo.nombre == nombre: return True
        return self._buscar_nombre(nodo.siguiente, nombre)

    def _insertar_rec(self, nodo, nombre, codigo):
        if nodo is None: return Producto(nombre, codigo)
        nodo.siguiente = self._insertar_rec(nodo.siguiente, nombre, codigo)
        return nodo

    # ==========================================
    # PUNTO 4: Diferencia Simétrica Manual
    # ==========================================
    # (Elementos que no se repiten entre dos listas)
    def diferencia_simetrica(self, otra_lista):
        nueva = Inventario()
        # Pasamos por la lista A y agregamos si NO está en B
        self._verificar_y_copiar(self.cabeza, otra_lista, nueva)
        # Pasamos por la lista B y agregamos si NO está en A
        self._verificar_y_copiar(otra_lista.cabeza, self, nueva)
        return nueva

    def _verificar_y_copiar(self, actual, lista_comparar, lista_nueva):
        if actual is None: return
        if not lista_comparar._buscar_nombre(lista_comparar.cabeza, actual.nombre):
            lista_nueva.agregar(actual.nombre, actual.codigo)
        self._verificar_y_copiar(actual.siguiente, lista_comparar, lista_nueva)

    # ==========================================
    # PUNTO 5: Fibonacci con Memorización
    # ==========================================
    def prediccion_ventas(self, n):
        if n <= 1: return n
        if n in self.memo: return self.memo[n]
        
        self.memo[n] = self.prediccion_ventas(n-1) + self.prediccion_ventas(n-2)
        return self.memo[n]

# --- PRUEBAS ---
inv_a = Inventario()
inv_a.agregar("Manzana", "ORG01")
inv_a.agregar("Banano", "ORG02")

inv_b = Inventario()
inv_b.agregar("Manzana", "ORG01")
inv_b.agregar("Uva", "ORG03")

# Diferencia simétrica debería dar: Banano y Uva
inv_final = inv_a.diferencia_simetrica(inv_b)

print(f"Ventas predichas mes 10: {inv_a.prediccion_ventas(10)}")


"""
Diferencia Simétrica Manual: El secreto es hacer dos recorridos. Primero comparas la Lista A contra la B, y luego la B contra la A. Los elementos que "fallen" la búsqueda de existencia son los que van para la nueva lista.
Backtracking: Fíjate que en _insertar_rec el return nodo al final es vital. Si se te olvida, la lista se "desconecta" y pierdes los punteros.
Regex: No olvides el ^ y $. Si el profe te pide 3 letras y 2 números, el patrón es ^[A-Z]{3}\d{2}$.
"""