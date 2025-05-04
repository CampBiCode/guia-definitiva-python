# Operadores de comparación
edad_usuario = int(input("¿Cuál es tu edad?"))
puede_pasar = "No"

if edad_usuario <= 17:
    print("No puedes pasar, eres menor de 18.")
elif edad_usuario <= 30:
    print("Puedes pasar y tienes un descuento.")
elif edad_usuario >= 50:
    print("Estas por encima de la edad máxima permitida.")
else:
    print("Puedes pasar")



# Operadores lógicos
nombre_usuario = "santiago"
clave_usuario = "12345"
clave_usuario2 = "333"
pin_usuario = "4444"

if clave_usuario == "12345" and pin_usuario == "4444" and clave_usuario2 == "333":
    print(f"Bienvenido {nombre_usuario}")
else:
    print("Clave o pin erroneo")