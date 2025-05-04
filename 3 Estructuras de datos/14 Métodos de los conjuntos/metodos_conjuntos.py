# Agregar datos a un conjunto
## add: agrega un dato al conjunto. Si el dato ya estaba, el conjunto no cambia
datos = {1, 2, 3}
datos.add(4)
datos.add(3)
print(datos)

## update: agrega los datos de un conjunto a otro
conjunto_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_b = {1, 2, 3, 10, 11, 12}
conjunto_a.update(conjunto_b)
print(conjunto_a)

## copy: crea una copia de un cojunto
datos_original = {1, 2, 3}
datos = datos_original.copy()
datos.add(4)
print(datos_original)
print(datos)



# Remover datos de un conjunto
## remove: remueve un dato del conjunto, si no lo encuentra regrasa un KeyError
datos = {1, 2, 3, 4, 5, 6}
datos.remove(3)

## discard: remueve un dato del conjunto, si no lo encuentra no regresa un KeyError
datos = {1, 2, 3, 4, 5, 6}
datos.discard(8)

## pop: elimina un dato aleatorio del conjunto, siempre y cuando este no este vacio
datos = {1, 2, 3} 
datos.pop()
print(datos)

## clear: remueve todo los datos de un conjunto
datos = {1, 2, 3}
datos.clear()



# Operaciones entre conjuntos
## union: devuelve un conjunto que es la unión de dos o más conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
union = conjunto_a.union(conjunto_b)
print(union)

## intersection: devuelve un conjunto que es la intersección de dos o más conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
interseccion = conjunto_a.intersection(conjunto_b)
print(interseccion)

## difference: devuelve un cojunto que es la diferencia entre dos conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
diferencia = conjunto_a.difference(conjunto_b)
print(diferencia)

## symmetric difference: devuelve un conjunto que es la diferencia simétrica entre dos conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferencia_simetrica)
