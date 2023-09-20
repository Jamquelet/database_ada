'''Código de configuracion para inicializar Tortoise ORM y preparar la conexión a la base de datos'''


from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return f"User(id={self.id}, email={self.email})"
    
    def __repr__ (self) -> str:
        return self.__str__()