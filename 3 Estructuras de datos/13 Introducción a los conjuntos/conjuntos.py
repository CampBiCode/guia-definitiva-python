# Sintáxis
datos = {1, 2, 3, 4, 5, 6}
print(type(datos))
print(datos)

## acceder a elementos
datos = {1, 2, 3, 4, 5, 6}
print(datos[0]) # No es posible

## eliminar duplicados
ciudades = ["Los angeles", "Los angeles", "Santiago", "Miami", "Miami"]
ciudades_unicas = set(ciudades)
print(ciudades_unicas)

## función set
datos = set(range(10))
print(datos)

## comprobación de pertenencia
colores = {"azul", "rojo", "verde", "amarillo"}
print("azul" in colores)



# Iterar sobre conjuntos
## for loop en conjuntos
datos = {1, 2, 3, 4, 5, 6, 7, 8, 9}
datos_duplicados = []
for x in datos:
    print(x)
    datos_duplicados.append(x)
    datos_duplicados.append(x)

## while loop no es posible



# Operaciones entre conjuntos
## union: crea un nuevo conjunto que contiene todos los elementos de ambos conjuntos, sin duplicados
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
union = conjunto_a | conjunto_b
print(union)

## intersección: crea un nuevo conjunto que contiene solo los elementos que están presentes en ambos conjuntos originales
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
interseccion = conjunto_a & conjunto_b
print(interseccion)

## diferencia: crea un nuevo conjunto que contiene los elementos presentes en el primer conjunto pero no en el segundo
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
diferencia = conjunto_a - conjunto_b
print(diferencia)

## diferencia simetrica: crea un nuevo conjunto que contiene los elementos que están en uno de los conjuntos, pero no en ambos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
diferencia_simetrica = conjunto_a ^ conjunto_b
print(diferencia_simetrica)
