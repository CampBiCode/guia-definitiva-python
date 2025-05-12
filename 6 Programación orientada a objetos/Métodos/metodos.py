# Tipos de métodos
## métodos de instancia
### toman la instancia actual (self) como el primer argumento
import datetime as dt

class Empleado:
    def __init__(self, nombre:str, identificacion:str, profesion:str, fecha_ingreso:dt.date):
        self.nombre = nombre
        self.identificacion = identificacion
        self.profesion = profesion
        self.fecha_ingreso = fecha_ingreso
        self.estado_activo = False
        
    def calcular_antiguedad(self):
        fecha_actual = dt.date.today()
        dias_antiguedad = (fecha_actual - self.fecha_ingreso).days
        print(f"El empleado {self.nombre} con identificacion {self.identificacion} tiene {dias_antiguedad} días de antiguedad.")

    def activar_empelado(self):
        print("Activando empleado...")
        self.estado_activo = True
        print("Empleado activo.")

e1 = Empleado("santiago", "123", "abogado", dt.date(2005, 12, 12))
e1.calcular_antiguedad()

## métodos de clase
### toman la clase (cls) como el primer argumento
#### ejemplo: modificar un atributo de clase
class Empleado:
    tasa_aumento = 1.05

    def __init__(self, salario):
        self.salario = salario

    @classmethod
    def set_tasa_aumento(cls, tasa):
        cls.tasa_aumento = tasa

emp1 = Empleado(12333)
emp2 = Empleado(20000)

Empleado.set_tasa_aumento(1.6)

print(emp1.tasa_aumento)
print(emp2.tasa_aumento)

#### ejemplo: llevar conteo de instancias
class Coche:
    cantidad_coches = 0  

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Coche.cantidad_coches += 1

    @classmethod
    def mostrar_cantidad_coches(cls):
        print(f"La cantidad total de coches es: {cls.cantidad_coches}")

coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")
coche3 = Coche("Ford", "Focus")

Coche.mostrar_cantidad_coches()

## métodos estáticos
### no toman ni la clase ni la instancia como argumentos. Funcionan de manera independiente
class Universidad:
    def __init__(self, nombre:str):
        self.nombre = nombre

    @staticmethod
    def fecha_actual():
        print(dt.date.today())

Universidad.fecha_actual()



# Métodos especiales
## __repr__
class Empleado:
    def __init__(self, nombre:str, identificacion:str, profesion:str, fecha_ingreso:dt.date):
        self.nombre = nombre
        self.identificacion = identificacion
        self.profesion = profesion
        self.fecha_ingreso = fecha_ingreso
        self.estado_activo = False
    
    ## __repr__: representación en forma de String cuando utilicemos la función str() o print() sobre el objeto
    def __repr__(self):
        return f"Esta es una instancia de la clase empleado con estos datos {self.__dict__}"
e = Empleado("santiago", "22123123", "ingeniero", dt.date(2006, 12, 31))
print(str(e))
print(e)