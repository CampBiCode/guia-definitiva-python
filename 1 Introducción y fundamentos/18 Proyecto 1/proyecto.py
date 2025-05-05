print("Hola, por favor comparteme tus siguientes datos:")
nombre = input("Nombre completo:")
correo_electronico = input("Correo electrónico:")
a_o_nacimiento = int(input("Año de nacimiento:"))
ciudad = input("Ciudad:")
porcentaje_bono = float(input("Porcetanje bono:"))
sueldo = int(input("Sueldo:"))

nombre = nombre.title().strip()
ciudad = ciudad.title().strip()
correo_electronico = correo_electronico.lower().strip()
edad = 2024 - a_o_nacimiento
porcentaje_bono = porcentaje_bono / 100
nuevo_sueldo = round(sueldo * (1 + porcentaje_bono))

mensaje = f"¡Hola {nombre}, bienvenid@! Hoy empieza tu aventura en nuestra empresa.\nEstos son algunos datos sobre ti: tu correo electrónico es {correo_electronico}, tu edad es {edad} años y vives en la ciudad de {ciudad}.\nSi cumples tus metas recibirás este sueldo ${nuevo_sueldo}, ánimo, sé que puedes lograrlo."

print(mensaje)
