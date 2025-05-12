while True:
    rondas = int(input("¿Cuántas rondas vas a jugar?"))
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0
    for x in range(rondas):
        print(f"Ronda {x+1}")
        jugador1 = input("Jugador 1 ¿Qué eliges?(piedra/papel/tijera)").lower()
        if (jugador1 != "tijera" and jugador1 != "papel" and jugador1 != "piedra"):
            print("Por favor, elige una opción válida.")
            continue
        elif jugador1 == "salir":
            break

        jugador2 = input("Jugador 2 ¿Qué eliges?(piedra/papel/tijera)").lower()
        if (jugador2 != "tijera" and jugador2 != "papel" and jugador2 != "piedra"):
            print("Por favor, elige una opción válida.")
            continue
        elif jugador2 == "salir":
            break

        print(f"Jugador 1: {jugador1}")
        print(f"Jugador 2: {jugador2}")

        if jugador1 == jugador2:
            print("¡Empate!")
            puntaje_jugador1 += 1
            puntaje_jugador2 += 1
        elif (jugador1 == "piedra" and jugador2 == "tijera") or \
            (jugador1 == "papel" and jugador2 == "piedra") or \
            (jugador1 == "tijera") and jugador2 == "papel":
            print("¡Gana el jugador 1!")
            puntaje_jugador1 += 1
        else:
            print("¡Gana el jugador 2!")
            puntaje_jugador2 +=1
        print("--------------------------")

    print("Juego terminado")
    print(f"Jugador 1: {puntaje_jugador1}")
    print(f"Jugador 2: {puntaje_jugador2}")
    if puntaje_jugador1 == puntaje_jugador2:
        print("¡Es un empate!")
    elif puntaje_jugador1 > puntaje_jugador2:
        print("¡Gana el jugador 1!")
    else:
        print("¡Gana el jugador 2!")

    opcion = input("¿Quieres jugar de nuevo?(si/no)").lower()
    if opcion == "no":
        break


