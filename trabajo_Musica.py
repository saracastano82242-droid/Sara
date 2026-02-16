#Listas doblemente ligadas

from tkinter import Menu


class Nodo:
    def __init__(self, nombre,artista):
        self.nombre = nombre
        self.artista = artista
        self.anterior = None
        self.siguiente = None
        
class reproductorMusical:
    def __init__(self):
        self.cabeza = None
        self.actual = None
        self.cola = None

    def mostrar_cancionActual(self):
        if self.actual is None:
            print("Actualmente no hay canciónes en reproduccion.\n")
        else:
            print(f"Se esta reproduciendo: {self.actual.nombre} de {self.actual.artista}\n")
    
    def siguiente_cancion(self):
        if self.actual is None:
            print("No hay canciónes en el reproductor（︶^︶）\n")
        elif self.actual.siguiente is None:
            print("Ya estas en la ultima cancion de la lista🎶\n")
        else:
            self.actual = self.actual.siguiente
            self.mostrar_cancionActual()

    def cancion_anterior(self):
        if self.actual is None:
            print("No hay canciónes en el reproductor OwO\n")
        elif self.actual.anterior is None:
            print("Ya estas en la primera cancion de la lista✅\n")
        else:
            self.actual = self.actual.anterior
            self.mostrar_cancionActual()
        
    def esta_vacia(self):
        return self.cabeza is None 
    
    def insertarCancion_inicio(self, nombre, artista):
        nuevo = Nodo(nombre,artista)
        
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            
    def insertarCancion_final(self,  nombre, artista):
        nuevo = Nodo(nombre, artista)
        
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo 
            
    def eliminarCancion_inicio(self): #se eliminan las referencias mas no los nodos.
        if self.esta_vacia():
            return None
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            
    def eliminarCancion_final(self):
        if self.esta_vacia():
            return None
        
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
            
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            
    def recorrerCancion_adelante(self):
        if self.esta_vacia():
            print("¡PAREN TODOOO!... \n ¡Esta lista esta vacia ಠಿ_ಠ! \n")
            return None
        
        print("⚙ Recorriendo el reproductor al inicio espere por favor ⚙....\n 🛠🛒\n")
        actual = self.cabeza
        while actual:
            print(f"{actual.nombre}",{actual.artista}, end=" ...(*￣０￣)ノ \n")
            actual = actual.siguiente
        print("\n...🎉 FIN🎉...\n")
        
    def recorrerCancion_atras(self):
        if self.esta_vacia():
            print("\n¡PAREN TODOOO!... \n ¡Esta lista esta vacia ಠಿ_ಠ! \n")
            return None
        
        print("\n⚙ Recorriendo el reproductor hacia el final.. espere por favor ⚙....\n 🛠🛒\n")
        actual = self.cola
        while actual:
            print(f"{actual.nombre}",{actual.artista}, end=" o(=•ェ•=)m \n")
            actual = actual.anterior
        print("\n...🎉 FIN🎉...\n")
        
    def buscarCancion(self, nombre, artista):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre and actual.artista == artista:
                return True
            actual = actual.siguiente
            
        return False   #ecuacion matematica (crecimiento lineal) f(n) = 1 + 4n + 1 = 2 + 4n = [n]
    

    def menu_Musical(self):
        while True:
            print("⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂")
            print("⁂(👉ﾟヮﾟ)👉¡BIENVENIDO A TU REPRODUCTOR DE MUSICA FAVORITAA!👈(ﾟヮﾟ👈)⁂")
            print("⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂\n")
            print("1. Canciones disponibles (●'◡'●)\n")
            print("2. Buscar una cancion es especifico （*゜ー゜*）\n")
            print("3. Agregar una cancion al reproductor \^o^/\n")
            print("4. Eliminar una cancion del reproductor ⊙﹏⊙∥ \n")
            print("5. Mostrar la cancion actual (⌐■_■) \n")
            print("6. Siguiente cancion (☞ﾟヮﾟ)☞ \n")
            print("7. Cancion anterior ☜(ﾟヮﾟ☜) \n")
            print("8. Salir del reproductor （︶^︶) \n")
            
        
            opcion = input("Selecciona una opción: \n")

            match opcion:
                case "1":
                    self.recorrerCancion_adelante()

                case "2":
                    nombre = input("Ingrese el nombre de la cancion buscada: ")
                    artista = input("¿Cual es el artista?: ")
                    if self.buscarCancion(nombre, artista):
                        print("\n¡MISION CUMPLIDA!\n La cancion ha sido encontrada.🎶\n")
                    else:
                        print("\nOHH.. LO SIENTO, NO PUDE ENCONTRAR LA CANCION SOLICITADA...😢\n")

                case "3":
                    while True:
                        nombre = input("Ingrese el nombre de la cancion por favor: ")
                        artista = input("Ingrese por favor el artista: ")
                        ubicacion = input("Donde las desea agregar ¿Inicio o Final? (i/f): ")

                        if ubicacion == "i":
                            self.insertarCancion_inicio(nombre, artista)
                            print("\nBuenas noticias!!\n La cancion a sido agregada exitosamente.\n")
                            break
                        elif ubicacion == "f":
                            self.insertarCancion_final(nombre,artista)
                            print("\nBuenas noticias!!\n La cancion a sido agregada exitosamente.\n")
                            break
                        else:
                            print("\n⚠️ ERROR ⚠️\n Opcion no valida, ingrese por favor (i/f)\n")

                case "4":
                    while True:
                        ubicacion = input("¿Desea eliminar la cancion del inicio o final? (i/f): ").lower()   #"lower" es para convertir la respuesta a minuscula y asi evitar errores por mayusculas

                        if ubicacion == "i":
                            self.eliminarCancion_inicio()
                            print("Cancion eliminada exitosamente")
                            break
                        elif ubicacion == "f":
                            self.eliminarCancion_final()
                            print("Cancion eliminada exitosamente")
                            break
                        else:
                            print("\n⚠️ ERROR ⚠️\n Opcion no valida, ingrese por favor (i/f)\n")
                case "5":
                    self.mostrar_cancionActual()

                case "6":
                    self.siguiente_cancion()

                case "7":
                    self.cancion_anterior()

                case "8":
                    print("Saliendo...\n Has salido correctamente del reproductor 👌\n")
                    break
                
                case _:
                    print("¡UPSHH!🚩\n ⚠️ HUBO UN ERROR INESPERADO ⚠️\n YA LO ESTAMOS SOLUCIONANDO PACIENCIA POR FAVOR 🚧\n Gracias por su espera, por favor continue✅...")
    
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
            elementos.append(str(actual.nombre))
            elementos.append(str(actual.artista))
            actual = actual.siguiente
        return " <==> ".join(elementos)
    
lista = reproductorMusical()
lista.insertarCancion_final("\n 1. Die With A Smile", "Lady Gaga & Bruno Mars\n")
lista.insertarCancion_final("\n 2. Gata Only ", "FloyyMenor & Cris Mj\n")
lista.insertarCancion_final("\n 3. Ma Meilleure Ennemie", "Stromae & Pomme\n")
lista.insertarCancion_final("\n 4. Bajo El Agua", "Manuel Medrano\n")

lista.menu_Musical()

lista.mostrar_cancionActual()
lista.siguiente_cancion()
lista.cancion_anterior()

lista.insertarCancion_inicio("")

lista.recorrerCancion_adelante()
lista.recorrerCancion_atras()


print("Buscando la cancion... espere por favor... ")
print(lista.buscarCancion())