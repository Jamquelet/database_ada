""" Parte 7: CRUD con ORM
Para realizar la siguiente tarea primero necesitarás crear el mapeo de las tablas a Tortoise

La tarea consiste en crear un CRUD por terminal

Ejecutar el programa en un while infinito
Listar las tablas con un número al lado (Para que el usuario seleccione con cuál operar)
Listar las operaciones (crear, listar, obtener, eliminar)
Dada una selección
Crear: leer los datos por terminal campo por campo y al final insertar a la db
Listar: mostrar todas las filas de la tabla
Obtener: filtrar por id
Eliminar: filtrar por id
Con esto creas una interfáz básica para poder crear datos mediante terminal, imagina que desplegaras este sistema para que los usuarios vayan registrando la información terminarías con una base de datos similar a la que te dimos aquí, a partir de estos datos es que podemos realizar consultas analíticas!. En el siguiente curso verás cómo generar reportes a partir de datos!. """


import asyncio
from tortoise import Tortoise
from models import Categoria, Productos, Sucursales, Stocks, Clientes, Ordenes, Items

async def main():
    await Tortoise.init(
        db_url='postgres://postgres:1234567890@localhost:5432/proyecto_ORM',
        modules={'models': ['models']}, 
    )
    await Tortoise.generate_schemas()

#----------------------------------------------------------------

async def create_categoria():
    nombre = input("Ingrese el nombre de la categoría: ")
    categoria = await Categoria.create(nombre=nombre)
    print(f'Categoría creada con id: {categoria.id}')

async def list_categorias():
    categorias = await Categoria.all()
    for categoria in categorias:
        print(f'ID: {categoria.id}, Nombre: {categoria.nombre}')

async def get_categoria():
    categoria_id = int(input("Ingrese el ID de la categoría que desea obtener: "))
    categoria = await Categoria.get_or_none(id=categoria_id)
    if categoria:
        print(f'ID: {categoria.id}, Nombre: {categoria.nombre}')
    else:
        print("Categoría no encontrada")

async def delete_categoria():
    categoria_id = int(input("Ingrese el ID de la categoría que desea eliminar: "))
    categoria = await Categoria.get_or_none(id=categoria_id)
    if categoria:
        await categoria.delete()
        print("Categoría eliminada")
    else:
        print("Categoría no encontrada")

#----------------------------------------------------------------

async def create_producto():
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    categoria_id = int(input("Ingrese el ID de la categoría del producto: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))

    producto = await Productos.create(
        nombre=nombre,
        marca=marca,
        categoria_id=categoria_id,
        precio_unitario=precio_unitario
    )
    print(f'Producto creado con ID: {producto.id}')

async def list_productos():
    productos = await Productos.all()
    for producto in productos:
        print(f'ID: {producto.id}, Nombre: {producto.nombre}, Marca: {producto.marca}, Categoría ID: {producto.categoria_id}, Precio Unitario: {producto.precio_unitario}')

async def get_producto():
    producto_id = int(input("Ingrese el ID del producto que desea obtener: "))
    producto = await Productos.get_or_none(id=producto_id)
    if producto:
        print(f'ID: {producto.id}, Nombre: {producto.nombre}')
    else:
        print("Producto no encontrado")

async def delete_producto():
    producto_id = int(input("Ingrese el ID de la categoría que desea eliminar: "))
    producto = await Productos.get_or_none(id=producto_id)
    if producto:
        await producto.delete()
        print("Producto eliminado")
    else:
        print("Producto no encontrado")

#----------------------------------------------------------------


async def create_sucursal():
    nombre = input("Ingrese el nombre de la sucursal: ")
    direccion = input("Ingrese la dirección de la sucursal: ")

    sucursal = await Sucursales.create(
        nombre=nombre,
        direccion=direccion
    )
    print(f'Sucursal creada con ID: {sucursal.id}')

async def list_sucursales():
    sucursales = await Sucursales.all()
    for sucursal in sucursales:
        print(f'ID: {sucursal.id}, Nombre: {sucursal.nombre}, Dirección: {sucursal.direccion}')

async def get_sucursal():
    sucursal_id = int(input("Ingrese el ID de la sucursal que desea obtener: "))
    sucursal = await Sucursales.get_or_none(id=sucursal_id)
    if sucursal:
        print(f'ID: {sucursal.id}, Nombre: {sucursal.nombre}, Dirección: {sucursal.direccion}')
    else:
        print("Sucursal no encontrada")

async def delete_sucursal():
    sucursal_id = int(input("Ingrese el ID de la sucursal que desea eliminar: "))
    sucursal = await Sucursales.get_or_none(id=sucursal_id)
    if sucursal:
        await sucursal.delete()
        print("Sucursal eliminada")
    else:
        print("Sucursal no encontrada")


#----------------------------------------------------------------

async def create_stock():
    sucursal_id = int(input("Ingrese el ID de la sucursal: "))
    producto_id = int(input("Ingrese el ID del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))

    stock = await Stocks.create(
        sucursal_id=sucursal_id,
        producto_id=producto_id,
        cantidad=cantidad
    )
    print(f'Stock creado con ID: {stock.id}')

async def list_stocks():
    stocks = await Stocks.all()
    for stock in stocks:
        print(f'ID: {stock.id}, Sucursal ID: {stock.sucursal_id}, Producto ID: {stock.producto_id}, Cantidad: {stock.cantidad}')

async def get_stock():
    stock_id = int(input("Ingrese el ID del stock que desea obtener: "))
    stock = await Stocks.get_or_none(id=stock_id)
    if stock:
        print(f'ID: {stock.id}, Sucursal ID: {stock.sucursal_id}, Producto ID: {stock.producto_id}, Cantidad: {stock.cantidad}')
    else:
        print("Stock no encontrado")

async def delete_stock():
    stock_id = int(input("Ingrese el ID del stock que desea eliminar: "))
    stock = await Stocks.get_or_none(id=stock_id)
    if stock:
        await stock.delete()
        print("Stock eliminado")
    else:
        print("Stock no encontrado")


#----------------------------------------------------------------

async def create_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")

    cliente = await Clientes.create(
        nombre=nombre,
        telefono=telefono
    )
    print(f'Cliente creado con ID: {cliente.id}')

async def list_clientes():
    clientes = await Clientes.all()
    for cliente in clientes:
        print(f'ID: {cliente.id}, Nombre: {cliente.nombre}, Teléfono: {cliente.telefono}')

async def get_cliente():
    cliente_id = int(input("Ingrese el ID del cliente que desea obtener: "))
    cliente = await Clientes.get_or_none(id=cliente_id)
    if cliente:
        print(f'ID: {cliente.id}, Nombre: {cliente.nombre}, Teléfono: {cliente.telefono}')
    else:
        print("Cliente no encontrado")

async def delete_cliente():
    cliente_id = int(input("Ingrese el ID del cliente que desea eliminar: "))
    cliente = await Clientes.get_or_none(id=cliente_id)
    if cliente:
        await cliente.delete()
        print("Cliente eliminado")
    else:
        print("Cliente no encontrado")

#----------------------------------------------------------------

async def create_orden():
    cliente_id = int(input("Ingrese el ID del cliente: "))
    sucursal_id = int(input("Ingrese el ID de la sucursal: "))
    fecha = input("Ingrese la fecha de la orden (YYYY-MM-DD): ")
    total = int(input("Ingrese el total de la orden: "))

    orden = await Ordenes.create(
        cliente_id=cliente_id,
        sucursal_id=sucursal_id,
        fecha=fecha,
        total=total
    )
    print(f'Orden creada con ID: {orden.id}')

async def list_ordenes():
    ordenes = await Ordenes.all()
    for orden in ordenes:
        print(f'ID: {orden.id}, Cliente ID: {orden.cliente_id}, Sucursal ID: {orden.sucursal_id}, Fecha: {orden.fecha}, Total: {orden.total}')

async def get_orden():
    orden_id = int(input("Ingrese el ID de la orden que desea obtener: "))
    orden = await Ordenes.get_or_none(id=orden_id)
    if orden:
        print(f'ID: {orden.id}, Cliente ID: {orden.cliente_id}, Sucursal ID: {orden.sucursal_id}, Fecha: {orden.fecha}, Total: {orden.total}')
    else:
        print("Orden no encontrada")

async def delete_orden():
    orden_id = int(input("Ingrese el ID de la orden que desea eliminar: "))
    orden = await Ordenes.get_or_none(id=orden_id)
    if orden:
        await orden.delete()
        print("Orden eliminada")
    else:
        print("Orden no encontrada")

#----------------------------------------------------------------

async def create_item():
    orden_id = int(input("Ingrese el ID de la orden: "))
    producto_id = int(input("Ingrese el ID del producto: "))
    cantidad = int(input("Ingrese la cantidad: "))
    monto_venta = int(input("Ingrese el monto de venta: "))

    item = await Items.create(
        orden_id=orden_id,
        producto_id=producto_id,
        cantidad=cantidad,
        monto_venta=monto_venta
    )
    print(f'Item creado con ID: {item.id}')

async def list_items():
    items = await Items.all()
    for item in items:
        print(f'ID: {item.id}, Orden ID: {item.orden_id}, Producto ID: {item.producto_id}, Cantidad: {item.cantidad}, Monto Venta: {item.monto_venta}')


async def get_item():
    item_id = int(input("Ingrese el ID del item que desea obtener: "))
    item = await Items.get_or_none(id=item_id)
    if item:
        print(f'ID: {item.id}, Orden ID: {item.orden_id}, Producto ID: {item.producto_id}, Cantidad: {item.cantidad}, Monto Venta: {item.monto_venta}')
    else:
        print("Item no encontrado")

async def delete_item():
    item_id = int(input("Ingrese el ID del item que desea eliminar: "))
    item = await Items.get_or_none(id=item_id)
    if item:
        await item.delete()
        print("Item eliminado")
    else:
        print("Item no encontrado")


#----------------------------------------------------------------


async def main_menu():
    while True:
        print("\nMenú Principal:")
        print("1. Categorías")
        print("2. Productos")
        print("3. Sucursales")
        print("4. Stocks")
        print("5. Clientes")
        print("6. Ordenes")
        print("7. Items")
        print("8. Salir")
        
        choice = input("Seleccione una tabla para operar (1-8): ")
        
        if choice == '1':
            await operate_on_categoria()
        elif choice == '2':
            await operate_on_producto()
        elif choice == '3':
            await operate_on_sucursal()
        elif choice == '4':
            await operate_on_stock()
        elif choice == '5':
            await operate_on_cliente()
        elif choice == '6':
            await operate_on_orden()
        elif choice == '7':
            await operate_on_item()
        elif choice == '8':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_categoria():
    while True:
        print("\nOperaciones en Categorías:")
        print("1. Crear Categoría")
        print("2. Listar Categorías")
        print("3. Obtener Categoría por ID")
        print("4. Eliminar Categoría por ID")
        print("5. Volver al Menú Principal")
        
        choice = input("Seleccione una operación (1-5): ")
        
        if choice == '1':
            await create_categoria()
        elif choice == '2':
            await list_categorias()
        elif choice == '3':
            await get_categoria()
        elif choice == '4':
            await delete_categoria()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_producto():
    while True:
        print("\nOperaciones en Productos:")
        print("1. Crear Producto")
        print("2. Listar Productos")
        print("3. Obtener Producto por ID")
        print("4. Eliminar Producto por ID")
        print("5. Volver al Menú Principal")
        
        choice = input("Seleccione una operación (1-5): ")
        
        if choice == '1':
            await create_producto()
        elif choice == '2':
            await list_productos()
        elif choice == '3':
            await get_producto()
        elif choice == '4':
            await delete_producto()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_sucursal():
    while True:
        print("\nOperaciones en Sucursales:")
        print("1. Crear Sucursal")
        print("2. Listar Sucursales")
        print("3. Obtener Sucursal por ID")
        print("4. Eliminar Sucursal por ID")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una operación (1-5): ")

        if choice == '1':
            await create_sucursal()
        elif choice == '2':
            await list_sucursales()
        elif choice == '3':
            await get_sucursal()
        elif choice == '4':
            await delete_sucursal()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_stock():
    while True:
        print("\nOperaciones en Stocks:")
        print("1. Crear Stock")
        print("2. Listar Stocks")
        print("3. Obtener Stock por ID")
        print("4. Eliminar Stock por ID")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una operación (1-5): ")

        if choice == '1':
            await create_stock()
        elif choice == '2':
            await list_stocks()
        elif choice == '3':
            await get_stock()
        elif choice == '4':
            await delete_stock()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_cliente():
    while True:
        print("\nOperaciones en Clientes:")
        print("1. Crear Cliente")
        print("2. Listar Clientes")
        print("3. Obtener Cliente por ID")
        print("4. Eliminar Cliente por ID")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una operación (1-5): ")

        if choice == '1':
            await create_cliente()
        elif choice == '2':
            await list_clientes()
        elif choice == '3':
            await get_cliente()
        elif choice == '4':
            await delete_cliente()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_orden():
    while True:
        print("\nOperaciones en Ordenes:")
        print("1. Crear Orden")
        print("2. Listar Ordenes")
        print("3. Obtener Orden por ID")
        print("4. Eliminar Orden por ID")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una operación (1-5): ")

        if choice == '1':
            await create_orden()
        elif choice == '2':
            await list_ordenes()
        elif choice == '3':
            await get_orden()
        elif choice == '4':
            await delete_orden()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

#----------------------------------------------------------------

async def operate_on_item():
    while True:
        print("\nOperaciones en Items:")
        print("1. Crear Item")
        print("2. Listar Items")
        print("3. Obtener Item por ID")
        print("4. Eliminar Item por ID")
        print("5. Volver al Menú Principal")

        choice = input("Seleccione una operación (1-5): ")

        if choice == '1':
            await create_item()
        elif choice == '2':
            await list_items()
        elif choice == '3':
            await get_item()
        elif choice == '4':
            await delete_item()
        elif choice == '5':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(main_menu())


