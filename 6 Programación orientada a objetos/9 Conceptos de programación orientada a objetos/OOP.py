# Herencia
## sintáxis básico
## ocurre cuando una clase hereda las funcionalidades de otra para evitar el código redundante
## se crea una relación

    # se denomina clase base o super clase
class Animal:
    def comer(self):
        print("Comiendo...")

    # se denomina subclase
class Dog(Animal):  # se coloca entre paréntesis la clase de la que queremos heredar
    def ladrar(self):
        print("Ladrar!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

c = Cat()
d = Dog()

c.comer()
d.comer()



# Polimorfismo
## es la habilidad de utilizar un mismo método en diferentes tipos de objetos y este método hará algo diferente dependiendo del tipo de objeto que estemos referenciando
### es una clase que como atributo usa otra clase
### permite diseños flexibles y modulares
from abc import ABC, abstractmethod

class VideoDownloader(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def descargar_video():
        pass

class VideoDownloaderMP3(VideoDownloader):
    def descargar_video(self):
        print("Descargando video en formato mp3")
        print(f"Video descargado de {self.url}")

class VideoDownloaderAVI(VideoDownloader):
    def descargar_video(self):
        print("Descargando video en formato AVI")
        print(f"Video descargado de {self.url}")

class Video:
    def __init__(self, downloader:VideoDownloader):
        self.donwloader = downloader
    
    def descargar_video(self, url):
        self.donwloader(url).descargar_video()

video1 = Video(VideoDownloaderMP3)

video1.descargar_video("w")



# Abstracción
## existen para ser heredadas, pero nunca instanciadas
## se utiliza el modulo ABC para definirlas
from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_nomina():
        pass

class EmpleadoMensual(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_nomina(self):
        return self.salario_mensual
    
class EmpleadoSemanal(Empleado):
    def __init__(self, nombre, salario_semanal):
        super().__init__(nombre)
        self.salario_semanal = salario_semanal

    def calcular_nomina(self):
        return self.salario_semanal * 4
    
class EmpleadoDiario(Empleado):
    def __init__(self, nombre, salario_diario):
        super().__init__(nombre)
        self.salario_diario = salario_diario

    def calcular_nomina(self):
        return self.salario_diario * 30

class SistemaNomina:
    def calcular_nomina(self, empleados:list[Empleado]):
        for empleado in empleados:
            print(f"Al empleado {empleado.nombre} se le debe transferir {empleado.calcular_nomina()}")

empleado1 = EmpleadoMensual("Maria", 1500)
empleado2 = EmpleadoSemanal("Thom", 300)
empleado3 = EmpleadoDiario("Cristina", 50)
empleados = [empleado1, empleado2, empleado3]

nomina = SistemaNomina()
nomina.calcular_nomina(empleados)



# Encapsulamiento
## visibilidad pública: el atributo puede ser accedido desde cualquier lugar
## visibilidad protegida: el atributo solo puede ser utilizado dentro del mismo módulo o archivo .py
## visibilidad privada: el atributo solo puede ser utilizado dentro de la misma clase
class Carro:
    def __init__(self, marca, color, modelo):
        self.marca = marca # público
        self._color = color ## protegido
        self.__modelo = modelo ## privado
