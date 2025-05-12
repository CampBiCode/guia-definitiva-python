from utils.id import generate_id
from enum import Enum

class Idioma(Enum):
    INGLES = "Inglés"
    ESPAÑOL = "Español"
    ITALINAO = "Italiano"
    FRANCES = "Frances"

class Profesor:
    def __init__(self, nombre:str, especialidad:str):
        self.id = generate_id()
        self.nombre = nombre
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad:str) -> None:
        self.__especialidad = especialidad

    def __repr__(self) -> None:
        return f"Mi nombre es {self.nombre} y mi especilidad en docencia es {self.especialidad}."
    
class ProfesorIntercambio(Profesor):
    def __init__(self, nombre:str, especilidad:str, pais_origen:str, idiomas:list[Idioma]):
        super().__init__(nombre, especilidad)
        self.pais_origen = pais_origen
        self.idiomas = idiomas