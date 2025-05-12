# Paradigma de programación imperativa
## utiliza variables para almacenar y manipular datos
## se basa en estructuras de control como bucles (for, while) y condicionales
## se enfoca en la reasignación de variables a lo largo del tiempo

## ejemplo: Receta de cocina. Se le indica al programa cada paso que debe dar para hacer la receta

suma = 0

for x in range(1, 11): # bucle for para iterar los números del 1 al 10
    if x % 2 == 0: # se verifica si cada número es par
        suma += x # se suma el total

print("La suma de los números pares del 1 al 10 es:", suma) # se imprime el total



# Paradigma de programación funcional
## todo se basa en el uso de funciones y expresiones
## ejemplo: Maquina expendedora. Insertas una moneda (entrada), presionas un botón y obtienes una bebida (resultado). La máquina no cambia nada en sí misma, solo produce la bebida basada en la entrada

## crear una lista de números del 1 al 10
numeros = list(range(1, 11))

## seleccionar los números pares usando list comprehensions
numeros_pares = [num for num in numeros if num % 2 == 0]

## sumar los números pares usando la función built-in sum
suma = sum(numeros_pares)

print("La suma de los números pares del 1 al 10 es:", suma)