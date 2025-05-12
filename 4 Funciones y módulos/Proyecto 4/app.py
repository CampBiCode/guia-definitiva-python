from utils.usuarios import crear_usuario, introducir_nombre, introducir_especialidad, editar_usuario
from utils.enemigos import crear_enemigos
from utils.batallas import crear_batalla

usuario = ""
enemigos = ""
opciones_menu = ["crear usuario", "editar usuario", "crear enemigos", "batalla", "salir"]

while True:

    menu_principal = input(f"¿Selecciona una opción? ({"/".join(opciones_menu)}): ").lower().strip()

    if menu_principal != "salir":

        if menu_principal == "crear usuario":
            print("Seleccionaste crear un usuario")
            nombre = introducir_nombre()
            especialidad = introducir_especialidad()
            usuario = crear_usuario(nombre, especialidad)
            print(f"Usuario creado: {usuario}")
            opciones_menu.remove("crear usuario")

        if menu_principal == "editar usuario":
            if usuario:
                print("Seleccionaste editar un usuario")
                usuario = editar_usuario(usuario)
                print(f"Usuario editado: {usuario}")
            else:
                print("Debes crear un usuario primero")

        if menu_principal == "crear enemigos":
            if usuario:
                print("Seleccionaste crear enemigos")
                enemigos = crear_enemigos()
                print(f"Enemigos creados: {enemigos}")
                opciones_menu.remove("crear enemigos")
            else:
                print("Debes crear un usuario primero")

        if menu_principal == "batalla":
            if usuario and enemigos:
                print("Seleccionaste batalla")
                resultado = crear_batalla(enemigos)
                if resultado == 1:
                    usuario["victorias"] += 1
                elif resultado == 0:
                    usuario["derrotas"] += 1
                    
                print(f"Puntaje actual: {usuario}")
            else:
                print("Aún no has creado un usuario o un listado de enemigos")

    if menu_principal == "salir":
        if usuario:
            print(f"Resultado final: {usuario}")
            break
        else:
            break