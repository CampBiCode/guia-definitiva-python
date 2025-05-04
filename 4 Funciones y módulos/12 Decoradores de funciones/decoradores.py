# ¿Qué es un decorador?
## sintáxis básico de los decoradores

def inicio_fin(func):
    def wrapper():
        print("Algo ocurre antes de que se ejecute la función")
        func()
        print("Algo ocurre después de que se ejecute la función")
    return wrapper

def imprimir_nombre():
    print("Thomas")

print_name = inicio_fin(imprimir_nombre)
print_name()

## propiedad de las funciones para almacenarlas en una variable y luego llamarlas (objetos de primera clase)
nombre = imprimir_nombre
nombre()

## para evitar crear una variable donde llamamos las dos funciones podemos usar un decorador antes de la función
def inicio_fin(func):
    def wrapper():
        print("Algo ocurre antes de que se ejecute la función")
        func()
        print("Algo ocurre después de que se ejecute la función")
    return wrapper

@inicio_fin
def imprimir_nombre():
    print("Thomas")

imprimir_nombre()



# Plantilla para crear decoradores
import functools
def inicio_fin(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Algo ocurre antes de que se ejecute la función")
        resultado = func(*args, **kwargs)
        return resultado # si queremos retornar el resultado de la función debemos específicarlo
    
    return wrapper

@inicio_fin
def adicionar5(x):
    return x + 5

print(adicionar5(10))

## Plantilla:
import functools

def decorator(func):

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # hacer algo antes
        valor = func(*args, **kwargs)
        ## hacer algo después
        return valor
    return wrapper_decorator

## ejemplo: contar el tiempo de ejecución de una función
import functools
import time
import random

def timer(func):

    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"La función se ejecuto en {run_time} segundos")
        return value
    return wrapper_time

@timer
def repetir_tarea(n = 100):
    intentos = []
    for x in range(n):
        aletorio = random.random()
        if aletorio > 0.5:
            intentos.append(1)
        else:
            intentos.append(0)

    resultado = sum(intentos) / len(intentos)
    print(f"La probabilidad promedio de que saques cara es: {resultado}")
    return intentos