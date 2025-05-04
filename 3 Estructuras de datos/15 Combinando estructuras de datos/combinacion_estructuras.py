# Listas y conjuntos
## se puede usar para eliminar duplicados
lista_duplicada = [1, 2, 2, 3, 4, 4, 5]
conjunto_unico = set(lista_duplicada)
print(conjunto_unico)



# Diccionarios y listas
## almacenar listado de diccionarios
usuarios = [{"nombre":"andrew", "edad":24, "profesion":"ingeniero"},
            {"nombre":"thomas", "edad":22, "profesion":"diseñador"},
            {"nombre":"david", "edad":23, "profesion":"contador"}]

for x in usuarios:
    print(x["nombre"])

## almacenar listas de datos dentro de un diccionario
usuario = {"nombre":"santiago", "edad":45, "profesion":"ingeniero",
           "lenguajes":["python", "java", "javascript", "kotlin"]}



# Listas y tuplas: Almacenar listados de coordenadas
lista_puntos = [(1, 2), (3, 4), (5, 6)]

for punto in lista_puntos:
    x, y = punto
    print("Coordenadas:", x, y)



# Listas de listas: Representan matrices
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in matriz:
    for valor in fila:
        print(valor)
    print("")



# Diccionarios y conjuntos
diccionario_relaciones = {'amigos': {'Juan', 'María'}, 'colegas': {'Pedro', 'María'}}

print(diccionario_relaciones['amigos'] - diccionario_relaciones["colegas"])