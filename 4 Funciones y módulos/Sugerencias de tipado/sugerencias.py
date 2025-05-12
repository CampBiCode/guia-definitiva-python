# Sintáxis
## cuando se llama a la función esta nos indica los tipos de datos esperados y que serán retornados con su ejecución
def suma(a: int, b: int) -> int:
    resultado = a + b
    return resultado

print(suma(2, 2))

## cuando la función no retorna un dato sino que solo imprime se usa None
def dar_saludo(mensaje: str, n: int) -> None:
    for x in range(n):
        print(mensaje)
        
## tipados básicos
def function(a: int, b: str, c: float, d: bool) -> None:
    pass



# Sugerencias de tipado para datos opcionales
from typing import Union

def add(x: Union[int, float], y:Union[int, float]) -> Union[int, float]:
    return x + y
    
## desde python 3.10
def add(x: int | float, y: int | float) -> int | float:
    return x + y



# Sugerencia de tipado para listas, diccionarios y conjuntos
## listas
from typing import List
def process_list(data: List[int]) -> None:
    pass

## diccionarios
from typing import Dict
def process_dict(data: Dict[str, int]) -> None:
    pass

## conjuntos
from typing import Set

def process_set(data: Set[str]) -> None:
    pass
    