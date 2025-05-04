# Introducción a los parámetros: Son una forma de pasar datos durante la ejecución de una función
def saludar(nombre):
    print(f"¡Hola {nombre}!")

saludar("Andrew")

def multiplicar(x, y):
    return x * y

x = multiplicar(4, 5)

def saludar(nombre, n):
    for x in range(n):
        print(f"¡Hola {nombre}!")

saludar("Andrew", 4)

def registrar_usuarios(usuario1, usuario2, usuario3, usuario4):
    usuarios = [usuario1, usuario2, usuario3, usuario4]
    return usuarios

usuarios = registrar_usuarios("santiago", "felipe", "thom", "andrea")



# Diferencia entre argumento y parámetro
## se asignan en orden y todos son requeridos
def registrar_usuarios(usuario1, usuario2, usuario3, usuario4):
    usuarios = [usuario1, usuario2, usuario3, usuario4]
    return usuarios

registrar_usuarios("santiago", "felipe", "thom", "andrea")
registrar_usuarios(usuario3="santiago", usuario4="felipe", usuario2="thom", usuario1="andrea")



# Valores predeterminados
## permiten que la función se llame sin proporcionar agumentos para los parámetros que se configuren de esta manera
def saludar(nombre, n=10):
    for x in range(n):
        print(f"¡Hola {nombre}!")

saludar("Andrew")

def longitud(datos, mensaje="La longitud es"):
    return f"{mensaje}:{len(datos)}"

## primero van los parámetros requeridos y luego los predeterminados
def crear_usuario(usuario, datos = []):
    datos.append(usuario)
    return datos

datos = crear_usuario("santiago")
print(datos)
datos = crear_usuario("felipe")
print(datos)
datos = crear_usuario("andrew")
print(datos)

def crear_usuario(usuario, datos = None):
    if datos is None:
        datos = []
    datos.append(usuario)
    return datos

datos = crear_usuario("santiago")
print(datos)
datos = crear_usuario("felipe")
print(datos)
datos = crear_usuario("andrew")
print(datos)

## los objetos originales pasados como argumento de una función no son modificados a pesar de ser mutables dentro de la función
## funcionan como si se creará una copia de estos
def transformar(datos): 
    datos = [x*2 for x in datos]
    return datos

datos = [1, 2, 3]

datos2 = transformar(datos)
print(datos)
print(datos2)
