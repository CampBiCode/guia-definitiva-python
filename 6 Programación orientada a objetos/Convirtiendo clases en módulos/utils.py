# Sin enumeraciones
import pandas as pd
import os

class LectorDB:
    def cargar_base(self, ruta:str, extension:str):
        if extension == "csv":
            return self.__cargar_csv(ruta)
        
        if extension == "xlsx":
            return self.__cargar_exceL(ruta)

    def __cargar_csv(self, ruta:str):
        df = pd.read_csv(ruta)
        return df

    def __cargar_exceL(self, ruta:str):
        df = pd.read_excel(ruta)
        return df
    
    

# Con enumeraciones
from enum import Enum
class Extension(Enum):
    CSV = "csv"
    EXCEL = "excel"

class LectorDB:
    def cargar_base(self, ruta:str, extension:Extension):
        if extension == Extension.CSV:
            return self.__cargar_csv(ruta)
        
        if extension == Extension.EXCEL:
            return self.__cargar_exceL(ruta)

    def __cargar_csv(self, ruta:str):
        df = pd.read_csv(ruta)
        return df

    def __cargar_exceL(self, ruta:str):
        df = pd.read_excel(ruta)
        return df
