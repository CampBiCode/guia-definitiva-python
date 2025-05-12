# Comentarios
## consiste es describir el código para otros desarrolladores


## reglas para comentar: máximo 72 caracteres


## objetivos de comentar código
### planear código
def modificar_usuarios():
    pass
    # se crea una nueva lista de usuarios
    # se itera sobre el listado original de usuarios
    # se guarda el usuario modificado en la nueva lista de usuarios

### describir código: explicar la intención del código
def convertir_en_diccionario():
    # convierte los elementos de una lista en un diccionario
    pass

### marcar secciones del código
def procesar_pago():
    # BUG: cuando es un nuevo usuario el pago no queda registrado
    # TODO: investigar cómo mejorar el rendimiento
    pass



# Docstrings
## son cadenas de texto que explican el funcionamiento del código
help(str)

def iniciar_sesion(usuario:str, contrasena:str) -> None:
    """Permite iniciar sesión a un usuario, siempre y cuando
       su contraseña este correcta."""
    print(f"Hola {usuario} has iniciado sesión.")
help(iniciar_sesion)


## estándar de Google para docstrings
"""
    Breve descripción:

    Args:
        param1: primer parámetro.
        param2: segundo parámetro.

    Retorna:
        Descripción de lo que retorna.
"""


## documentar una clase
class Calculadora:
    """
    Una clase para realizar operaciones aritméticas básicas.

    Métodos
    -------
    sumar(a, b)
        Devuelve la suma de a y b.
    
    restar(a, b)
        Devuelve la resta de b de a.
    
    multiplicar(a, b)
        Devuelve el producto de a y b.
    
    dividir(a, b)
        Devuelve la división de a por b. Lanza una excepción si b es cero.
    """

    def sumar(self, a, b):
        """
        Suma dos números.

        Parámetros:
            a : float
                El primer número a sumar.
            b : float
                El segundo número a sumar.

        Retorna:
            float
                La suma de a y b.
        """
        return a + b

    def restar(self, a, b):
        """
        Resta el segundo número del primero.

        Parámetros:
            a : float
                El número del que se va a restar.
            b : float
                El número que se va a restar.

        Retorna:
            float
                La diferencia entre a y b.
        """
        return a - b

    def multiplicar(self, a, b):
        """
        Multiplica dos números.

        Parámetros:
            a : float
                El primer número a multiplicar.
            b : float
                El segundo número a multiplicar.

        Retorna:
            float
                El producto de a y b.
        """
        return a * b

    def dividir(self, a, b):
        """
        Divide el primer número por el segundo.

        Parámetros:
            a : float
                El numerador.
            b : float
                El denominador. No debe ser cero.

        Retorna:
            float
                El cociente de a y b.

        Lanza:
            ValueError
                Si b es cero.
        """
        if b == 0:
            raise ValueError("El divisor no puede ser cero.")
        return a / b
