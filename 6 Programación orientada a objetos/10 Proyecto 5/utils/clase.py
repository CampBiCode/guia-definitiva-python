from utils.profesor import Profesor
from utils.estudiante import Estudiante
from utils.id import generate_id

class Clase:
    def __init__(self, nombre:str, capacidad:int, edad_minima:int, profesor:Profesor):
        self.id = generate_id()
        self.nombre = nombre
        self.capacidad = capacidad
        self.edad_minima = edad_minima
        self.estudiantes = []
        self.profesor = profesor

    def asociar_estudiante(self, estudiante:Estudiante) -> None:
        if estudiante.edad > self.edad_minima:
            self.estudiantes.append(estudiante)
            print(f"Estudiante: {estudiante.nombre} asociado.")
        else:
            print("El estudiante no cumple con la edad mínima para ser asociado a esta clase.")

    def mostrar_estudiantes(self) -> None:
        print(f"Lo estudiantes que pertenecen a la clase {self.nombre} son {[x.nombre for x in self.estudiantes]}.")

    def generar_promedio_notas(self) -> None:
        promedio_por_estudiante = []
        for x in self.estudiantes:
            promedio = sum(x.notas) / len(x.notas)
            promedio_por_estudiante.append(promedio)
        
        promedio_general = sum(promedio_por_estudiante) / len(promedio_por_estudiante)

        print(promedio_general)