# Introducción a las clases
## proveen una manera elegante de definir y reutilizar piezas de código que alamacenan datos y comportamiento en una sola entidad
## son una plantilla que permite crear objetos o instancias que cumplen con unas características predefinidas
## se definen utilizando la palabra clave class
class Estudiante:
    pass

e1 = Estudiante() # cuando creamos un objeto se llama instanciar o crear una instancia de una clase



# Atributos
## valores definidos dentro de la clase con el proposito de almacenar toda la información necesaria para que la clase funcione
## tipos de atributos
### atributos de la clase
class Musician:
    titulo = "Rockstar"

### atributos de la instancia u objeto, este constructor crea la clase pasando los argumentos que son necesarios para su creación
class SearchEngineEntry:
    def __init__(self, url): # __init___ es el metodo inicializador del objeto porque define sus valores iniciales
        self.url = url # self es el encargado de referenciar los atributos del objeto actual

### el método __init__ es llamado cada vez que se crea un nuevo objeto
class Gritar:
    def __init__(self):
        print("HELLO")

grito1 = Gritar()



# Métodos
class Altavoz:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def gritar_mensaje(self, n):
        for x in range(n):
            print(self.mensaje)

e1 = Altavoz("Hola")
e1.gritar_mensaje(10)

## ejemplo
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False

    def encender(self):
        if not self.encendido:
            print("El coche está encendido")
            self.encendido = True
        else:
            print("El coche ya está encendido")

    def apagar(self):
        if self.encendido:
            print("El coche está apagado")
            self.encendido = False
        else:
            print("El coche ya está apagado")

    def estado(self):
        if self.encendido:
            print("El coche está encendido")
        else:
            print("El coche está apagado")

coche1 = Coche("Toyota", "Corolla", "Azul")

coche1.encender()
coche1.estado()
coche1.apagar()
coche1.estado()

print(f"Mi caro es de la marca {coche1.marca} y es {coche1.color}")



# Beneficios del uso de las clases
## modelar problemas complejos de la vida real
## código amigable, más organizado
## encapsular: oculta los detalles internos de su implementación y expone solo la interfaz necesaria para interactuar con la clase