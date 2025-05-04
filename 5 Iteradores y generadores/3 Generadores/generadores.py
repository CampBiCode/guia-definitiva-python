# Expresiones de generadores
## hay dos formas de definir generadores: usando generator comprehension o definiendo funciones
## generator comprehension
data = (2 * num for num in range(10))
print(data)
print(type(data))
print(list(data))

## Funciones de generador
### usa yield en lugar de return y retorna una secuencia de valores en lugar de retornar uno solo
### genera cada valor con la palabra clave yield. El estado de la función es recordado
def secuencia_num(n):
    i = 0
    while i < n:
        yield i
        i += 1

secuencia = secuencia_num(20)
print(type(secuencia))
print(next(secuencia))

### se continuará ejecutando hasta que se detenga el programa
def secuencia_infinita():
    num = 0
    while True:
        yield num
        num += 1



# Rendimiento de generadores
import random
import time

nombres = ["santiago", "andrew", "thomas", "elizabeth"]

def crear_usuario(numero_usuarios):
    datos = []
    for x in range(numero_usuarios):
        usuario = {
            "id": x,
            "nombre": random.choice(nombres),
            "edad": random.randint(10, 40)
        }
        datos.append(usuario)    
    return datos

def crear_usuario_generador(numero_personas):
    for x in range(numero_personas):
        usuario = {
            "id": x,
            "nombre": random.choice(nombres),
            "edad": random.randint(10, 40)
        }
        yield usuario

t1 = time.time()
resultado = crear_usuario(10000000)
t2 = time.time()
print(f"Tiempo total sin generador: {t2 - t1}")

t1 = time.time()
resultado = crear_usuario_generador(10000000)
t2 = time.time()
print(f"Tiempo total con generador: {t2 - t1}")


