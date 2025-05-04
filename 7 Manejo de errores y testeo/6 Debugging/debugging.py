# Detener el flujo de ejecución
## se hace un llamado a la función breakpoint para detener el flujo de ejecución hasta este punto
breakpoint() # muestra en que linea hemos pausado la ejecución
print(f"path = {__file__}") # con el comando p 'nombre_variable' podemos ver su contenido
                            # con el comando q cerramos el debugger

import random
from typing import Dict
import uuid

def generar_usuario_aleatorios(cantidad:int) -> Dict[int,str]:
    nombres = ["thom", "cristina", "maria", "charlie"]
    usuarios = {}
    for x in range(cantidad):
        usuario = nombres[random.randint(0, len(nombres) - 1)]
        usuarios[uuid.uuid4()] = usuario
    breakpoint() # el comando 'll' permite mostrar el origen de la función
                 # cuando pdb está activo podemos pasar cualquier código de Python válido
                 # el comando 'pp' muestra el contenido de una variable con un mejor formato
                 
    return usuarios


u = generar_usuario_aleatorios(5)
print(u)



# Navegar el flujo de ejecución
## usamos el comando 'n' para ejecutar la siguiente línea
## usamos el comando 's' para ejecutar la siguiente línea con la diferencia que este se adentrará en la definición de funcionalidades que estemos importando
import random
from typing import Dict
import uuid

def generar_usuario_aleatorios(cantidad:int) -> Dict[int,str]:
    breakpoint()
    nombres = ["thom", "cristina", "maria", "charlie"]
    usuarios = {}
    for x in range(cantidad):
        usuario = nombres[random.randint(0, len(nombres) - 1)]
        usuarios[uuid.uuid4()] = usuario
    return usuarios


u = generar_usuario_aleatorios(5)
print(u)



# Detener y resumir el flujo de ejecución
## utlizando el comando 'b' el nombre del módulo y la linéa (debugging:5) define un break point
## utilizando el comando 'c' se resume la ejecución del código hasta el siguiente break
## con el comando 'b' se ve la lista de todos los breakpoints
## para deshabilitar un breakpoint usamos 'disable 1' para deshabilitar el primero 
import random
from typing import Dict
import uuid

def generar_usuario_aleatorios(cantidad:int) -> Dict[int,str]:
    breakpoint()
    nombres = ["thom", "cristina", "maria", "charlie"]
    usuarios = {}
    for x in range(cantidad):
        usuario = nombres[random.randint(0, len(nombres) - 1)]
        usuarios[uuid.uuid4()] = usuario
    return usuarios


u = generar_usuario_aleatorios(5)
print(u)