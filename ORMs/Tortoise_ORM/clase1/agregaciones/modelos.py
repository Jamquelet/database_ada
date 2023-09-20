from tortoise import fields, models

class Cliente(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Cliente(id={self.id}, nombre={self.nombre})"
    
    def __repr__(self) -> str: 
        return self.__str__()

class Producto(models.Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Producto(id={self.id}, nombre={self.nombre})"
    
    def __repr__(self) -> str: 
        return self.__str__()

class Venta(models.Model):
    id = fields.IntField(pk=True)
    monto = fields.DecimalField(max_digits=10, decimal_places=2) # 10 digitos, 2 decimales
    fecha_hora = fields.DatetimeField()

    #hacer referencias, como me conecto a las otras tablas
    cliente = fields.ForeignKeyField("models.Cliente", related_name="ventas")
    producto = fields.ForeignKeyField("models.Producto", related_name="ventas")

    def __str__(self) -> str:
        return f"Venta(id={self.id}, monto={self.monto}, time={self.fecha_hora})"

    def __repr__(self) -> str: 
        return self.__str__()

