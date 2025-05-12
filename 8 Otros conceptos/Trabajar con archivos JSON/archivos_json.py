# Módulo JSON
import json
## convertir un diccionario a una cadena JSON
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data) # proceso de codificación
print(json_string)
print(type(json_string))

## guardar json en un archivo
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("data.json", "w") as archivo_json:
    json.dump(data, archivo_json)

## leer json desde un archivo
import json

with open("data.json", "r") as archivo_json:
    data = json.load(archivo_json) # proceso de decodificación

print(data)

## convertir JSON a Python
import json

cadena_json = '{"name": "John", "age": 30, "city": "New York"}'

data = json.loads(cadena_json)
print(data)

## opciones adicionales de json.dumps()
### formato con indent
import json 

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
cadena_json = json.dumps(data, indent=4)
print(cadena_json)

### ordenar llaves con sort_keys
import json 

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
cadena_json = json.dumps(data, sort_keys = True, indent = 4)
print(cadena_json)



# Manejo de errores
import json

cadena_json = '{"name": "John", "age": 30, "city": "New York"'

try:
    data = json.loads(cadena_json)
except json.JSONDecodeError as e:
    print(f"Error al decodificar JSON: {e}")