#Listas doblemente ligadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None
        
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def esta_vacia(self):
        return self.cabeza is None #si se cumple retorna un "true" y si no un false
    
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            
    def insertar_final(self,  dato):
        nuevo = Nodo(dato)
        
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo 
            
    def eliminar_inicio(self): #se eliminan las referencias mas no los nodos.
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            
    def eliminar_final(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza.dato == self.cola.dato:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            
    def recorrer_adelante(self):
        if self.esta_vacia():
            print("La lista esta vacia ( ´･-･)ﾉ(._.`)\n")
            return None
        
        print("Recorriendo Inicio 🛠... FIN🎉\n")
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" (☞ﾟヮﾟ)☞ \n")
            actual = actual.siguiente
        print("\n...FIN...\n")
        
    def recorrer_atras(self):
        if self.esta_vacia():
            print("La lista esta vacia ( ´･-･)ﾉ(._.`)\n")
            return None
        
        print("Recorriendo hacia atras 🛠... FIN🎉\n")
        actual = self.cola
        while actual:
            print(actual.dato, end=" ☜(ﾟヮﾟ☜) \n")
            actual = actual.anterior
        print("\n...FIN...\n")
        
    def buscar(self, dato):
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
            return "Lista vacia"
        
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <==> ".join(elementos)
    
lista = ListaDoble()
lista.insertar_final(50)
lista.insertar_final(60)
lista.insertar_final(70)
print(lista)

lista.insertar_inicio(48)
print(lista)

lista.recorrer_adelante()
lista.recorrer_atras()

print(f"El tamaño de la lista: {len(lista)}")

print(lista.buscar(50))