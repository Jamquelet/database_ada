""" Tabla "Clientes":

id	nombre
1	Juan Pérez
2	María López
3	Carlos Gómez
4	Laura Ramírez
5	Andrés Torres

Tabla "Productos":

id	nombre
1	Camisa
2	Pantalón
3	Zapatos
4	Bolso
5	Reloj
6	Bufanda

Tabla "Venta":

id	id_cliente	id_producto	monto	fecha_hora
1	1	3	50.00	2023-06-01 10:15
2	2	2	35.50	2023-06-02 14:20
3	3	1	20.00	2023-06-03 12:45
4	4	5	80.00	2023-06-04 16:30
5	5	4	45.50	2023-06-05 09:10
6	1	6	15.00	2023-06-06 11:25
7	2	3	50.00	2023-06-07 13:40
8	3	4	40.00	2023-06-08 15:55
9	4	1	25.00	2023-06-09 17:00
10	5	2	30.50	2023-06-10 08:45
11	1	5	70.00	2023-06-11 10:20
12	2	6	18.00	2023-06-11 12:35
13	3	3	45.00	2023-06-11 14:50
14	4	4	60.00	2023-06-11 17:05
15	5	1	22.50	2023-06-11 19:30 """

'--------------------------------------------------------'

'Creamos la DB'

from tortoise import fields, models, Tortoise, run_async


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


async def create_database():
    await Tortoise.init(
        db_url='sqlite://tienda.db',
        modules={'models': ['__main__']}
    )
    await Tortoise.generate_schemas(safe=True)

async def fill_data():
    # Rellenar la tabla Clientes
    clientes = [
        {'nombre': 'Juan Pérez'},
        {'nombre': 'María López'},
        {'nombre': 'Carlos Gómez'},
        {'nombre': 'Laura Ramírez'},
        {'nombre': 'Andrés Torres'},
    ]
    clientes = [Cliente(**cliente) for cliente in clientes]
    for cliente in clientes:
        await cliente.save()

    # Rellenar la tabla Productos
    productos = [
        {'nombre': 'Camisa'},
        {'nombre': 'Pantalón'},
        {'nombre': 'Zapatos'},
        {'nombre': 'Bolso'},
        {'nombre': 'Reloj'},
        {'nombre': 'Bufanda'},
    ]
    productos = [Producto(**producto) for producto in productos]
    for producto in productos:
        await producto.save()

    # Rellenar la tabla Venta
    ventas = [
        {'cliente': clientes[0], 'producto': productos[2], 'monto': 50.00, 'fecha_hora': '2023-06-01 10:15'},
        {'cliente': clientes[1], 'producto': productos[1], 'monto': 35.50, 'fecha_hora': '2023-06-02 14:20'},
        {'cliente': clientes[2], 'producto': productos[0], 'monto': 20.00, 'fecha_hora': '2023-06-03 12:45'},
        {'cliente': clientes[3], 'producto': productos[4], 'monto': 80.00, 'fecha_hora': '2023-06-04 16:30'},
        {'cliente': clientes[4], 'producto': productos[3], 'monto': 45.50, 'fecha_hora': '2023-06-05 09:10'},
        {'cliente': clientes[0], 'producto': productos[5], 'monto': 15.00, 'fecha_hora': '2023-06-06 11:25'},
        {'cliente': clientes[1], 'producto': productos[2], 'monto': 50.00, 'fecha_hora': '2023-06-07 13:40'},
        {'cliente': clientes[2], 'producto': productos[3], 'monto': 40.00, 'fecha_hora': '2023-06-08 15:55'},
        {'cliente': clientes[3], 'producto': productos[0], 'monto': 25.00, 'fecha_hora': '2023-06-09 17:00'},
        {'cliente': clientes[4], 'producto': productos[1], 'monto': 30.50, 'fecha_hora': '2023-06-10 08:45'},
        {'cliente': clientes[0], 'producto': productos[4], 'monto': 70.00, 'fecha_hora': '2023-06-11 10:20'},
        {'cliente': clientes[1], 'producto': productos[5], 'monto': 18.00, 'fecha_hora': '2023-06-11 12:35'},
        {'cliente': clientes[2], 'producto': productos[2], 'monto': 45.00, 'fecha_hora': '2023-06-11 14:50'},
        {'cliente': clientes[3], 'producto': productos[3], 'monto': 60.00, 'fecha_hora': '2023-06-11 17:05'},
        {'cliente': clientes[4], 'producto': productos[0], 'monto': 22.50, 'fecha_hora': '2023-06-11 19:30'},
    ]
    await Venta.bulk_create([Venta(**venta) for venta in ventas])

run_async(create_database())
run_async(fill_data())

'--------------------------------------------------------'

'Ejecutamos las consultas:'

'Número de personas distintas que compraron el producto X:'
async def get_distinct_buyers(product_name):
    count = await Venta.filter(producto__nombre=product_name).distinct().count()
    return count
"""  utilizamos filter para filtrar las ventas por el nombre del producto utilizando la relación producto__nombre. Luego, utilizamos values('cliente') para obtener los valores distintos del campo cliente y distinct().count() para contar la cantidad de valores distintos. El resultado es el número de personas distintas que compraron el producto X. """

'--------------------------------------------------------'

'Nombre del producto más vendido:'
async def get_most_sold_product():
    most_sold_product = (
        await Venta.annotate(sold_count=Count('id'))
        .group_by('producto_id')
        .order_by('-sold_count', 'producto__nombre')
        .first()
        .values("producto__nombre")
    )
    return most_sold_product['producto__nombre']
""" utilizamos annotate para agregar una anotación sold_count que cuenta la cantidad de ventas por producto utilizando la función de agregación Count. Luego, agrupamos por producto, ordenamos por la cuenta de ventas en orden descendente y el nombre de producto de forma ascendente (order_by('-sold_count', 'producto__nombre')) y utilizamos values('producto__nombre') para obtener el nombre del producto. El resultado es el nombre del producto más vendido. """

'--------------------------------------------------------'

'Persona que gastó más:'
async def get_biggest_spender():
    biggest_spender = (
        await Venta.annotate(total_spent=Sum('monto'))
        .group_by('cliente_id')
        .order_by('-total_spent')
        .first()
        .values('cliente__nombre')
    )
    return biggest_spender['cliente__nombre']
""" En esta consulta, utilizamos annotate para agregar una anotación total_spent que suma el campo monto de las ventas por cliente utilizando la función de agregación Sum. Luego, agrupamos por cliente, ordenamos por el total gastado en orden descendente (order_by('-total_spent')) y utilizamos values('cliente__nombre') para obtener el nombre del cliente. El resultado es el nombre de la persona que gastó más. """

'--------------------------------------------------------'

'Lista de productos de la persona que más gastó:'
async def get_products_of_biggest_spender():
    subquery = (
        Venta.annotate(total_spent=Sum('monto'))
        .group_by('cliente_id')
        .order_by('-total_spent')
        .first()
        .values('cliente_id')
    )
    products = (
        await Venta.filter(cliente_id=Subquery(subquery))
        .values_list('producto__nombre', flat=True)
    )
    return products
""" utilizamos una subconsulta (subquery) para obtener el ID del cliente que gastó más. Luego utilizamos la subconsulta en el filtro de la consulta principal para obtener las ventas del cliente que gastó más. .values_list retorna una lista de tuplas de los valores solicitados, pero como sólo solicitamos una colúmna, podemos usar flat=True para que nos devuelva el resultado como una lista de strings. """