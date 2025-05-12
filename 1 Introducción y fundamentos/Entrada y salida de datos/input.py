# Introducción a la función Input
print("¡Hola bienvenido a nuestro programa!")
nombre = input("¿Cómo te llamas?")
edad = int(input("¿Cuál es tu edad?"))
print(nombre)
print(edad)



# Opciones de la función print
nombre_empresa = "Coca Cola"
edad_empresa = 200
print("Nombre de la empresa", nombre_empresa, "Edad de la empresa", edad_empresa)



# F-strings
nombre_usuario = "santiago"
email_usuario = "santiago@gmail.com"
edad_usuario = 24
print(f"Hola {nombre_usuario}. Tu email es {email_usuario} y tú edad es: {str(edad_usuario)}")