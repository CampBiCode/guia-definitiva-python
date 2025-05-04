# Opción 1
from utils import crear_cuenta

usuario = crear_cuenta("thom", 22, 123444, 50000)
print(usuario)



# Opción 2
import utils.usuario.crear

usuario = utils.usuario.crear.crear_cuenta("thom", 22, 123444, 50000)
print(usuario)



# Ejemplos
from utils.usuario.crear import crear_cuenta
from utils.usuario.editar import editar_cuenta

from utils.tarjetas.crear import crear_tarjeta
from utils.tarjetas.editar import editar_tarjeta

