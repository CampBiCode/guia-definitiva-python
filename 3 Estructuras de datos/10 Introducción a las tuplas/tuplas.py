# Sintáxis
## declaración de una tupla
datos = (1, 2, 3, 4, 5, 6)
print(type(datos))

datos = tuple((1, 2, 3, 4, 5))
print(datos)

## convertir de una lista a una tupla
datos = ["andrew", "alan", "monica"]
datos = tuple(datos)
print(datos)

## acceder a elementos
datos = (1, 2, 3, 4, 5)
datos[2]

## inmutabilidad
datos[2] = 10

## tuplas como llaves de diccionarios
ubicaciones = {
	(35.6895, 39.6917): "Tokyo Office",
	(40.7128, 740060): "New York Office",
	(37.7749, 122.4194): "San Francisco Office"
}

## tuplas anidadas
numeros = (1, 2, 3, (4, 5), 6, 7)



# Iterar sobre tuplas
## for loop en tuplas
datos = (35.6895, 39.6917, 35.86895, 39.6913)
datos_enteros = []
for x in datos:
    print(x)
    numero = int(x)
    datos_enteros.append(numero)

## while loop en tuplas
datos = (35.6895, 39.6917, 35.86895, 39.6913)
datos_nuevo = []
tipo_dato = input("¿A qué tipo de dato te gustaría convertir los datos?(str/int)")
contador = 0

while contador < len(datos):
    if tipo_dato == "int":
        numero = int(datos[contador])
        datos_nuevo.append(numero)
    elif tipo_dato == "str":
        string = str(datos[contador])
        datos_nuevo.append(string)
    contador += 1

print(datos_nuevo)



# Desempaquetar tuplas
usuario = (23, "andrew", "44")

id_usuario, nombre, edad = usuario

print(id_usuario)
print(nombre)
print(edad)

## equivale a
usuario = (23, "andrew", "44")

id_usuario = usuario[0]
nombre = usuario[1]
edad = usuario[2]


