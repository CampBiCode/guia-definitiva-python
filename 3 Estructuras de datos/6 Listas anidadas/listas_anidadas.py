# Lista anidadas
listas_numeros = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## accediendo a valores según indice
print(listas_numeros[0][1])

## accediendo a valores con for loops
numeros = []
for x in listas_numeros:
    for n in x:
        print(n)
        numeros.append(n)
print(numeros)

## list comprehension
listas_numeros = [[x for x in range(3)] for x in range(3)]

## list comprehension y lógica condicional
datos = [[1, 20], [2, 30], [3, 50], [4, 32], [5, 22]]
datos = [["cumple" if x > 30 else "no cumple" for x in l] for l in datos]
print(datos)

datos = [["andrew", 20], ["karen", 30], ["thom", 50], ["elizabeth", 32], ["austin", 22]]

for x in range(len(datos)): 
    if datos[x][1] > 30:
        datos[x].append("cumple")
    else:
        datos[x].append("no cumple")

print(datos)