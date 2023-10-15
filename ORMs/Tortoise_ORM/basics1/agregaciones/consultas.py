#Crear nueva base de datos agregaciones
from tortoise import Tortoise, run_async
from tortoise.functions import Count
from modelos import Cliente, Producto, Venta
from data import fill_data


async def main():
    await Tortoise.init(
        db_url='postgres://username:password@localhost:5432/database',
        modules={'models': ['modelos']},
    )
    await Tortoise.generate_schemas(safe=True)
    
    #await fill_data()

    """ v = await Venta.get_or_none(id=1)
    print(v)#Venta(id=1, monto=50.00, time=2023-06-01 10:15:00:00)
    print(await v.cliente) #Cliente(id=1, nombre= Juan Perez). me da el objeto cliente """

    """ c = await Cliente.get_or_none(nombre="Juan Perez")
    print(await c.ventas) #Veo las ventas de ese cliente """

    #numero de personas distintas que compraron el producto x
    #sql: select distinc count(*) as n_ventas from venta where producto_id = x
    count = await Venta.filter(producto__id=4).distinct().count() #
    print(count)#3 #3 ventas con el producto 4

    #si quiero filtar por el nombre en sql tendria q
    #select distinc count(*) as n_ventas from venta v join producto p on v.producto_id = p.id where p.nombre = 'Bolso'
    count = await Venta.filter(producto__nombre='Bolso').distinct().count() #retorna 3

    #nombre del producto mas vendido
    most_sold = (await Venta.annotate(conteo_vendidos=Count("id")).group_by("producto_id", "producto__nombre").order_by("-conteo_vendidos").limit(1).values("producto_nombre")) #annotate es como un as alias, - ordena de mayor a menor
    print(most_sold["producto__nombre"])#devuelve bolso


run_async(main())


#como sacar datos relacionados en sql: join
