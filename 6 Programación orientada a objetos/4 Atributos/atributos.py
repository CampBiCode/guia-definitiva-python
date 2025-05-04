# Atributos de clase vs atributos de instancia
## atributos de clase
### todos los objetos creados a partir de una misma clase van a compartir los mismos atributos
class Empresa:
    tipos = ["SaaS", "PaaS", "IaaS"]
    
    def __init__(self):
        print("Creaste un objeto de clase Empresa")
        print(self.tipos)


e1 = Empresa()
e2 = Empresa()
print(e2.tipos)

## atributos de instancia
### los atributos están asociados al ojbeto de la clase
import datetime as dt

class Carro:
    def __init__(self, marca, color, modelo = dt.date.today().year):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = 0
        self.velocidad_maxima = 200

c1 = Carro(marca = "Mazda", color = "Azul")
print(c1.color)
print(c1.marca)
print(c1.modelo)

## saber de que clase es un objeto
print(type(c1))
print(isinstance(c1, Carro)) # es una instancia de la clase carro

## imprimir todos los atributos de un objeto
print(c1.__dict__)



# modificar atributos
class Usuario:
    pass

u = Usuario()
## agregar atributos a una clase
setattr(u, "nombre", "Santiago")
print(u.nombre)

## retornar atributos
print(getattr(u, "nombre", 800))

## comprobar existencia de un atributo
print(hasattr(u, "nombre"))

## eliminar atributo
delattr(u, "nombre")
print(u.nombre)



# Encapsulamiento
## visibilidad pública: el atributo puede ser accedido desde cualquier lugar
## visibilidad protegida: el atributo solo puede ser utilizado dentro del mismo módulo o archivo .py
## visibilidad privada: el atributo solo puede ser utilizado dentro la misma clase

class Carro:
    def __init__(self, marca, color, modelo):
        self.marca = marca # público
        self._color = color # protegido
        self.__modelo = modelo # privado
