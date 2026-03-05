"""EJERCICIO: estamos trabajando en una clinica y necesitamos gestionar las prioridades de los pacientes, 
anotamos el nombre del paciente, su nivel de prioridad (1 para alta prioridad, 2 para prioridad media, 3 para baja prioridad) y orden de llegada. 
Queremos asegurarnos de que los pacientes con mayor prioridad sean atendidos primero. Para esto, podemos utilizar un heap para almacenar los pacientes, usar un menu basico y sus prioridades. 
Aquí hay un ejemplo de cómo podríamos implementar esto en Python:
"""
import heapq
class Paciente:
    def __init__(self, nombre, prioridad, orden_llegada):
        self.nombre = nombre
        self.prioridad = prioridad
        self.orden_llegada = orden_llegada

    def __lt__(self, other): #este metodo lo utilizo para comparar dos objetos de la clase Paciente y determinar cuál tiene mayor prioridad.
        if self.prioridad == other.prioridad:
            return self.orden_llegada < other.orden_llegada
        return self.prioridad < other.prioridad
class Clinica:
    def __init__(self):
        self.pacientes = []
        self.orden_llegada = 0

    def agregar_paciente(self, nombre, prioridad):
        paciente = (prioridad, self.orden_llegada, nombre)
        heapq.heappush(self.pacientes, paciente)
        self.orden_llegada += 1
        print(f"Paciente '{nombre}' agregado con prioridad {prioridad}.\n")

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes en la clínica.\n")
            return
        print("⁛"*35)
        print("Pacientes en la clínica")
        print("⁛"*35)
        for paciente in self.pacientes:
            print(f"Nombre: {paciente[2]}, Prioridad: {paciente[0]}, Orden de llegada: {paciente[1]} \n")
    

    def atender_paciente(self):
        if not self.pacientes:
            print("No hay pacientes para atender.")
            return
        paciente_atendido = heapq.heappop(self.pacientes)
        print(f"Atendiendo al paciente: '{paciente_atendido[2]}' con una prioridad de: {paciente_atendido[0]} ' su orden de llegada: {paciente_atendido[1]}.\n")
# Ejemplo de uso
clinica = Clinica()
clinica.agregar_paciente("Sara", 2)
clinica.agregar_paciente("Pablo", 1)
clinica.agregar_paciente("Daniel", 3)
clinica.agregar_paciente("Lisbet", 1)
clinica.mostrar_pacientes()

clinica.atender_paciente()  
clinica.atender_paciente()  
clinica.atender_paciente()  
clinica.atender_paciente()  
clinica.orden_llegada = 0 

print(clinica.pacientes)
