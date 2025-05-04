# Sintáxis básico
"""
if alguna_condicion es verdadera:
    haz algo
elif otra condición es verdadera:
    haz algo
else:
    haz algo
"""

nombre_usuario = "santiago"

if nombre_usuario == "santiago":
    print("Bienvenido Santiago")
elif nombre_usuario == "Esteban":
    print("Bienvenido Esteban")
else:
    print("No te reconozco")


edad_usuario = int(input("¿Cuál es tu edad?"))
puede_pasar = "No"

if edad_usuario == 17:
    print("No puedes pasar")
    puede_pasar = "No"
elif edad_usuario == 18:
    print("Puedes pasar")
    puede_pasar = "Sí"
else:
    print("No reconozco tu edad")

