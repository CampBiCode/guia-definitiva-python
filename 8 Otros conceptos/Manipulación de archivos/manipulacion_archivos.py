# Leer archivos de un directorio
import os

archivos = os.listdir("directorio/")
print(archivos)


from pathlib import Path # forma preferida ya que contiene más metadata sobre el archivo

archivos = Path("directorio/")
archivos_gen = archivos.iterdir()
for a in archivos_gen:
    if a.name[-1].lower() == "2":
        print(a.name)

## validar si un elemento de un directorio es un archivo
from pathlib import Path

ruta_base = Path("directorio/sub 2/")
archivos = ruta_base.iterdir()

for archivo in archivos:
    if archivo.is_file(): # el método válida si el elemento es un archivo
        print(archivo.name)

## listar sub-directorios
from pathlib import Path

ruta_base = Path("directorio/")
for archivo in ruta_base.iterdir():
    if archivo.is_dir():
        print(archivo.name)


## acceder a los atributos de un archivo como:
### tamaño del archivo
### fecha de creación
### fecha de modificación

from pathlib import Path
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    fecha_formato = d.strftime("%d %b %Y")
    return fecha_formato

current_dir = Path("directorio")
for archivo in current_dir.iterdir():
    info = archivo.stat()
    print(convert_date(info.st_mtime)) # fecha de modificación
    print(convert_date(info.st_ctime)) # fecha de creación



# Creación de archivos
## crear carpeta
from pathlib import Path

p = Path("carpeta ejemplo/")
p.mkdir(exist_ok=True) # con el argumento 'exist_ok=True' evitamos errores en el caso de que la carpeta ya existe

## crear múltiples carpetas
from pathlib import Path

p = Path("2018/10/05")
p.mkdir(parents=True)

## buscar archivo por nombre
import os
for archivo in os.listdir("directorio/sub 1"):
    if archivo.startswith("app1"):
        print(archivo)

## acceder a carpetas y subcarpetas
import os

for carpeta_actual, sub_carpetas, archivos in os.walk("."):
    print(f"Carpeta encontrada {carpeta_actual}")
    for nombre_archivo in archivos:
        print(nombre_archivo) 

## crear archivos temporales
### se eliminan luego de ser utilizados
from tempfile import TemporaryFile
                  # modo escritura
with TemporaryFile("w+t") as fp:
    fp.write("Welcome")
    fp.seek(0)
    mensaje = fp.read()

print(mensaje)



# Mover archivos
## eliminar archivos
import os
archivo = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/directorio/sub 1/app1.py"
os.remove(archivo)

## eliminar carpetas vacías
import os
carpeta = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/directorio/sub 1/sub 1.1"
os.rmdir(carpeta)

## eliminar carpetas vacías y no vacías
import shutil
carpeta = "2018"
shutil.rmtree(carpeta)

## copiar archivos
import shutil
origen = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/carpeta original/programa.py"
destino = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/carpeta destino"
shutil.copy(origen, destino) # si el destino es un archivo y no una carpeta, el archivo será remplazado

## mover archivos
origen = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/carpeta original/programa.py"
destino = "C:/Users/santi/Desktop/Guía lecciones/8 Otros conceptos/4 Manipulación de archivos/carpeta destino"
shutil.move(origen, destino) 

## renombrar archivos
from pathlib import Path
archivo = Path("directorio")
archivo.rename("nuevo_directorio")