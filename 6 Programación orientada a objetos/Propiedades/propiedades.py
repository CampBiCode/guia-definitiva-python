# Propiedades
## permiten agregar logica a la reasignación y eliminación de atributos
class Caja:
    def __init__(self, peso):
        self.__peso = peso # atributo privado

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        if peso >= 0:
            self.__peso = peso

    @peso.deleter
    def peso(self):
        del self.__peso


mi_caja = Caja(10)

print(mi_caja.peso)

mi_caja.peso = 15
print(mi_caja.peso)

del mi_caja.peso
print(mi_caja.peso)