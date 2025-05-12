# Sintáxis básico

# nueva_lista = [expresion for elemento in iterable if condicion]

numeros = [1, 2, 3, 4, 5, 6]
numeros = [[x for x in numeros]]
numeros = [[x * 10 for x in numeros]]

numeros = [x / 2 for x in range(10)]

datos = ["Andrew", "Karen", "Thom", "Elizabeth"]
datos = [x[0].lower() + x[1:].upper() for x in datos]

# for loop equivalente
numeros = [1, 2, 3, 4, 5, 6]
nuevo_numeros = []
for x in numeros:
    numero = x * 10
    nuevo_numeros.append(numero)



# List comprehension con lógica condicional 
## 1 condicional para excluir o mantener
datos = ["Andrew", "Karen", "Thom", "Elizabeth", "Austin"]
datos = [x for x in datos if x[0].lower() == "a"] # no se usa else

numeros = list(range(10))
numeros = [x for x in numeros if x % 2 == 0]

## 2 condicional para modificar la expresion
numeros = list(range(10))
numeros = [0 if x%2 == 0 else x for x in numeros]

datos = ["Andrew", "Karen", "Thom", "Elizabeth", "Austin"]
datos = ["cumple" if x[0].lower() == "a" else "cumple" if x[-1].lower() == "n" else "no cumple" for x in datos]
datos = ["cumple" if x[0].lower() == "a" or x[-1].lower() == "n" else "no cumple" for x in datos]