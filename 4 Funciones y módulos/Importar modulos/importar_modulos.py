# ¿Qué es un módulo?
## pequeños bloques de código reutilizables



# Tipos de módulos
## pre instalados
## de terceros
## definidios en nuestras aplicaciones



# ¿Cómo importar un modulo?
import random

## acceder a las funcionalidades del módulo
entero_aleatorio = random.randint(1, 20)
aleatorio = random.random()

print(entero_aleatorio)
print(aleatorio)

## ubicación en la que está almecenado el módulo
print(random.__file__)

## Importar con un alias
import datetime as dt
print(dt.date.today())

## importar funcionalidades de un módulo
### opción recomendada para mejorar legibilidad
from random import randint

print(randint(1, 10))