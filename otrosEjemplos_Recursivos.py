def longitud(nodo):
"""Cuenta nodos de forma recursiva."""
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