# *args: permite recibir un número variable de argumentos y almacenarlos en una tupla
## ejemplo 1: función sin args (no escalable) y con args (escalable)
def sumar_numeros(n1, n2, n3):
    total = n1 + n2 + n3
    return total

print(sumar_numeros(1, 2, 3))

### puede que no sepamos la cantidad de valores a pasar hasta que llamemos la función
def sumar_numeros(*args):
    total = 0
    for x in args:
        total += x
    return total

print(sumar_numeros(1, 2, 3, 4, 5, 6, 7))

## ejemplo 2: recibir una cantidad variable de datos y convertirlos en una lista
def transformar_datos(*args):
    datos = [x[0].lower() + x[1:-1].upper() + x[-1].lower() for x in args]
    return datos

nombres = transformar_datos("andrew", "yesica", "kath", "thom")
print(nombres)



# **kwargs: permite recibir un número variable de argumentos y almacenarlos en un diccionario
## ejemplo 1: entendiendo que estos argumentos se convierten en diccionarios
def imprimir_info(**kwargs):
    llaves = kwargs.keys()
    valores = kwargs.values()
    print(llaves)
    print(valores)

imprimir_info(nombre = "santiago", edad=30, ciudad="miami")


## ejemplo 2: interactuando con las llaves del diccionario
def dar_color(**kwargs):
    for persona, color in kwargs.items():
        print(f"El color favorito de {persona} es: {color}")

dar_color(santiago = "verde", thomas = "rojo", laura = "amarillo")



# Orden de parámetros
## 1. parámetros estándar
## 2. *args
## 3. **kwargs

def concatenar_mensaje(mensaje:str, *args, **kwargs):
    mensajes = [mensaje + x for x in args]
    kwargs["datos"] = mensajes
    return kwargs

dato = concatenar_mensaje("Bienvenido", "t1", "t2", "t3" , "t4", nombre = "usuario1", datos = None)
print(dato)



# Desempaquetado de argumentos
## desempaquetado de iterables con operador *
lista1 = [1, 2, 3]
print(lista1)
print(*lista1) # es como si print estuviera recibiendo cada valor como un argumento

### desempaquetado con argumentos requeridos
def suma(n1, n2, n3):
    return n1 + n2 + n3

valores = [1, 2, 3]
print(suma(*valores))

### desempaquetado con argumentos variables
def suma(*args):
    total = 0
    for x in args:
        total += x
    return total

valores = [1, 2, 3, 4, 5, 6, 7]
print(suma(*valores))


## desempaquetado de diccionarios con operador **
def imprimir_info(**kwargs):
    nombre = kwargs["nombre"]
    edad = kwargs["edad"]
    ciudad = kwargs["ciudad"]
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

datos = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

imprimir_info(**datos)