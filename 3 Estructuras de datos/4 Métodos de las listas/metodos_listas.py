"""Las listas en Python son objetos mutables, lo que significa que puedes modificar su contenido sin necesidad de crear una nueva lista. 
Cuando aplicas un método a una lista, el método modifica directamente la lista existente, 
y no es necesario reasignar la variable para reflejar esos cambios."""


# Agregar datos a una lista
## append: agregar un dato al final de la lista
datos = [1, 2, 3, 4]
datos.append(10)

## extend: agregar una lista de datos al final de la lista
datos = [1, 2, 3, 4]
datos.extend([4, 5, 6, 7, 8])

datos = [1, 2, 3, 4]
datos_2 = [4, 5, 6, 7, 8]
datos.extend(datos_2)

## insert: agregar un dato en una posición determinada
datos = [1, 2, 3, 4]
datos.insert(2, 10)

datos = [1, 2, 3, 4]
datos.insert(len(datos), "Adios")

## +: combinar dos listas
datos1 = [1, 2, 3, 4]
datos2 = [5, 6, 7, 8]
datos = datos1 + datos2



# Eliminar datos de una lista
## clear: remover todos los datos de una lista
datos = [1, 2, 3, 4]
datos.clear()
print(datos) 

## pop: remueve el dato en la posición específicada, sino se específica remueve el último dato
datos = [1, 2, 3, 4]
datos.pop(2)
dato_eliminado = datos.pop()

## remove: remueve la primera aparación del dato específicado
datos = ["thomas", "andres", "felipe", "andres"]
datos.remove("andres")



# Otros métodos
## index: regresa la posición de un dato
numeros = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(numeros.index(5))
print(numeros.index(5, 0)) # segunda posición donde aparece el 5
print(numeros.index(5, 1)) # tercera posición donde aparace el 5
print(numeros.index(8, 6, 8)) # busca el 8 entre la posición 6 y 8

## count: regresa la cantidad de veces que aparece un dato en la lista
numeros = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(numeros.count(5)) # 3

## reverse: invierte el orden la lista
numeros = [5, 5, 6, 7, 5, 8, 8, 9, 10]
numeros.reverse() # in-place

## sort: ordena los datos de una lista in-place
numeros = [6, 4, 1, 2, 5]
numeros.sort(reverse = True)

## join: concatena los elementos de la lista por un separador específico
datos = ["programar", "es", "divertido"]
print(", ".join(datos))

## copy: crea una copia de la lista
lista_original = [1, 2, 3, 4]
lista_modificada = lista_original.copy()
lista_modificada.append(4)

print(lista_original)
print(lista_modificada)

## convertir string en una lista
mensaje = ["hola es un gusto conocerte"]
mensaje = mensaje.split()
print(mensaje) # ["hola", "es", "un", "gusto", "conocerte"]
