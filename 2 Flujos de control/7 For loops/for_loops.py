# Sintáxis de los for loops
for x in range(10):
    print(x)



# For loops con rangos
contador = 0
for x in range(10):
    contador = contador + 1
    print(contador)
print(contador)



# For loops con strings
nombre_usuario = "santiago"
nuevo_nombre_usuario = ""
for x in nombre_usuario:
    if x == "a":
        nuevo_nombre_usuario = nuevo_nombre_usuario + x.upper()
    else:
        nuevo_nombre_usuario = nuevo_nombre_usuario + x
print(nuevo_nombre_usuario)