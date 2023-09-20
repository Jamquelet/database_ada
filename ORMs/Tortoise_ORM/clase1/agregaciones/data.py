from modelos import *

async def fill_data():
    #rellenar la tabla Clientes
    clientes = [
        {'nombre': 'Juan'},
        {'nombre': 'Maria Lopez'},
        {'nombre': 'Carlos Juan'},
        {'nombre': 'Laura Ramirez'},
        {'nombre': 'Andres Torres'},
    ]
    clientes = [Cliente(**cliente) for cliente in clientes]
    for cliente in clientes:
        await cliente.save()

    #rellenar la tabla productos
    productos = [
        {'nombre': 'Camisa'},
        {'nombre': 'Pantalon'},
        {'nombre': 'Zapatos'},
        {'nombre': 'Bolso'},
        {'nombre': 'Reloj'},
        {'nombre': 'Bufanda'},
    ]
    productos = [Producto(**producto) for producto in productos]
    for producto in productos:
        await producto.save()

    #rellenar la tabla venta
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