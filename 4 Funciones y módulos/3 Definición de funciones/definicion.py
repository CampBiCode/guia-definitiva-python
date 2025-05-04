# Funciones integradas: Podemos usar help para mostrar la información de una función integrada o definida por nosotros
datos = list(range(100))
print(len(datos))

help(print)
help(len)



# Sintáxis de la definición de funciones
def saludar():
    print("¡Hola, bienvenid@!")

saludar()
saludar()
print(help(saludar))

def multiplicar():
    x = int(input("¿Cuál es el valor para la variable x?:"))
    y = int(input("¿Cuál es el valor para la variable y?:"))
    resultado = x * y
    print(resultado)

def almacenar_nombres():
    nombres = []
    for x in range(3):
        nombre = input("Indica un nombre:")
        nombres.append(nombre)

    nombres = [x.lower() for x in nombres]
    print(nombres)



# Palabra clave Return
## regresa cualquier objeto
def almacenar_nombres():
    nombres = []
    for x in range(3):
        nombre = input("Indica un nombre:")
        nombres.append(nombre)

    nombres = [x.lower() for x in nombres]
    return nombres

### se pueden usar múltiples return en una misma función pero la función deja de ejecutarse una vez llegue al primer return
def editar_personas():
    datos = ["andrew", "thom", "michael"]
    modificar = "mayuscula"
    if modificar == "mayuscula":
        datos = [x.upper() for x in datos]    
        return datos
    
    if modificar == "minuscula":
        datos = [x.lower() for x in datos]
        return datos
    
## terminar la ejecución del código
def validar_edad():
    edad = 34
    if edad > 34:
        return
    else:
        print("Tu edad no es valida")

## varios valores separados por coma en el return serán empaquetados en una tupla
def f():
    return "nombre", "ciudad", "profesion"

