# Introducción a assert
## assert nos permite hacer validaciones del resultado esperado de una función
def multiplicar_por_diez(numero):
    return numero * 100

resultado = multiplicar_por_diez(20)
       
       # condición
assert resultado == 200, f"Se esperaba que multiplicar_por_diez(20) retornara 200"
                         # mensaje de error

## varias pruebas para una sola función
### se pueden definir en un módulo separado
def test_multiplicar_diez_por_cero():
    assert multiplicar_por_diez(0) == 0, "Se esperaba que multiplicar_por_diez(0) retornara 0"

def test_multiplicar_diez_por_un_millon():
    assert multiplicar_por_diez(1000000) == 10000000, "Se esperaba que multiplicar_por_diez(1000000) retornara 10000000"

def test_multiplicar_diez_por_numero_negativo():
    assert multiplicar_por_diez(-10) == -100, "Se esperaba que multiplicar_por_diez(-10) retornara -100"

test_multiplicar_diez_por_cero()
test_multiplicar_diez_por_un_millon()
test_multiplicar_diez_por_numero_negativo()



# Ejecutador de pruebas
## unittest es el estándar de Python
### 1. se crea una clase donde cada método es una prueba
### 2. se usan los métodos assert que vienen con el módulo

### convirtiendo el ejemplo anterior a unittest
import unittest # importar unittest

class TestMultiplicarPorDiez(unittest.TestCase): # crear clase que hereda de la clase TestCase
    def test_multiplicar_diez_por_cero(self): # convertir funciones en métodos
        # cambiar assert por el método assertEqual de la clase TestCase
        self.assertEqual(multiplicar_por_diez(0), 0, "Se esperaba que multiplicar_por_diez(0) retornara 0")

    def test_multiplicar_diez_por_un_millon(self):
        self.assertEqual(multiplicar_por_diez(1000000), 10000000, "Se esperaba que multiplicar_por_diez(1000000) retornara 10000000")

    def test_multiplicar_diez_por_numero_negativo(self):
        self.assertEqual(multiplicar_por_diez(-10), -100, "Se esperaba que multiplicar_por_diez(-10) retornara -100")

unittest.main() # cómando para ejecutar las pruebas   

## se puede crear un archivo con todas las pruebas o una carpeta donde cada archivo está testeando una funcionalidad diferente

## el proceso para crear pruebas es:
### 1. pensar en los datos de entrada
### 2. ejecutar el código a testear y capturar los datos de salida
### 3. comparar los datos de entrada con los datos de salida

## tipos de aserciones de unittest
import unittest 

class TestAserciones(unittest.TestCase): 
    def test_assert_equal(self):
        self.assertEqual(2, 5) # equivale a 2 == 5

    def test_assert_in(self):
        self.assertIn(5, [1, 2, 3]) # equivale a 5 in [1, 2, 3]

    def test_assert_true(self):
        self.assertTrue(0) # equivale a 0 == True

    def test_assert_less(self):
        self.assertLess(2, 5) # equivale a 2 < 5

    def test_assert_almost_equal(self):
        self.assertAlmostEqual(0.22, 0.225) # equivale a round(0.22 - 0.225, 7) == 0

    def test_assert_raises(self):
        sumar_numeros = SumarNumeros()
        self.assertRaises(Exception, sumar_numeros.sumar, 2, 3)


class SumarNumeros:
    def sumar(self, a, b):
        return a + b

unittest.main()   

                                                                  # nombre del módulo      
## se pueden ejecutar las pruebas con el cómando 'python -m unittest test'
### ejecutar todas las pruebas del proyecto 'python -m unittest discover'


## entender el resultado de la prueba
### 1. F si fallo y . si paso
### 2. el nombre del método testeado
### 3. el nombre del test
### 4. la línea que causo el fallo del test
### 5. detalles de la aserción con el resultado esperado y el real



# Configuraciones avanzadas
## parametrización de pruebas
### se usa un objeto llamado subTest que permite generar un nuevo test por cada iteración en un for loop
import unittest

class TestMultiplicarPorDiez(unittest.TestCase):
    def test_parametrizacion(self):
        for num in [0, 1000000, -10]:
            with self.subTest():
                resultado_esperado = num * 10
                mensaje = "Se esperaba que multiplizar_por_diez(" + str(num) + ") retornara " + str(resultado_esperado)
                self.assertEqual(multiplicar_por_diez(num), resultado_esperado, mensaje)

unittest.main() 

## Preparativos de pruebas
### permite aislar nuestras pruebas
import unittest

class Calculadora:
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
        self.estado = False

    def encender_calculadora(self):
        print("Encendiendo calculadora")
        self.estado = True

    def apagar_calculadora(self):
        print("Apagando calculadora")
        self.estado = False
    
    def suma(self):
        return self.a + self.b
    
    def resta(self):
        return self.a - self.b
    
class TestCalculadora(unittest.TestCase):

    def setUp(self): # se crea un método setup con todos los preparativos, se ejecuta cada vez que se realice una prueba
        self.calculadora = Calculadora(2, 5)
        self.calculadora.encender_calculadora()

    def tearDown(self):  # limpieza cada vez que se ejecuta una prueba
        self.calculadora.apagar_calculadora()
        del self.calculadora

    def test_suma(self):
        resultado = self.calculadora.suma()
        self.assertEqual(resultado, 7)

    def test_resta(self):
        resultado = self.calculadora.resta()
        self.assertEqual(resultado, -3)

unittest.main()


### preparativos que se ejecutan una vez
import unittest

class Calculadora:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.estado = False

    def encender_calculadora(self):
        print("Encendiendo calculadora")
        self.estado = True

    def apagar_calculadora(self):
        print("Apagando calculadora")
        self.estado = False

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

class TestCalculadora(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.calculadora = Calculadora(2, 5)
        cls.calculadora.encender_calculadora()

    @classmethod
    def tearDownClass(cls):
        cls.calculadora.apagar_calculadora()
        del cls.calculadora

    def test_suma(self):
        resultado = self.calculadora.suma()
        self.assertEqual(resultado, 7)

    def test_resta(self):
        resultado = self.calculadora.resta()
        self.assertEqual(resultado, -3)

unittest.main()



### ejemplo
import unittest

class Usuario:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def es_correo_valido(self):
        return "@" in self.correo and "." in self.correo
    

class TestUsuario(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        usuario1 = Usuario("Juan", 25, "juan@example.com")
        usuario2 = Usuario("María", 17, "maria@example.com")

        self.assertEqual(usuario1.es_mayor_de_edad())
        self.assertFalse(usuario2.es_mayor_de_edad())

    def test_es_correo_valido(self):
        usuario1 = Usuario("Juan", 25, "juan@example.com")
        usuario2 = Usuario("María", 30, "maria@example")

        self.assertTrue(usuario1.es_correo_valido())
        self.assertFalse(usuario2.es_correo_valido())

unittest.main()