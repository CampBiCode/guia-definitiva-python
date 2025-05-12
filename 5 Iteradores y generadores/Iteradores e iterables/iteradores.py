# Iterables
## ejemplos de iterables
nombre = "Thomas"
datos = ["Thomas", "Andrew", "Kim"]
datos_diccionario = {"nombre":"thomas", "edad":34, "color":"azul"}

for x in nombre:
    print(x)

datos = [x[0].upper() + x[0:] for x in datos]
print(datos)

## una manera rápida de saber que objetos de Python son iterables es porque tienen el atributo __iter__
print(dir(datos_diccionario))



# Iteradores
data = iter([1, 2, 3, 4])
print(data)
print(type(data))

## la función next permite retornar el siguiente elemento de un iterador
print(next(data))
print(next(data))
print(next(data))
print(next(data))

## la función next tiene un segundo parámetro, el valor a retornar en el caso de recibir un StopIteration error
print(next(data, ""))

## métodos de los iteradores
from itertools import accumulate

a = [1, 2, 3, 4]

print(list(accumulate(a)))

with open("texto.txt") as f:
    print(next(f))
    print(next(f))