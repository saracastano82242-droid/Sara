# ============================================================
# LISTA LIGADA PARA PASOS
# ============================================================

class NodoPaso:
    __slots__ = ("descripcion", "siguiente")

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.siguiente = None


class ListaPasos:
   
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    def agregar_paso(self, descripcion):
        nuevo = NodoPaso(descripcion)

        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

        self.tamano += 1

    def insertar_en_posicion(self, posicion, descripcion):
        if posicion < 0 or posicion > self.tamano:
            print("Posicion fuera de rango.")
            return False

        nuevo = NodoPaso(descripcion)

        if posicion == 0:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

            if self.tamano == 0:
                self.cola = nuevo

            self.tamano += 1
            return True

        actual = self.cabeza

        for _ in range(posicion - 1):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

        if nuevo.siguiente is None:
            self.cola = nuevo

        self.tamano += 1
        return True

    def eliminar_paso(self, posicion):
        if posicion < 1 or posicion > self.tamano:
            print("Posicion fuera de rango.")
            return False

        if posicion == 1:
            self.cabeza = self.cabeza.siguiente

            if self.tamano == 1:
                self.cola = None

            self.tamano -= 1
            return True

        actual = self.cabeza

        for _ in range(posicion - 2):
            actual = actual.siguiente

        nodo_eliminado = actual.siguiente
        actual.siguiente = nodo_eliminado.siguiente

        if nodo_eliminado == self.cola:
            self.cola = actual

        self.tamano -= 1
        return True

    def mostrar_pasos(self):
        if self.cabeza is None:
            print("Sin pasos registrados.")
            return

        actual = self.cabeza
        numero = 1

        while actual:
            print(f"{numero}. {actual.descripcion}")
            actual = actual.siguiente
            numero += 1

    def contar_pasos(self):
        return self.tamano

    def esta_vacia(self):
        return self.tamano == 0


# ============================================================
# CLASE RECETA
# ============================================================

class Receta:
    """
    Cada receta utiliza:
    - Set para ingredientes -> O(1)
    - Lista ligada para pasos
    """

    def __init__(self, nombre, categoria, tiempo_minutos):
        self.nombre = nombre.strip()
        self.categoria = categoria.strip().lower()
        self.tiempo_minutos = tiempo_minutos
        self.ingredientes = set()
        self.pasos = ListaPasos()

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.add(ingrediente.strip().lower())

    def agregar_varios_ingredientes(self, ingredientes):
        for ingrediente in ingredientes:
            self.agregar_ingrediente(ingrediente)

    def agregar_paso(self, descripcion):
        self.pasos.agregar_paso(descripcion.strip())

    def mostrar(self):
        print("\n" + "-" * 50)
        print(f"Receta: {self.nombre}")
        print(f"Categoria: {self.categoria}")
        print(f"Tiempo: {self.tiempo_minutos} minutos")

        print("\nIngredientes:")
        for ingrediente in sorted(self.ingredientes):
            print(f"- {ingrediente}")

        print(f"\nPasos ({self.pasos.contar_pasos()}):")
        self.pasos.mostrar_pasos()

        print("-" * 50)


# ============================================================
# ARBOL DE SUSTITUCIONES
# ============================================================

arbol_sustituciones = {
    "leche": ["leche de almendras", "leche de avena", "leche de coco"],
    "huevo": ["pure de manzana", "yogur natural"],
    "mantequilla": ["aceite de oliva", "margarina vegetal"],
    "harina": ["harina de avena", "harina de almendras"],
    "azucar": ["miel", "stevia"],
    "arroz": ["quinoa", "cebada"],
    "queso": ["tofu prensado"],
}


def buscar_sustituciones(ingrediente, visitados=None, nivel=0):

    if visitados is None:
        visitados = set()

    if ingrediente in visitados:
        return

    visitados.add(ingrediente)

    alternativas = arbol_sustituciones.get(ingrediente)

    if not alternativas:
        if nivel > 0:
            print("  " * nivel + f"{ingrediente} no tiene mas alternativas.")
        return

    if nivel == 0:
        print(f"\nSustituciones para '{ingrediente}':")

    for alternativa in alternativas:
        print("  " * nivel + f"-> {alternativa}")
        buscar_sustituciones(alternativa, visitados, nivel + 1)


# ============================================================
# GESTOR DE RECETAS
# ============================================================

class GestorRecetas:

    def __init__(self):
        self.recetas = {}
        self.categorias = {}

    def agregar_receta(self, receta):
        self.recetas[receta.nombre] = receta

        if receta.categoria not in self.categorias:
            self.categorias[receta.categoria] = set()

        self.categorias[receta.categoria].add(receta.nombre)

    def eliminar_receta(self, nombre):
        receta = self.recetas.pop(nombre, None)

        if receta is None:
            return False

        categoria = receta.categoria
        self.categorias[categoria].discard(nombre)

        if not self.categorias[categoria]:
            del self.categorias[categoria]

        return True

    def buscar_por_nombre(self, nombre):
        return self.recetas.get(nombre)

    def listar_todas(self):
        if not self.recetas:
            print("No hay recetas registradas.")
            return

        print("\n" + "-" * 65)
        print(f"{'#':<4}{'Nombre':<30}{'Categoria':<20}{'Tiempo'}")
        print("-" * 65)

        for i, receta in enumerate(self.recetas.values(), start=1):
            print(
                f"{i:<4}"
                f"{receta.nombre:<30}"
                f"{receta.categoria:<20}"
                f"{receta.tiempo_minutos} min"
            )

    def listar_por_categoria(self):
        if not self.categorias:
            print("No hay categorias registradas.")
            return

        for categoria, nombres in self.categorias.items():
            print(f"\n[{categoria.upper()}]")

            for nombre in sorted(nombres):
                receta = self.recetas[nombre]

                print(
                    f"- {nombre} "
                    f"({receta.tiempo_minutos} min, "
                    f"{len(receta.ingredientes)} ingredientes)"
                )

    def modo_nevera(self, ingredientes_disponibles):
        disponibles = {
            ingrediente.strip().lower()
            for ingrediente in ingredientes_disponibles
        }

        completas = []
        parciales = []

        for receta in self.recetas.values():
            ingredientes = receta.ingredientes

            if not ingredientes:
                continue

            tengo = disponibles & ingredientes
            faltan = ingredientes - disponibles

            porcentaje = (len(tengo) / len(ingredientes)) * 100

            if not faltan:
                completas.append(receta.nombre)

            elif porcentaje >= 50:
                parciales.append(
                    (
                        receta.nombre,
                        round(porcentaje),
                        sorted(faltan)
                    )
                )

        print()

        if completas:
            print("Puedes preparar:")
            for receta in completas:
                print(f"- {receta}")

        if parciales:
            print("\nRecetas casi completas:")

            for nombre, porcentaje, faltan in parciales:
                print(f"- {nombre} ({porcentaje}%)")
                print(f"  Faltan: {', '.join(faltan)}")

        if not completas and not parciales:
            print("No hay coincidencias.")

    def estadisticas(self):
        total_ingredientes = set()
        tiempos = []

        for receta in self.recetas.values():
            total_ingredientes.update(receta.ingredientes)
            tiempos.append(receta.tiempo_minutos)

        print("\nEstadisticas")
        print("-" * 30)
        print(f"Recetas registradas: {len(self.recetas)}")
        print(f"Categorias: {len(self.categorias)}")
        print(f"Ingredientes unicos: {len(total_ingredientes)}")

        if tiempos:
            promedio = sum(tiempos) / len(tiempos)

            print(f"Tiempo promedio: {promedio:.1f} min")
            print(f"Receta mas rapida: {min(tiempos)} min")
            print(f"Receta mas lenta: {max(tiempos)} min")


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def pedir_opcion(opciones):
    while True:
        entrada = input("Opcion: ").strip()

        if entrada.isdigit():
            opcion = int(entrada)

            if opcion in opciones:
                return opcion

        print("Opcion invalida.")


def pedir_texto(mensaje, permitir_vacio=False):
    while True:
        valor = input(f"{mensaje}: ").strip()

        if valor or permitir_vacio:
            return valor

        print("El campo no puede estar vacio.")


def seleccionar_receta(gestor):
    nombres = list(gestor.recetas.keys())

    if not nombres:
        print("No hay recetas registradas.")
        return None

    print()

    for i, nombre in enumerate(nombres, start=1):
        print(f"{i}. {nombre}")

    print("0. Cancelar")

    while True:
        entrada = input("Seleccione una receta: ").strip()

        if entrada == "0":
            return None

        if entrada.isdigit():
            indice = int(entrada) - 1

            if 0 <= indice < len(nombres):
                return nombres[indice]

        print("Opcion invalida.")


# ============================================================
# MENUS
# ============================================================

def menu_ver_receta(gestor):
    nombre = seleccionar_receta(gestor)

    if nombre:
        gestor.recetas[nombre].mostrar()


def menu_agregar_receta(gestor):
    print("\nNueva receta")

    nombre = pedir_texto("Nombre")

    if nombre in gestor.recetas:
        print("La receta ya existe.")
        return

    categoria = pedir_texto("Categoria")

    while True:
        tiempo = input("Tiempo en minutos: ").strip()

        if tiempo.isdigit():
            tiempo = int(tiempo)
            break

        print("Ingrese un numero valido.")

    receta = Receta(nombre, categoria, tiempo)

    print("\nIngredientes (vacio para terminar):")

    while True:
        ingrediente = input("- ").strip()

        if not ingrediente:
            break

        receta.agregar_ingrediente(ingrediente)

    if not receta.ingredientes:
        print("Debe ingresar al menos un ingrediente.")
        return

    print("\nPasos (vacio para terminar):")

    while True:
        paso = input("- ").strip()

        if not paso:
            break

        receta.agregar_paso(paso)

    if receta.pasos.esta_vacia():
        print("Debe ingresar al menos un paso.")
        return

    gestor.agregar_receta(receta)

    print("Receta guardada correctamente.")


def menu_eliminar_receta(gestor):
    nombre = seleccionar_receta(gestor)

    if not nombre:
        return

    confirmacion = input(
        f"Eliminar '{nombre}'? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        gestor.eliminar_receta(nombre)
        print("Receta eliminada.")


def menu_sustituciones():
    print("\nIngredientes disponibles:")
    print(", ".join(sorted(arbol_sustituciones.keys())))

    ingrediente = input("\nIngrediente: ").strip().lower()

    if ingrediente:
        buscar_sustituciones(ingrediente)


# ============================================================
# DATOS INICIALES
# ============================================================

def cargar_datos_iniciales(gestor):
    recetas = [
        (
            "Torta de chocolate",
            "postres",
            60,
            [
                "harina",
                "azucar",
                "cacao",
                "huevo",
                "leche"
            ],
            [
                "Mezclar ingredientes",
                "Hornear durante 35 minutos"
            ]
        ),
        (
            "Pasta al pesto",
            "platos principales",
            25,
            [
                "pasta",
                "queso",
                "aceite de oliva"
            ],
            [
                "Hervir pasta",
                "Preparar pesto",
                "Mezclar"
            ]
        ),
    ]

    for nombre, categoria, tiempo, ingredientes, pasos in recetas:
        receta = Receta(nombre, categoria, tiempo)

        receta.agregar_varios_ingredientes(ingredientes)

        for paso in pasos:
            receta.agregar_paso(paso)

        gestor.agregar_receta(receta)


# ============================================================
# MENU PRINCIPAL
# ============================================================

def main():
    gestor = GestorRecetas()

    cargar_datos_iniciales(gestor)

    while True:
        print("\n" + "=" * 50)
        print("GESTOR DE RECETAS")
        print("=" * 50)

        print("1. Ver recetas")
        print("2. Ver detalle")
        print("3. Agregar receta")
        print("4. Eliminar receta")
        print("5. Buscar por categoria")
        print("6. Modo nevera")
        print("7. Sustituciones")
        print("8. Estadisticas")
        print("0. Salir")

        opcion = pedir_opcion(set(range(9)))

        if opcion == 0:
            print("Programa finalizado.")
            break

        elif opcion == 1:
            gestor.listar_todas()

        elif opcion == 2:
            menu_ver_receta(gestor)

        elif opcion == 3:
            menu_agregar_receta(gestor)

        elif opcion == 4:
            menu_eliminar_receta(gestor)

        elif opcion == 5:
            gestor.listar_por_categoria()

        elif opcion == 6:
            ingredientes = input(
                "Ingredientes separados por coma: "
            ).split(",")

            gestor.modo_nevera(ingredientes)

        elif opcion == 7:
            menu_sustituciones()

        elif opcion == 8:
            gestor.estadisticas()


if __name__ == "__main__":
    main()
