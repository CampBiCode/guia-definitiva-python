from .id import crear_id
from random import randint
import datetime as dt
from typing import List, Dict

def crear_enemigos() -> List[Dict]:
    while True:
        cantidad = int(input("¿Cuántos enemigos quieres crear?: ").strip())
        if type(cantidad) == int:
            break
        
        print("Acción inválida") 
        
    enemigos = []
    for x in range(cantidad):
        nuevo_enemigo = {}
        nuevo_enemigo["id"] = crear_id()
        nuevo_enemigo["especialidad"] = seleccionar_especialidad()
        nuevo_enemigo["creación"] = dt.date.today()
        enemigos.append(nuevo_enemigo)
    return enemigos

def seleccionar_especialidad() -> str:
    especialidades = ["boxeo", "judo", "karate", "taekwondo", "kickboxing"]
    indice = randint(0, len(especialidades) - 1)
    especilidad = especialidades[indice]
    return especilidad