# Sintáxis
datos = [1, 2, 3, 4, 5, 6, 7] # debe haber un espacio entre cada elemento
datos = list((1, 2, 3, 4, 5, 6, 7))



# Acceder a un elemento
print(datos[1])
edad_usuario = datos[1]



# Multiplicación
print([1, 2] * 2)



# Slicing
## sintáxis [start:end:step]
first_list = [1, 2, 3, 4]

first_list[1:] #[2, 3, 4]

first_list[3:] #[4]

first_list = [1, 2, 3, 4]

first_list[-1:] #[4]

first_list[-3:] #[2, 3, 4]



# Iteración en listas
for x in datos:
    print(x)

for x in range(len(datos)):
    datos[x] = x


