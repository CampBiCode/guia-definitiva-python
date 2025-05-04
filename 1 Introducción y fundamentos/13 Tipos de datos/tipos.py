# En esta lección introducimos los diferentes tipos de datos soportados por Python

# String (str): Representa una cadena de texto
nombre_usuario = "Santiago"

## string de múltiples lineas
nombre_empresa = """Coca cola
múltiples
lineas."""

## métodos de los Strings
nombre_usuario = "santiago"
nombre_usuario.upper() # convierte el texto a mayúscula
nombre_usuario.lower() # convierte el texto a minúscula
nombre_usuario.capitalize() # convierte el primer carácter a mayúscula y el resto a minúscula
nombre_usuario.count("a") # regresa la cantidad de aparaciones de un carácter dentro de un texto
nombre_usuario.find("an") # busca una subcadena dentro de otra cadena y devuelve la posición donde comienza la primera coincidencia
nombre_usuario.replace("a", "A") # remplaza partes de un string por otro texto nuevo
nombre_usuario.strip() # remueve carácteres vacios de un texto
nombre_usuario.startswith("san") # verifica si un string comienza con una subcadena específica
nombre_usuario.endswith("ago") # verifica si un string termina con una subcadena específica
len(nombre_usuario) # obtener la longitud (cantidad de carácteres) de una cadena de texto



# Integer (int): Representa un número entero
edad = 24



# Float (float): Representa un número con decimales
longitud = 2.24

## métodos de los valores númericos (int/float)
abs(-3.2) # devuelve el valor absoluto de un número
pow(3, 2) # calcula la potencia de un número
round(3.61231) # redondea un número al entero más cercano



# Boolean (bool): Representa un valor que solo puede tener dos valores posibles True o False
es_mayor_de_edad = False
esta_lloviendo = True



# None (None): Representa la ausencia de un valor
esta_lloviendo = None