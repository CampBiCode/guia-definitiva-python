# Sintáxis
# variable = {key1:value1, key2:value2}
base_datos = {"nombre":"santiago", "edad":24, "color":"azul", "musica":"rock", "pais":"colombia"}
print(type(base_datos))
print(base_datos["edad"])

## reasignación de valores
base_datos["edad"] = 44

## funcion dict
base_datos = dict(nombre="santiago", edad=24, color="azul", musica="rock", pais="colombia")

## validar por existencia
print("color" in base_datos) # True
print("azul" in base_datos) # False
print("azul" in base_datos.values())

print(base_datos.keys())
print(base_datos.values())
print(base_datos.items())



# iterar diccionarios
base_datos = {"nombre":"santiago", "edad":24, "color":"azul", "musica":"rock", "pais":"colombia"}

## iterar llaves
for x in base_datos.keys():
    print(x)
    if x == "edad":
        base_datos[x] = base_datos[x] * 2

## iterar valores
valores = []
for x in base_datos.values():
    print(x)
    valores.append(x)

## iterar items
for key, value in base_datos.items():
    print(key, value)
    if key == "edad":
        base_datos[key] = value * 2



# listas y diccionarios
## listas dentro de diccionarios
base_datos = {"nombre":"santiago", "edad":24, "color":"azul", "musica":["rock", "techno", "jazz"], "pais":"colombia"}

for key, value in base_datos.items():
    if key == "musica":
        nuevo_genero = input("¿Qué genero agrego?")
        base_datos[key].append(nuevo_genero)
print(base_datos)


## diccionarios dentro de listas
usuarios = [{"nombre":"santiago", "edad":24, "color":"green"}, 
            {"nombre":"andrew", "edad":33, "color":"blue"},
            {"nombre":"sara", "edad":54, "color":"yellow"},
            {"nombre":"cristian", "edad":33, "color":"pink"}]

usuarios = [x["nombre"] for x in usuarios]

for x in range(len(usuarios)):
    print(usuarios[x])
    usuarios[x]["nombre"] = usuarios[x]["nombre"].lower()[:3]

print(usuarios)
