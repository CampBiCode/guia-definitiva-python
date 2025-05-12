# Ejemplo sin enumeraciones
from utils import LectorDB

l = LectorDB()
df = l.cargar_base(
        ruta = "C:/Users/santi/Desktop/Guía lecciones/6 Programación orientada a objetos/8 Convirtiendo clases en módulos/tips.csv",
        extension = "csv")

print(df)



# Ejemplo con enumeraciones
from utils import LectorDB, Extension

l = LectorDB()
df = l.cargar_base(
        ruta = "C:/Users/santi/Desktop/Guía lecciones/6 Programación orientada a objetos/8 Convirtiendo clases en módulos/tips.csv",
        extension = Extension.CSV)

print(df)

