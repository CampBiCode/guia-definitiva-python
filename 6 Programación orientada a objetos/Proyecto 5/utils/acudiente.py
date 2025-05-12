from utils.id import generate_id
from abc import ABC, abstractmethod

class Acudiente(ABC):
    def __init__(self, nombre:str, pago:int):
        self.id = generate_id()
        self.nombre = nombre
        self.pago = pago

    @abstractmethod
    def calcular_pago_mensual() -> None:
        pass

class AcudienteDiario(Acudiente):
    def calcular_pago_mensual(self) -> None:
        pago_mensual = self.pago * 30
        print(pago_mensual)

class AcudienteSemanal(Acudiente):
    def calcular_pago_mensual(self) -> None:
        pago_mensual = self.pago * 4
        print(pago_mensual)        

class AcudienteMensual(Acudiente):
    def calcular_pago_mensual(self) -> None:
        print(self.pago)


