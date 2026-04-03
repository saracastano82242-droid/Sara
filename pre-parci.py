"""
═══════════════════════════════════════════════════════════════════════════════
       EXAMEN PARCIAL: ALGORITMOS Y ESTRUCTURAS DE DATOS II
             TEMAS: CONJUNTOS, RECURSIVIDAD, REGEX, PILAS Y COLAS
═══════════════════════════════════════════════════════════════════════════════
"""

import re

# -----------------------------------------------------------------------------
# PARTE 1: CONJUNTOS (Lógica de Datos)
# -----------------------------------------------------------------------------
# Contexto: Gestión de una comunidad de desarrolladores.
# Dispones de tres grupos de interés:

python_devs = {"Ana", "Carlos", "Diana", "Eduardo", "Ivan"}
java_devs = {"Carlos", "Diana", "Juan", "Luis", "Maria"}
web_devs = {"Diana", "Eduardo", "Gabriel", "Karen", "Ivan"}

# RETO 1: 
# a) Encuentra los desarrolladores que saben los TRES lenguajes.
# b) Encuentra los desarrolladores que saben Python pero NO saben Java.
# c) ¿Es el grupo de los que saben los tres lenguajes un subconjunto de python_devs? (Respuesta Booleana)

print("--- SOLUCIÓN RETO 1 ---")
# Escribe tu código aquí:


# -----------------------------------------------------------------------------
# PARTE 2: RECURSIVIDAD (Lógica Matemática)
# -----------------------------------------------------------------------------
# RETO 2:
# Crea una función recursiva llamada 'suma_digitos(n)' que reciba un número
# entero positivo y retorne la suma de sus dígitos.
# Ejemplo: suma_digitos(123) -> 1 + 2 + 3 = 6

def suma_digitos(n):
    # Escribe tu código aquí:
    pass

print("\n--- PRUEBA RETO 2 ---")
# print(suma_digitos(456)) # Debería imprimir 15


# -----------------------------------------------------------------------------
# PARTE 3: EXPRESIONES REGULARES (Validación)
# -----------------------------------------------------------------------------
# RETO 3:
# Crea un patrón de Regex para validar una "Clave de Empleado".
# Reglas: Debe empezar con 2 letras mayúsculas, seguido de un guion '-',
# y terminar con exactamente 4 números.
# Ejemplo válido: "AB-1234"

def validar_clave(clave):
    patron = r"" # Escribe tu patrón aquí
    if re.match(patron, clave):
        return True
    return False

print("\n--- PRUEBA RETO 3 ---")
# print(validar_clave("TY-9081")) # True
# print(validar_clave("abc-123")) # False


# -----------------------------------------------------------------------------
# PARTE 4: PILAS Y COLAS (Estructuras de Datos)
# -----------------------------------------------------------------------------
# RETO 4: 
# Imagina que gestionas los procesos de una impresora. 
# a) Si los documentos deben imprimirse en el orden en que llegaron, 
#    ¿qué estructura usarías (Pila o Cola)?
# b) Implementa una simulación simple usando una lista de Python para 
#    añadir 3 documentos ("Doc1", "Doc2", "Doc3") y luego "imprimirlos" 
#    mostrando cuál sale primero.

print("\n--- SOLUCIÓN RETO 4 ---")
# Escribe tu código aquí:


# -----------------------------------------------------------------------------
# PARTE 5: PREGUNTAS TEÓRICAS (Selección Múltiple)
# -----------------------------------------------------------------------------
"""
PREGUNTA A: ¿Cuál es la principal característica de una Pila (Stack)?
1. FIFO (First In, First Out)
2. LIFO (Last In, First Out)
3. Ordenamiento aleatorio

PREGUNTA B: En recursividad, ¿qué sucede si falta el "Caso Base"?
1. El programa termina más rápido.
2. Se produce un error de 'RecursionError' (Stack Overflow).
3. La función devuelve None automáticamente.

PREGUNTA C: ¿Qué operador de conjuntos en Python representa la Intersección?
1. |
2. -
3. &
"""

# =============================================================================
# SECCIÓN DE RESPUESTAS (Míralas solo después de terminar)
# =============================================================================
"""
SOLUCIONES:

RETO 1 (Conjuntos):
a) tres_lenguajes = python_devs & java_devs & web_devs
b) solo_python = python_devs - java_devs
c) print(tres_lenguajes <= python_devs)  # True

RETO 2 (Recursividad):
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

RETO 3 (Regex):
patron = r"^[A-Z]{2}-\d{4}$"

RETO 4 (Estructuras):
a) Cola (Queue).
b) 
cola = []
cola.append("Doc1")
cola.append("Doc2")
cola.append("Doc3")
print(cola.pop(0)) # Sale "Doc1"

TEORÍA:
Pregunta A: 2 (LIFO)
Pregunta B: 2 (RecursionError)
Pregunta C: 3 (&)
"""

"""
═══════════════════════════════════════════════════════════════════════════════
                    EXAMEN PARCIAL 2: ESTRUCTURAS DE DATOS II
                          SISTEMA INTEGRADO "CYBER-LOG"
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Has sido contratado por "Cyber-Log", una empresa de ciberseguridad. 
Debes implementar un sistema que gestione logs de errores, valide formatos 
de usuarios y procese tareas pendientes usando estructuras avanzadas.

TEMAS A EVALUAR:
1. Conjuntos (Sets) - Análisis de incidencias.
2. Expresiones Regulares (Regex) - Validación de credenciales.
3. Pilas (Stacks) - Historial de navegación (Undo).
4. Colas (Queues) - Procesamiento de tickets de soporte.
5. Recursividad - Análisis de profundidad de archivos.

INSTRUCCIONES:
--------------
- Completa el código en las secciones marcadas como "TU CÓDIGO AQUÍ".
- Puedes ejecutar el script para probar tus soluciones.
- Al final del archivo encontrarás las respuestas para autoevaluarte.

═══════════════════════════════════════════════════════════════════════════════
"""

import re

# =============================================================================
# PUNTO 1: ANÁLISIS DE INCIDENCIAS (CONJUNTOS) - [Valor: 1.0]
# =============================================================================
# Se tienen dos servidores con listas de IPs que han intentado ataques.

ips_servidor_A = {"192.168.1.1", "10.0.0.5", "172.16.0.10", "192.168.1.50"}
ips_servidor_B = {"192.168.1.1", "10.0.0.8", "172.16.0.10", "8.8.8.8"}

print("--- PUNTO 1: CONJUNTOS ---")
# a) Encuentra las IPs que atacaron a AMBOS servidores (Intersección).
# b) Encuentra las IPs que son EXCLUSIVAS del servidor A.
# c) Crea un catálogo total de IPs únicas que atacaron la empresa.

# TU CÓDIGO AQUÍ:


# =============================================================================
# PUNTO 2: VALIDACIÓN DE USUARIOS (REGEX) - [Valor: 1.0]
# =============================================================================
# El sistema solo permite usuarios con el formato: 
# "USR" + 4 números + "_" + 2 letras minúsculas (Ejemplo: USR1234_ab)

def validar_usuario(usuario):
    # Define el patrón Regex correcto:
    patron = r"" # TU CÓDIGO AQUÍ
    return bool(re.match(patron, usuario))

print("\n--- PUNTO 2: REGEX ---")
# print(f"¿USR9999_xy es válido?: {validar_usuario('USR9999_xy')}") # Debería ser True
# print(f"¿usr1234_AB es válido?: {validar_usuario('usr1234_AB')}") # Debería ser False


# =============================================================================
# PUNTO 3: HISTORIAL Y TICKETS (PILAS Y COLAS) - [Valor: 1.0]
# =============================================================================
# Implementa la lógica básica de una Pila para "Deshacer" y una Cola para "Tickets".

print("\n--- PUNTO 3: PILAS Y COLAS ---")

# a) PILA (Historial de comandos): Agrega 'SCAN' y 'FIX'. Luego elimina el último.
pila_comandos = []
# TU CÓDIGO AQUÍ (Usa append y pop)


# b) COLA (Tickets de soporte): Entra 'Ticket_1' y 'Ticket_2'. Atiende al primero.
cola_tickets = []
# TU CÓDIGO AQUÍ (Usa append y pop(0))


# =============================================================================
# PUNTO 4: BÚSQUEDA DE VIRUS (RECURSIVIDAD) - [Valor: 1.0]
# =============================================================================
# Implementa una función recursiva que sume el tamaño de archivos en una 
# estructura de carpetas anidadas (representada por una lista de listas).
# Ejemplo: [10, [20, 5], 30] -> Total: 65

def calcular_peso_total(lista_archivos):
    # TU CÓDIGO AQUÍ:
    pass

print("\n--- PUNTO 4: RECURSIVIDAD ---")
# sistema_archivos = [100, [50, [25, 25]], 200]
# print(f"Peso total: {calcular_peso_total(sistema_archivos)}") # Debería ser 400


# =============================================================================
# PUNTO 5: PREGUNTAS DE RESPUESTA BREVE - [Valor: 1.0]
# =============================================================================
"""
RESPONDE AQUÍ:

1. ¿Cuál es la diferencia técnica entre usar lista.pop() y lista.pop(0)?
   R: 

2. En una expresión regular, ¿qué significa el símbolo '^' al inicio?
   R: 

3. ¿Por qué una función recursiva sin 'Caso Base' causa un error de memoria?
   R: 
"""

# ═══════════════════════════════════════════════════════════════════════════════
#                      SOLUCIONES (PARA AUTOEVALUACIÓN)
# ═══════════════════════════════════════════════════════════════════════════════
"""
PUNTO 1:
a) comunes = ips_servidor_A & ips_servidor_B
b) solo_A = ips_servidor_A - ips_servidor_B
c) todas = ips_servidor_A | ips_servidor_B

PUNTO 2:
patron = r"^USR\d{4}_[a-z]{2}$"

PUNTO 3:
a) pila_comandos.append('SCAN'); pila_comandos.append('FIX'); ultimo = pila_comandos.pop()
b) cola_tickets.append('Ticket_1'); cola_tickets.append('Ticket_2'); primero = cola_tickets.pop(0)

PUNTO 4:
def calcular_peso_total(lista):
    total = 0
    for elemento in lista:
        if isinstance(elemento, list):
            total += calcular_peso_total(elemento)
        else:
            total += elemento
    return total

PUNTO 5:
1. pop() elimina el último (O(1) - Pila), pop(0) elimina el primero y desplaza el resto (O(n) - Cola).
2. Indica que la coincidencia debe empezar exactamente al inicio de la cadena.
3. Porque las llamadas se apilan infinitamente en el 'Stack' de ejecución hasta agotarlo (Stack Overflow).
"""

"""
═══════════════════════════════════════════════════════════════════════════════
                    QUIZ 1 - ESTRUCTURAS DE DATOS AVANZADAS
                                  EXAMEN C
                    Sistema de Monitoreo "Cyber-Sentinel"
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
La agencia "Cyber-Sentinel" necesita un sistema para gestionar logs de ataques.
Debes implementar una estructura de Lista Enlazada para almacenar "Alertas".
Cada alerta tiene un código de amenaza, nivel de riesgo (1-10) y origen (IP).

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Alerta) y la clase Lista (HistorialAlertas).
2. Usar RECURSIVIDAD en los métodos donde se indique.
3. Usar EXPRESIONES REGULARES para validar el código de amenaza.
4. Implementar PILAS y COLAS para procesos específicos de respuesta.
5. Usar CONJUNTOS para análisis de duplicados.
6. Tiempo: 90 minutos.

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO Y VALIDACIÓN (REGEX)
------------------------------------------
a) Clase NODO (Alerta):
   - Almacena: código, riesgo (1-10), ip_origen, siguiente.
   
b) Clase LISTA (HistorialAlertas):
   - El método agregar() debe validar el código con REGEX: 
     Formato: "ATK" seguido de 3 números y un guion con una letra (Ej: ATK123-X).


PUNTO 2 (1.0): AGREGAR ORDENADO - RECURSIVO
-------------------------------------------
Las alertas deben guardarse de mayor a menor riesgo.
- OBLIGATORIO usar recursividad para encontrar la posición e insertar.


PUNTO 3 (1.0): FILTRADO DE IPs ÚNICAS - CONJUNTOS
-------------------------------------------------
Implementa un método que recorra la lista y retorne un SET (conjunto)
con todas las IPs de origen sin repetir.
- Puede ser iterativo o recursivo.


PUNTO 4 (1.0): RESPUESTA A INCIDENTES - PILAS Y COLAS
-----------------------------------------------------
a) Implementar un método 'generar_pila_reaccion()': Retorna una PILA con los
   códigos de las últimas 5 alertas (para análisis forense LIFO).
   
b) Implementar un método 'generar_cola_atencion()': Retorna una COLA con los
   códigos de alertas nivel 10 (para atención inmediata FIFO).


PUNTO 5 (1.0): ELIMINAR RIESGO BAJO - RECURSIVO
-----------------------------------------------
Implementa un método que elimine todas las alertas con riesgo menor a 3.
- OBLIGATORIO usar recursividad.
- Debe modificar la lista original.

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO

import re

# PUNTO 1: Clase Nodo
class Alerta:
    def __init__(self, codigo, riesgo, ip_origen):
        self.codigo = codigo
        self.riesgo = riesgo
        self.ip_origen = ip_origen
        self.siguiente = None

class HistorialAlertas:
    def __init__(self):
        self.cabeza = None

    # PUNTO 1.b: Validación con Regex
    def validar_codigo(self, codigo):
        # ^ indica inicio, \d{3} son 3 números, [A-Z] una letra mayúscula
        patron = r"^ATK\d{3}-[A-Z]$"
        return bool(re.match(patron, codigo))

    # PUNTO 2: Agregar Ordenado (Recursivo)
    def agregar(self, codigo, riesgo, ip_origen):
        if not self.validar_codigo(codigo):
            print(f"Código {codigo} inválido. No se agregó.")
            return

        nuevo = Alerta(codigo, riesgo, ip_origen)
        
        # Caso base: lista vacía o el nuevo tiene más riesgo que el primero
        if self.cabeza is None or riesgo > self.cabeza.riesgo:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            self._agregar_recursivo(self.cabeza, nuevo)

    def _agregar_recursivo(self, actual, nuevo):
        # Si llegamos al final o el siguiente tiene menos riesgo que el nuevo
        if actual.siguiente is None or nuevo.riesgo > actual.siguiente.riesgo:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    # PUNTO 3: IPs Únicas con Conjuntos
    def obtener_ips_unicas(self):
        ips = set() # Los conjuntos no permiten duplicados automáticamente
        actual = self.cabeza
        while actual:
            ips.add(actual.ip_origen)
            actual = actual.siguiente
        return ips

    # PUNTO 4: Pilas y Colas
    def generar_pila_reaccion(self):
        pila = []
        actual = self.cabeza
        cont = 0
        while actual and cont < 5:
            pila.append(actual.codigo) # LIFO: el último en entrar (append) es el primero en salir (pop)
            actual = actual.siguiente
            cont += 1
        return pila

    def generar_cola_atencion(self):
        cola = []
        actual = self.cabeza
        while actual:
            if actual.riesgo == 10:
                cola.append(actual.codigo) # FIFO: se saca con pop(0)
            actual = actual.siguiente
        return cola

    # PUNTO 5: Eliminar Riesgo Bajo (Recursivo)
    def eliminar_riesgo_bajo(self):
        self.cabeza = self._eliminar_rec(self.cabeza)

    def _eliminar_rec(self, nodo):
        if nodo is None:
            return None
        
        # Llamada recursiva hacia el final
        nodo.siguiente = self._eliminar_rec(nodo.siguiente)
        
        # Al regresar (backtracking), evaluamos si este nodo debe borrarse
        if nodo.riesgo < 3:
            return nodo.siguiente # Saltamos este nodo
        return nodo # Mantenemos este nodo

# --- PRUEBA DEL SISTEMA ---
sistema = HistorialAlertas()
sistema.agregar("ATK101-A", 5, "192.168.1.1")
sistema.agregar("ATK202-B", 10, "10.0.0.5")
sistema.agregar("ATK303-C", 2, "192.168.1.1") # Este se debería borrar luego
sistema.agregar("ATK404-D", 8, "172.16.0.5")

print(f"IPs detectadas: {sistema.obtener_ips_unicas()}")
sistema.eliminar_riesgo_bajo()
print("Sistema procesado (sin riesgo bajo).")
═══════════════════════════════════════════════════════════════════════════════
"""