#invertir un string usando recursividad
#hola -> aloh

def invertir_string(s):
    if len(s) <= 0:
        return s
    return invertir_string(s[1:]) + s[0]

def es_palindromo(s):
    if len(s) <= 1:
        return True 
    if s[0] != s[-1]:
        return False
    return es_palindromo(s[1:-1])



# Ejemplo de uso
cadena = "reconocer"
cadena_invertida = invertir_string(cadena)
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {cadena_invertida}")
palindromo = "reconocer"
no_palindromo = "guatarimicaro"
print(f"¿'{palindromo}' es un palíndromo? {es_palindromo(palindromo)}")
print(f"¿'{no_palindromo}' es un palíndromo? {es_palindromo(no_palindromo)}")

#contar cuantas veces aparece un caracter en una cadena usando recursividad
def contar_caracter(s, caracter):
    if len(s) == 0:
        return 0
    count = 1 if s[0] == caracter else 0
    return count + contar_caracter(s[1:], caracter) # [1:] es para tomar la subcadena desde el segundo caracter hasta el final
# Ejemplo de uso
cadena = "algotimos de programacion"
caracter = "a"
conteo = contar_caracter(cadena, caracter)  
print(f"El caracter '{caracter}' aparece {conteo} veces en la cadena '{cadena}'.")

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0 
        return 1 + self._contar_nodos_recursivo(nodo.siguiente)

    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.cabeza) 
    
    def _buscar_recursivo(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        return self._buscar_recursivo(nodo.siguiente, dato)
    
    def buscar(self, dato):
        return self._buscar_recursivo(self.cabeza, dato)