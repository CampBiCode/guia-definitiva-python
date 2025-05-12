# Especifican la región del código donde una variable o nombre es accesible
# Ámbito global: Se definen fuera de las funciones y son accesibles en cualquier parte del programa
total = 0

def sumar_uno():
    global total
    total += 1
    return total

print(sumar_uno())

## si solo estamos referenciando la variable global sin modificarla podemos saltarnos la palabra clave global
usuario = "Usuario1"

def nombramiento():
    print(usuario)

nombramiento()



# Ambito local: Se refiere al interior de una función o método
def sumar_uno():
    total = 0
    total += 1
    return total

print(sumar_uno())



# Ámbito enclosing (no local): Se refiere al ámbito de las funciones anidadas
## funciona como el ámbito global pero en funciones anidadas
def funcion_externa():
    x = 10

    def funcion_interna():
        print(x)
        
    funcion_interna()


funcion_externa()