from tortoise import fields
from tortoise.models import Model

class Categoria(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Categoria(id={self.id}, nombre={self.nombre})"
    
    def __repr__(self) -> str:
        return self.__str__()

class Productos(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    marca = fields.CharField(max_length=255)
    categoria_id = fields.ForeignKeyField("models.Categoria")
    precio_unitario = fields.DecimalField(max_digits=10, decimal_places=2)

class Sucursales(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    direccion = fields.CharField(max_length=255)

class Stocks(Model):
    id = fields.IntField(pk=True)
    sucursal_id = fields.ForeignKeyField("models.Sucursales")
    producto_id = fields.ForeignKeyField("models.Productos")
    cantidad = fields.IntField()
    
class Clientes(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)
    telefono = fields.CharField(max_length=50)

class Ordenes(Model):
    id = fields.IntField(pk=True)
    cliente_id = fields.ForeignKeyField("models.Clientes")
    sucursal_id = fields.ForeignKeyField("models.Sucursales")
    fecha = fields.DateField()
    total = fields.IntField()

class Items(Model):
    id = fields.IntField(pk=True)
    orden_id = fields.ForeignKeyField("models.Ordenes")
    producto_id = fields.ForeignKeyField("models.Productos")
    cantidad = fields.IntField()
    monto_venta = fields.DecimalField(max_digits=10, decimal_places=2)

