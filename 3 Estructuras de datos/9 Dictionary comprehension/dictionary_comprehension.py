# Sintáxis básico de dictionary comprehension
## {nueva_clave: nuevo_valor for elemento in iterable}

datos = {"nombre":"ANDREW", "pais":"COLOMBIA", "color":"AZUL"}
datos = {k:v.lower() for k,v in datos.items()}
print(datos)

datos = {"primero":1, "segundo":2, "tercero":3, "cuarto":4}
datos = {k:v**2 for k,v in datos.items()}
print(datos)



# Dictionary comprehension con otros iterables
## range
datos_numericos = {x:x*2 for x in range(1, 10)}
print(datos_numericos)

## listas
print({x:x**2 for x in [1, 2, 3, 4, 5]})

usuarios = ["thomas", "jack", "alejandro", "carol"]
usuarios = {x:usuarios[x] for x in range(len(usuarios))}

variables = ["nombre", "edad", "pais", "area", "cargo"]
datos_usuarios = {x:0 for x in variables}
print(datos_usuarios)



# Dictionary comprehension con lógica condicional
## condicional para modificar llaves
instructor = {
	"name":"andrew",
	"ciudad":"san francisco",
	"color":"purple"
}

instructor = {k.upper() if k == "color" else k:v.upper() for k, v in
											instructor.items()}

print(instructor)

## condicional para modificar valores
instructor = {
	"name":"andrew",
	"ciudad":"san francisco",
	"color":"purple",
    "clases": ["python", "java", "html", "css"]
}

instructor = {k.upper() if type(v) == list else k:v for k, v in instructor.items()}
print(instructor)


## condicionales para incluir o excluir
instructor = {
	"name":"andrew",
	"ciudad":"san francisco",
	"color":"purple",
    "clases": ["python", "java", "html", "css"]
}

instructor = {k:v for k,v in instructor.items() if type(v) != list}
print(instructor)

## condicionales con otros iterables
numeros = [1, 2, 3, 4, 5]
diccionario_doble_impares = {x: x*2 for x in numeros if x % 2 != 0}