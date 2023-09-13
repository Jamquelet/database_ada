""" Tortoise ORM es un ORM asíncrono para Python inspirado en el ORM de Django. Está diseñado específicamente para trabajar con bases de datos relacionales en entornos asíncronos. """

'instalación: pip install tortoise-orm'

'Configuración para SQLite:'
""" Para utilizar Tortoise ORM con SQLite, necesitarás tener el módulo aiosqlite instalado. Puedes instalarlo ejecutando el siguiente comando: pip install aiosqlite
Luego, crea un archivo Python (por ejemplo, main.py) y agrega el siguiente código de configuración: """

from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['main']},
    )
    await Tortoise.generate_schemas(safe=True)
    
    # A partir de aquí, puedes utilizar Tortoise ORM para interactuar con la base de datos

run_async(main())

"""  hemos definido una clase de modelo User que representa una tabla en la base de datos. Luego, utilizamos Tortoise.init() para configurar la conexión a la base de datos SQLite (db.sqlite3 en este caso) y especificamos la ubicación del archivo de base de datos en la URL. Finalmente, ejecutamos Tortoise.generate_schemas() para generar los esquemas de la base de datos basados en los modelos definidos. """

'----------------------------------------------------------------'

""" Configuración para PostgreSQL
Para utilizar Tortoise ORM con PostgreSQL, necesitarás tener el módulo asyncpg instalado. Puedes instalarlo ejecutando el siguiente comando:
pip install asyncpg """

from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

async def main():
    await Tortoise.init(
        db_url='postgres://username:password@localhost:5432/database',
        modules={'models': ['main']},
    )
    await Tortoise.generate_schemas()
    
    # A partir de aquí, puedes utilizar Tortoise ORM para interactuar con la base de datos

run_async(main())
