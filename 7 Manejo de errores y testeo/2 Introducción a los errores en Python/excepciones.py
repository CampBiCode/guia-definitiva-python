# Definición
## un programa de Python se termina cuando encuentra un error
## existen dos tipos de errores en Python, de sintáxis y excepciones

## Errores de sintáxis
### ocurren cuando nuestro programa identifica un uso incorrecto de código
print(1 / 2)) # la flecha indica donde se encuentra el error

## errores de tipo excepción
### este tipo de errores ocurre cuando código escrito correctamente resulta en un error
### estamos realizando una acción inválida
print(0 / 0) # existen diferentes tipos de excepciones, en este caso es de tipo ZeroDivisionError



# Generar excepciones
## hay ocasiones en la que vamos a querer lanzar excepciones en nuestro código
## usamos la palabra clave 'raise' y el objeto Exception
edad = 10
if edad > 5:
    raise Exception(f"La edad no debe exceder 5. (edad={edad})") # mensaje informativo
print(edad)



# Usar bloques try/except para manejar excepciones
## se usan para capturar excepciones
## permite determinar como debe reaccionar el programa si el código que se intento ejecutar genera un error de tipo Exception
def comprar_producto(producto:str):
    productos_disponibles = ["Camara", "Tripode", "Computador"]
    if not producto in productos_disponibles:
        raise Exception(f"El producto seleccionado es inválido. (producto={producto})")
    print("Compra completada.")

## ejemplo 1
try: # código que se intenta ejecutar
    comprar_producto("Esfero")
except: # código que se ejecuta en el caso de un error
    pass # no es recomendado usar pass, se debería dar algún tipo de información
    # después del bloque try/except el programa continua ejecutandose

## ejemplo 2
try:
    comprar_producto("Esfero")
except Exception as error: # en este caso capturamos el mensaje con un alias y lo podemos imprimir
    print("No se pudo ejecutar la función exitosamente.")
    print(error)

## múltiples excepciones
def dividir_numeros(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except TypeError:
        print("Error: Los operandos deben ser números.")

num1 = 10
num2 = 0
resultado = dividir_numeros(num1, num2)

## palabra clave else
### permite especificar código que debe ejecutarse en el caso de que no se haya identificado ningún error
import uuid

class Azure:
    def comprar_producto(producto:str):
        productos_disponibles = ["Camara", "Tripode", "Computador"]
        if not producto in productos_disponibles:
            raise Exception(f"El producto seleccionado es inválido. (producto={producto})")
        return uuid.uuid4()
    
    def alamacenar_compra(orden_id:str):
        print("Compra almacenada.")

try:
    orden = Azure.comprar_producto("Camara")
except Exception as error:
    print(error)
else:
    Azure.alamacenar_compra(orden)

## palabra clave finally
### es código que siempre se va a ejecutar así se haya encontrado un error en la ejecución del programa
import uuid

class Azure:
    def comprar_producto(producto:str):
        productos_disponibles = ["Camara", "Tripode", "Computador"]
        if not producto in productos_disponibles:
            raise Exception(f"El producto seleccionado es inválido. (producto={producto})")
        return uuid.uuid4()
    
    def alamacenar_compra(orden_id:str):
        print("Compra almacenada.")

    def cerrar_sesion():
        print("Sesión cerrada exitosamente.")

try:
    orden = Azure.comprar_producto("Camara")
except Exception as error:
    print(error)
else:
    Azure.alamacenar_compra(orden)
finally:
    Azure.cerrar_sesion()

