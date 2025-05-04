# Operadores ternarios
edad = 22
mensaje = "Mayor de edad" if edad >= 18 else "Menor de 50 años"
print(mensaje)



# Condicionales anidados
x = 2
y = 10

if x > 0: # True
    if y > 0: # True
        print("Ambos números son positivos")
    else:
        print("Solo ún número es positivo")
else:
    print("Ningún número es positivo")