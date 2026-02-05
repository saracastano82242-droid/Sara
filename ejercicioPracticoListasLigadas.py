class Nodo:
    def __init__ (self,nom, cc):
        self.nom = nom
        self.cc = cc
        self.siguiente = None

class Lista:
    def __init__ (self):
        self.cabeza = None

    def agregarNodoAlfinal(self, nom, cc):
        
        nodo = Nodo(nom, cc)

        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente != None:
                actual = actual.siguiente

            actual.siguiente =nodo

    print ("Nodo agregado exitosamente 👌")

    def mostrarLista(self):
        actual = self.cabeza #se ejecuta una vez
        while actual: #se ejecutara segun cuantos nodos tenga (este caso 3)
            print(actual.nom, end="<---")
            print(actual.cc, end="<---")
            print("-->")
            actual = actual.siguiente
        print("FIN")

    def prioridad(self, nom, cc, prioridad):
        nodo = Nodo(nom, cc, prioridad)

        if self.cabeza == None:
            self.cabeza = Nodo
            return
        elif self.cabeza.prioridad > prioridad:
            nodo.siguiente = self.cabeza
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nodo.siguiente = actual.siguiente
            actual.siguiente = nodo


lista = Lista()
lista.agregarNodoAlfinal("Sara", 1036252584)
lista.agregarNodoAlfinal("Daniel", 156615486)

lista.mostrarLista()