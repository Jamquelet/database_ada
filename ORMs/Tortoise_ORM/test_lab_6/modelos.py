from tortoise import fields, models


class Cliente(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)


class Producto(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)


class Venta(models.Model):
    id = fields.IntField(pk=True)
    cliente = fields.ForeignKeyField('models.Cliente', related_name='ventas')
    producto = fields.ForeignKeyField('models.Producto', related_name='ventas')
    monto = fields.DecimalField(max_digits=10, decimal_places=2)
    fecha_hora = fields.DatetimeField()
