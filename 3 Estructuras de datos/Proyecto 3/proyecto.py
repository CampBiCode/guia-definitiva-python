proveedores = []

while True:
    opcion = input("¿Selecciona una opción?(proveedores/salir):")
    
    if opcion == "proveedores":
        print("Seleccionaste proveedor")
    
        accion = input("¿Qué deseas hacer?(crear/consultar/editar/eliminar):")
    
        if accion == "crear":
            print("Seleccionaste crear un proveedor")
            salir = "no"
    
            while salir == "no":
                nuevo_proveedor = {}
    
                nombre = input("Nombre:")
                ciudad = input("Ciudad:")
                direccion = input("Dirección (x,y):")
                coordenada = []
                coordenada_x = direccion[1:3]
                coordenada_y = direccion[4:6]
                coordenada.append(coordenada_x)
                coordenada.append(coordenada_y)
                direccion = tuple(coordenada)
                telefono = input("Teléfono:")
                correo = input("Correo electrónico:")

                nuevo_proveedor["nombre"] = nombre
                nuevo_proveedor["ciudad"] = ciudad
                nuevo_proveedor["direccion"] = direccion
                nuevo_proveedor["telefono"] = telefono
                nuevo_proveedor["correo"] = correo

                proveedores.append(nuevo_proveedor)
                salir = input("¿Salir?(si/no):")

        if accion == "consultar":
            print("Seleccionaste consultar un proveedor")
            salir = "no"
    
            while salir == "no":
                nombre = input("Nombre:")
                proveedor = None
                for x in proveedores:
                    if x["nombre"] == nombre:
                        proveedor = x
    
                if proveedor is None:
                    print("El proveedor no existe")

                if type(proveedor) == dict:
                    print(f"Proveedor consultado: {proveedor}")

                salir = input("¿Salir?(si/no):")
                
        if accion == "editar":
            print("Seleccionaste editar un proveedor")
            salir = "no"
            
            while salir == "no":
                nombre = input("Nombre:")
                proveedor_editar = None
                for x in proveedores:
                    if x["nombre"] == nombre:
                        proveedor_editar = x
                        print(x)
                        
                if proveedor_editar is None:
                    print("El proveedor no existe")
                
                if type(proveedor_editar) == dict:
                    llave = input("Selecciona el dato a editar (nombre/ciudad/direccion/telefono/correo):")
                    valor = input("Nuevo dato:")
                    if llave == "direccion":
                        coordenada = []
                        coordenada_x = valor[1:3]
                        coordenada_y = valor[4:6]
                        coordenada.append(coordenada_x)
                        coordenada.append(coordenada_y)
                        valor = tuple(coordenada)
                        proveedor_editar[llave] = valor
                    else:
                        proveedor_editar[llave] = valor

                salir = input("¿Salir?(si/no):")

        if accion == "eliminar":
            print("Seleccionaste eliminar un proveedor")
            salir = "no"

            while salir == "no":
                nombre = input("Nombre:")
                proveedor_eliminar is None
                for x in proveedores:
                    if x["nombre"] == nombre:
                        proveedor_eliminar = proveedores.index(x)
                        
                if proveedor_eliminar == None:
                    print("El proveedor no existe")
                
                if type(proveedor_eliminar) == int:
                    proveedor_eliminado = proveedores.pop(proveedor_eliminar)
                    print(f"Eliminaste a: {proveedor_eliminado}")

                salir = input("¿Salir?(si/no)")

    elif opcion == "salir":
        break

print(proveedores)