import datetime as dt
from typing import Dict
from .id import crear_id

def crear_usuario(nombre: str, especialidad: str) -> Dict[str, str | int | dt.date]:
    usuario = {}
    usuario["id"] = crear_id()
    usuario["nombre"] = nombre
    usuario["especialidad"] = especialidad
    usuario["victorias"] = 0
    usuario["derrotas"] = 0
    usuario["creación"] = dt.date.today()
    return usuario


def introducir_nombre() -> str:
    while True:
        nombre = input("Nombre del usuario: ").lower().strip()
        if type(nombre) == str:
            return nombre

        print("Acción inválida")    


def introducir_especialidad() -> str:
    especialidades = ["boxeo", "judo", "karate", "taekwondo", "kickboxing"]
    while True:
        especialidad = input(f"Selecciona una especialidad ({", ".join(especialidades)}): ").lower().strip()
        if type(especialidad) == str and especialidad in [x.lower() for x in especialidades]:
            return especialidad

        print("Acción inválida")    


def editar_usuario(usuario: Dict[str, str | int | dt.date]) -> Dict[str, str | int | dt.date]:
    nombre = introducir_nombre()
    especialidad = introducir_especialidad()

    if nombre:
        usuario["nombre"] = nombre
    
    if especialidad:
        usuario["especialidad"] = especialidad

    return usuario