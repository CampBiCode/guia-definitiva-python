# Acceder a datos
## get: devuelve el valor asociado a una llave, si el valor no existe regresa None o un valor por defecto específicado
datos = {"a":1, "b":2, "c":3}
datos.get("a", "s")



# Agregar datos
## copy: crea una copia de otro diccionario
diccionario = {"a":1, "b":2, "c":3}
diccionario_modificado = diccionario.copy()
diccionario_modificado["d":4]
print(diccionario_modificado)
print(diccionario)

## fromkeys: crea un diccionario con un listado de claves proporcionadas y un valor opcional para todas las claves
datos = {}.fromkeys("a", "b")
print(datos)

datos = {}.fromkeys("a", [1, 2, 3, 4, 5, 6])
print(datos)

usuarios = {}.fromkeys(["nombre", "edad", "color", "pais"], "desconocido")
print(datos)

## update: actualiza las llaves y valores de un diccionario deste otro diccionario
datos = {"a":1, "b":2, "c":3}
datos2 = {"d":4, "e":5, "f":6}
datos.update(datos2)



# Eliminar datos
## clear: elimina todas las llaves y valores de un diccionario
datos = {"a":1, "b":2, "c":3}
datos = datos.clear()

## pop: toma un llave y remueve el par llave-valor del diccionario. Regresa el valor de la llave removida
datos = {"a":1, "b":2, "c":3}
eliminado = datos.pop("b")
print(eliminado)

## popitem: remueve un par llave-valor aleatorio.
datos = {"a":1, "b":2, "c":3}
datos.popitem()
print(datos)
