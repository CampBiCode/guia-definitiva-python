from typing import Dict, List
import datetime as dt
import random

def crear_batalla(enemigos: List[Dict]) -> int:
    aleatorio = random.random()
    indice = random.randint(0, len(enemigos) - 1)
    enemigo = enemigos[indice]
    juego_enemigo = random.randint(1, 10)

    while True:
        juego_usuario = int(input("Selecciona un número entre 1 y 10: ").strip())
        if type(juego_enemigo) == int:
            break

    print(f"Enemigo: {enemigo}")
    print(f"Jugador 1: {juego_usuario}")
    print(f"Jugador 2: {juego_enemigo}")

    if aleatorio > 0.5:
        print("Modalidad mayor puntaje")

        if juego_usuario > juego_enemigo:
            print("Gana el jugador 1")
            return 1
        elif juego_usuario < juego_enemigo:
            print("Gana el jugador 2")
            return 0
        else:
            print("Empate")

    if aleatorio < 0.5:
        print("Modalidad menor puntaje")

        if juego_usuario < juego_enemigo:
            print("Gana el jugador 1")
            return 1
        elif juego_usuario > juego_enemigo:
            print("Gana el jugador 2")
            return 0
        else:
            print("Empate")