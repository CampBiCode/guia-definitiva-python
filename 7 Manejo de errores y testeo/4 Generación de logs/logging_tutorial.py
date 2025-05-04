# Configurar logging
import logging
import sys # módulo para acceder a información de nuestro sistema operativo

## crear un objeto logger
logger = logging.getLogger(__name__) # se recomienda usar '__name__' esta variable almacena el nombre del módulo actual

## crear un handler
### cermite indicar donde queremos que se envien nuestros logs
stream_handler = logging.StreamHandler(sys.stdout) # enviará los logs a la terminal
### agregamos nuestro manejador de logs a nuestros objeto logger
logger.addHandler(stream_handler)

## niveles de logging
### son niveles que determinan la severidad del log, entre más alto el valor del nivel, más severo es el log
print(logging.DEBUG) # 10
print(logging.INFO) # 20
print(logging.WARNING) # 30
print(logging.ERROR) # 40
print(logging.CRITICAL) # 50
print(logging.NOTSET) # 0
### configurar el nivel de log: solo se mostrarán los logs de este nivel o niveles superiores
logger.setLevel(logging.INFO) # por defecto el nivel de los logs es WARNING



# Crear logs
## se usa el método log en el objeto logger
logger.log(logging.DEBUG, "Este mensaje es nivel DEBUG.") # no se muestra
logger.log(logging.INFO, "Este es un mensaje informativo.")

## enviar logs a un archivo
file_handler = logging.FileHandler("programa.log")
logger.addHandler(file_handler)

logger.log(logging.INFO, "Este es un mensaje informativo.")

## ejemplo del uso de logs
import logging
import sys

logger = logging.getLogger(__name__) 

stream_handler = logging.StreamHandler(sys.stdout) 
formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(lineno)d:%(message)s")
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

def procesar_pedido(pedido):
    try:
        if pedido["id"] > 1234:
            raise Exception("El pedido no cuenta con un id valido")

        logger.log(logging.INFO, f"Iniciando procesamiento del pedido {pedido['id']}")
        logger.log(logging.INFO, f"Pedido {pedido['id']} procesado con éxito")
        enviar_correo_confirmacion(pedido)
    except Exception as e:
        logger.log(logging.ERROR, f"Error al procesar el pedido {pedido['id']}: {str(e)}")

def enviar_correo_confirmacion(pedido):
    try:
        logger.log(logging.INFO, f"Enviando correo de confirmación para el pedido {pedido['id']}")
        logger.log(logging.INFO, f"Correo de confirmación enviado para el pedido {pedido['id']}")
    except Exception as e:
        logger.log(logging.ERROR, f"Error al enviar correo de confirmación para el pedido {pedido['id']}: {str(e)}")

pedido_ejemplo = {"id": 1234, "cliente": "Ejemplo Cliente", "productos": ["Producto 1", "Producto 2"]}
procesar_pedido(pedido_ejemplo)



# Formato de logs
## se puede incluir información relevante como:
### secha y horal log
### nombre del módulo
### número de la linea
formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(lineno)d:%(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

nombre = "santiago"
logger.log(logging.INFO, f"Este es un mensaje informativo (variable={nombre}).")