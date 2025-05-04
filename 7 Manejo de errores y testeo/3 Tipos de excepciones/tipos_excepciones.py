# Tipos de excepciones
## TypeError: ocurre cuando se realiza una operación en un objeto de tipo inapropiado
num = 10
texto = "Hola"
resultado = num + texto

## ValueError: se produce cuando una función recibe un argumento de tipo correcto pero con un valor que no puede procesar
num = int("diez")

## ZeroDivisionError: ocurre cuando se intenta dividir un número entre cero
resultado = 10 / 0

## IndexError: se produce cuando se intenta acceder a un índice que está fuera del rango de una lista
lista = [1, 2, 3]
print(lista[3])

## KeyError: se genera cuando se intenta acceder a una clave que no está presente en un diccionario
diccionario = {"a":1, "b":2}
print(diccionario["c"])

## FileNotFoundError: se produce cuando se intenta abrir un archivo que no existe
archivo = open("archivo_que_no_existe.txt")

## NameError: se produce cuando se intenta acceder a una variable que no está definida en el ámbito local
print(variable_no_definida)

## AttributeError: ocurre cuando se intenta acceder a un atributo que no existe en un objeto
class MiClase:
    pass

objeto = MiClase()
print(object.atributo_que_no_existe)

## ImportError: se genera cuando hay un error al intentar importar un módulo
import modulo_que_no_existe

## MemoryError: se produce cuando no hay suficiente memoria disponible para la ejecución del programa
lista_grande = [0] * 100000000000000000

## KeyboardInterrupt: se genera cuando el usuario interrumpte la ejecución del programa (por ejemplo, presionando Ctrl + C en una terminal)
while True:
    pass # bucle de ejecución indefinida



# Crear nuevas excepciones
class PlatformError(Exception):
    pass

def cargar_a_plataforma(mensaje:str, plataforma:str) -> None:
    plataformas = ["azure", "gcp", "aws"]
    if not plataforma in plataformas:
        raise PlatformError(f"La plataforma {plataforma} no esta disponible. (Plataformas={plataformas})")
    print("Mensaje cargado")

cargar_a_plataforma("Hola mundo", "azur")