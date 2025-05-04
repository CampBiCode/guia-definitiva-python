# Argumentos en decoradores
import functools

def repetir(n):
    def decorador_repetir(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorador_repetir

@repetir(n = 5)
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Thom")