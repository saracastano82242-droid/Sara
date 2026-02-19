# Listas doblemente ligadas - VERSION RECURSIVA TOTAL

class Nodo:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista
        self.anterior = None
        self.siguiente = None


class reproductorMusical:
    def __init__(self):
        self.cabeza = None
        self.actual = None
        self.cola = None

    # ---------------------------
    # UTILIDADES BÁSICAS
    # ---------------------------

    def esta_vacia(self):
        return self.cabeza is None

    # ---------------------------
    # INSERTAR
    # ---------------------------

    def insertarCancion_inicio(self, nombre, artista):
        nuevo = Nodo(nombre, artista)

        if self.esta_vacia():
            self.cabeza = self.cola = self.actual = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertarCancion_final(self, nombre, artista):
        nuevo = Nodo(nombre, artista)

        if self.esta_vacia():
            self.cabeza = self.cola = self.actual = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    # ---------------------------
    # ELIMINAR
    # ---------------------------

    def eliminarCancion_inicio(self):
        if self.esta_vacia():
            return

        if self.cabeza == self.cola:
            self.cabeza = self.cola = self.actual = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

    def eliminarCancion_final(self):
        if self.esta_vacia():
            return

        if self.cabeza == self.cola:
            self.cabeza = self.cola = self.actual = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None

    # ---------------------------
    # RECORRER ADELANTE (REC)
    # ---------------------------

    def recorrerCancion_adelante(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("\n🎵 Recorriendo hacia adelante 🎵\n")
        self._recorrer_adelante_rec(self.cabeza)
        print("\n--- FIN ---\n")

    def _recorrer_adelante_rec(self, nodo):
        if nodo is None:
            return
        print(f"{nodo.nombre} - {nodo.artista}")
        self._recorrer_adelante_rec(nodo.siguiente)

    # ---------------------------
    # RECORRER ATRÁS (REC)
    # ---------------------------

    def recorrerCancion_atras(self):
        if self.esta_vacia():
            print("Lista vacía")
            return
        print("\n🎵 Recorriendo hacia atrás 🎵\n")
        self._recorrer_atras_rec(self.cola)
        print("\n--- FIN ---\n")

    def _recorrer_atras_rec(self, nodo):
        if nodo is None:
            return
        print(f"{nodo.nombre} - {nodo.artista}")
        self._recorrer_atras_rec(nodo.anterior)

    # ---------------------------
    # BUSCAR (REC)
    # ---------------------------

    def buscarCancion(self, nombre, artista):
        return self._buscar_rec(self.cabeza, nombre, artista)

    def _buscar_rec(self, nodo, nombre, artista):
        if nodo is None:
            return False
        if nodo.nombre == nombre and nodo.artista == artista:
            return True
        return self._buscar_rec(nodo.siguiente, nombre, artista)

    # ---------------------------
    # LONGITUD (REC)
    # ---------------------------

    def __len__(self):
        return self._len_rec(self.cabeza)

    def _len_rec(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._len_rec(nodo.siguiente)

    # ---------------------------
    # MOSTRAR ACTUAL
    # ---------------------------

    def mostrar_cancionActual(self):
        if self.actual is None:
            print("No hay canción en reproducción")
        else:
            print(f"🎶 Reproduciendo: {self.actual.nombre} - {self.actual.artista}")

    # ---------------------------
    # SIGUIENTE / ANTERIOR
    # ---------------------------

    def siguiente_cancion(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("Ya estás en la última canción")
        self.mostrar_cancionActual()

    def cancion_anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("Ya estás en la primera canción")
        self.mostrar_cancionActual()

    # ---------------------------
    # MENU RECURSIVO 🔥
    # ---------------------------

    def menu_Musical(self):
        print("\n====== REPRODUCTOR MUSICAL ======")
        print("1. Mostrar canciones")
        print("2. Buscar canción")
        print("3. Agregar canción")
        print("4. Eliminar canción")
        print("5. Mostrar canción actual")
        print("6. Siguiente canción")
        print("7. Canción anterior")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            self.recorrerCancion_adelante()

        elif opcion == "2":
            nombre = input("Nombre: ")
            artista = input("Artista: ")
            if self.buscarCancion(nombre, artista):
                print("Canción encontrada 🎶")
            else:
                print("No encontrada")

        elif opcion == "3":
            nombre = input("Nombre: ")
            artista = input("Artista: ")
            ubicacion = input("¿Inicio o Final? (i/f): ")
            if ubicacion == "i":
                self.insertarCancion_inicio(nombre, artista)
            else:
                self.insertarCancion_final(nombre, artista)

        elif opcion == "4":
            ubicacion = input("¿Inicio o Final? (i/f): ")
            if ubicacion == "i":
                self.eliminarCancion_inicio()
            else:
                self.eliminarCancion_final()

        elif opcion == "5":
            self.mostrar_cancionActual()

        elif opcion == "6":
            self.siguiente_cancion()

        elif opcion == "7":
            self.cancion_anterior()

        elif opcion == "8":
            print("Saliendo del reproductor...")
            return  # CASO BASE DEL MENU

        else:
            print("Opción inválida")

        # llamada recursiva del menú
        self.menu_Musical()


# ---------------------------
# PRUEBA
# ---------------------------

lista = reproductorMusical()

lista.insertarCancion_final("Die With A Smile", "Lady Gaga & Bruno Mars")
lista.insertarCancion_final("Gata Only", "FloyyMenor & Cris Mj")
lista.insertarCancion_final("Ma Meilleure Ennemie", "Stromae & Pomme")
lista.insertarCancion_final("Bajo El Agua", "Manuel Medrano")

lista.menu_Musical()
