"""
ENUNCIADO:

una empresa necesita un sistema de control de acceso basado en roles.
cada rol tiene un conjunto de permisos. el sistema debe:

1. Verificar si un usuario puede realizar una accion
2. Encontrar permisos comunes entre roles
3. encontrar permisos excluidos de cada rol
4.verificar si un rol es "superior" a otro (tiene todos sus permisos)
5. Crear un nuevo rol combinando permisos de otros

Implementar usando operaciones de conjuntos
"""
roles = {
    "admin": {
        "leer", "escribir", "eliminar", "crear_usuarios",
        "ver_logs", "configuar", "backup", "restaurar"
    },
    "editor": {"leer", "escribir", "subir_archivos"},
    "viewer": {"leer"},
    "moderador": {"leer", "escribir", "eliminar", "ver_logs"},
    "auditor": {"leer", "ver_logs", "exportar_reportes"}
}
usuarios = {
    "Sara": "admin",
    "Lisbeth": "editor",
    "Daniel": "moderador",
    "Toro": "viewer",
    "Antonio": "auditor"
}

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Roles:
    def __init__(self, elementos = None):
        self.cabeza = None
        self.tamaño = 0 

        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    #1. Verificar si un usuario puede realizar una acción. 
    def verificar_accion(usuario, accion):
        rol = Roles.roles.get(Roles.usuarios.get(usuario))
        if rol and accion in rol:
            return True
        return False
    
  
    
    #2. Verificar si hay permisos comunes entre ellos

    def permisos_comunes(rol1, rol2):
        return Roles.roles.get(rol1, set()) & Roles.roles.get(rol2, set()) #Intersección de los permisos de ambos roles
    
    #3. Encontrar permisos exclusivos de un rol
    def permisos_exclusivos(rol):
        return Roles.roles.get(rol, set()) - set().union(*Roles.roles.values()) #Diferencia de los permisos del rol con la unión de los permisos de todos los roles
    
    #Tarea: Validar si un conjunto es subconjunto de otro
    def es_subconjunto(conjunto1, conjunto2):
        return conjunto1.issubset(conjunto2) #Verificar si conjunto1 es subconjunto de conjunto2 utilizando el método issubset de los conjuntos de Python

    #tarea: implementar con listas y listas ligadas el caso 4 y 5 