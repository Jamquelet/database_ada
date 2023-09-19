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