# Rutas
## se conforman de:
### ruta de carpetas
### nombre del archivo
### extension
ruta = "assets/data/data.csv" # ruta desde la carpeta actual
ruta = "C:/Users/user/Desktop/Guía lecciones/8 Otros conceptos/2 Trabajar con archivos en Python/assets/data/data.csv" # ruta desde otra carpeta



# Abrir y cerrar archivos de Python
archivo = open("archivo.txt") 
archivo.close() # una vez abierto siempre debe cerrarse

## la segunda forma es utilizar un bloque with
with open("archivo.txt") as archivo: # se encarga de cerrar el archivo automáticamente
    pass



# Escribir y leer archivos
## leer
with open("archivo.txt", "r") as archivo:
    pass

## escribir
with open("archivo.txt", "w") as archivo:
    pass

## leer lineas
with open("archivo.txt", "r") as archivo:
    print(archivo.read()) # lee todas las lineas del archivo
    print(archivo.readline()) # lee línea por linea
    print(archivo.readlines()) # lee el resto de lineas y las retorna en una lista

### iterar las lineas de un archivo
with open("archivo.txt", "r") as archivo:
    lineas_importantes = []
    for x in archivo.readlines():
        if x[0].lower() == "p":
            lineas_importantes.append(x)

print(lineas_importantes)


## Escribir lineas
### si usamos el nombre de un archivo que no existe lo crea, si no lo sobreescribe
with open("nuevo_archivo.txt", "w") as archivo: 
    archivo.write("Hola mundo\n")
    archivo.write("Mi nombre es Santiago.\n")
    lineas = [
        "Primera\n"
        "Segunda\n"
        "Tercera\n"
    ]
    archivo.writelines(lineas)

### agregar una linea adicional
with open("nuevo_archivo.txt", "a") as archivo:
    archivo.write("\nnueva linea")