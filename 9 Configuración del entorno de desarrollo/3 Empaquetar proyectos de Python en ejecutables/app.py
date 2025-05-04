from utils.data_generator import generate_data
import pandas as pd

print("Hola, bienvenido a nuestra aplicación")

columns = int(input("¿Cuántas columnas quieres usar?:"))
rows = int(input("¿Cuántas filas quieres usar?:"))

data = generate_data(columns = columns, rows = rows)

data.to_csv("data.csv", index = False)