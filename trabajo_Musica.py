#Listas doblemente ligadas

class Nodo:
    def __init__(self, nombre,artista):
        self.nombre = nombre
        self.artista = artista
        self.anterior = None
        self.siguiente = None
        
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def esta_vacia(self):
        return self.cabeza is None 
    
    def insertarCancion_inicio(self, nombre, artista):
        nuevo = Nodo(nombre,artista)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            
    def insertarCancion_final(self,  dato):
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo 
            
    def eliminarCancion_inicio(self): #se eliminan las referencias mas no los nodos.
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            
    def eliminarCancion_final(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            
    def recorrerCancion_adelante(self):
        if self.esta_vacia():
            print("El album esta vacio ಠಿ_ಠ\n")
            return None
        
        print("⚙ Recorriendo el album al inicio espere por favor ⚙....\n 🛠🛒\n ...🎉 FIN🎉\n")
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ...(*￣０￣)ノ \n")
            actual = actual.siguiente
        print("\n...FIN...\n")
        
    def recorrerCancion_atras(self):
        if self.esta_vacia():
            print("La lista esta vacia ಠಿ_ಠ \n")
            return None
        
        print("⚙ Recorriendo el album hacia el final.. espere por favor ⚙....\n 🛠🛒\n ...🎉 FIN🎉\n")
        actual = self.cola
        while actual:
            print(actual.dato, end=" o(=•ェ•=)m \n")
            actual = actual.anterior
        print("\n...FIN...\n")
        
    def buscarCancion(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            
        return False                                 #ecuacion matematica (crecimiento lineal) f(n) = 1 + 4n + 1 = 2 + 4n = [n]
    
    
    def __len__(self): #devuelve un contador
        contador = 0
        actual = self.cabeza
        while  actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def __str__(self): #le da las indicaciones al print
        if self.esta_vacia():
            return "Lista de musica esta vacia"
        
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <==> ".join(elementos)
    
lista = ListaDoble()
lista.insertar_final(Die With A Smile (Lady Gaga & Bruno Mars))
lista.insertar_final(Gata Only (FloyyMenor & Cris Mj))
lista.insertar_final(70)
print(lista)

lista.insertar_inicio(48)
print(lista)

lista.recorrer_adelante()
lista.recorrer_atras()

print(f"El tamaño de la lista: {len(lista)}")

print(lista.buscar(50))