from utils.clase import Clase
from utils.estudiante import Estudiante
from utils.profesor import Profesor, ProfesorIntercambio, Idioma
from utils.acudiente import AcudienteDiario, AcudienteSemanal, AcudienteMensual


profesor1 = ProfesorIntercambio("Thom", "Languages", "United Kingdom", [Idioma.ESPAÑOL, Idioma.INGLES])

acudiente1 = AcudienteSemanal("Steve", 220000)
acudiente2 = AcudienteDiario("Harry", 22000)

estudiante1 = Estudiante("George", 15, acudiente1)
estudiante2 = Estudiante("Timmy", 14, acudiente2)

clase_ingles = Clase("Inglés", 5, 10, profesor1)
clase_ingles.asociar_estudiante(estudiante1)
clase_ingles.asociar_estudiante(estudiante2)

estudiante1.agregar_nota(100)
estudiante1.agregar_nota(80)
estudiante2.agregar_nota(70)
estudiante2.agregar_nota(60)

estudiante1.generar_promedio_notas()
estudiante2.generar_promedio_notas()

profesor1.especialidad = "Dancing"
print(profesor1)

clase_ingles.mostrar_estudiantes()
clase_ingles.generar_promedio_notas()

