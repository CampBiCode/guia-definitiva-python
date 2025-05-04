from utils.acudiente import Acudiente
from utils.id import generate_id

class Estudiante:
    def __init__(self, nombre:str, edad:int, acudiente:Acudiente):
        self.id = generate_id()
        self.nombre = nombre
        self.notas = []
        self.edad = edad
        self.acudiente = acudiente

    def __repr__(self) -> None:
        return f"Mi nombre es {self.nombre}, mi edad es {self.edad} y mi acuidente es {self.acudiente.nombre}"
    
    def agregar_nota(self, nota:float) -> None:
        self.notas.append(nota)

    def generar_promedio_notas(self) -> None:
        promedio_notas = sum(self.notas) / len(self.notas)
        print(promedio_notas)