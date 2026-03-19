#en un conjunto no  hay duplicados
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Conjuntos:
    def __init__(self, elementos = None): #se puede crear un conjunto que ya tiene elementos
        self.cabeza = None
        self.tamaño = 0 #es para saber cuantos elemetos tenemos en el conjunto

        if elementos:
            for e in elementos:
                self.agregar(e) #esta validando que si hay elemetos, entonces los agregamos al conjunto 
    
    def esta_vacio(self):
        return self.cabeza is None #si esta vacio nos da true y si no, nos da false
    
    def cardinalidad(self): #es el tamaño, osea cuantos elementos tiene el conjunto
        return self.tamaño
    
     #buscara un elemeto en el conjunto, recorriendo la lista nodo por nodo, si alguno de los nodos es el elemento retorna true
     #si recorre todo y no lo encuentra, retorna false
    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x: #si alguno de los datos que estoy buscando es igual al que busco retornara true y si no sera false
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x): #metodo para agregar un nuevo metodo al conjunto, lo que hace es que si el elemento ya esta en el conjunto, no se puede agregar

        if self.pertenece(x):
            return  False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    def eliminar(self, x):

        if self.esta_vacio():
            return False
        
        if self.cabeza.dato == x:
            self.cabeza = self.cabeza.siguiente
            tamaño -= 1
            return True
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == x: #valida si el siguiente tiene el dato que estamos buscando 
                actual.siguiente = actual.siguiente.siguiente #esta eliminando al nodo encontrado 
                self.tamaño -= 1
                return True
            actual = actual.siguiente
        return False
    
    def union(self, otro): 
        
        #estamos creando un nuevo conjunto para guardar el resultado de la union
        resultado = Conjuntos()

        #recorremos todos los elementos del conjunto en el que estoy trabajando y los agrego a resultado
        actual = self.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        #recorremos todos los elementos del otro conjunto y los agrego a resultado
        actual = otro.cabeza
        while actual:
            resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado
    
    def interseccion(self, otro): # vamos a validar si en los otros conjuntos hay elementos repetidos,
        #si los hay, vamos a separarlos en un nuevo conjunto 

        resultado = Conjuntos()

        actual = self.cabeza
        while actual:
            if otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)
            actual = actual.siguiente

        return resultado
    
    def diferencia(self, otro): # vamos a validar que los elementos que pertenescan a un conjunto no pertenescan al otro
        resultado = Conjuntos()
        actual = self.cabeza

        #recorremos todo el conjunto
        while actual:
            #y si no pertenece al otro conjunto, lo agrego al resultado
            if not otro.pertenece(actual.dato):
                resultado.agregar(actual.dato)

            actual = actual.siguiente
        return resultado
    
    def diferencia_simetrica(self, otro):
        return self.diferencia(otro).union(otro.diferencia(self)) #esta seria la union de las direfencias de los dos conjuntos 
    
    """
    otra pocible solucion a la diferencia simetrica
        union = self.union(otro)
        interseccion = self.interseccion(otro)
        return union.diferencia(interseccion)
    """

    def a_lista(self):

        resultado = []

        actual = self.cabeza
        while actual: #estamos convirtendo el conjunto a una lista
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado 