from tortoise.functions import Count, Sum, Avg
from modelos import Cliente, Venta, Producto

from pypika import CustomFunction
from tortoise.expressions import Function

class TruncDate(Function):
    database_func = CustomFunction("DATE", ["name"])

#Número total de compras realizadas por cada cliente (Retornar como tuplas (nombre,n_compras))
    """
    select c.nombre, count(v.id) as n_compras
    from ventas v
    join clientes c on v.cliente_id = c.id
    group by c.nombre, v.cliente_id
    """
async def solucion_1():
    # Implementa tu solución aquí
    res = await (
        Venta.annotate(n_compras=Count("id"))
    
    .group_by("cliente_id")
    .values_list("cliente__nombre", "n_compras"))
    return res
    
    raise NotImplementedError()

#Monto total de ventas por producto, ordenado de mayor a menor (Retornar como tuplas (nombre, monto))
    """
    select p.nombre, SUM(v.monto) as monto
    from ventas v
    join productos p on v.producto_id = p.id
    group by p.nombre, v.producto_id
    """
async def solucion_2():
    # Implementa tu solución aquí
    res = await (
        Venta.annotate(monto=Sum("monto")).group_by("producto_id").values_list("producto__nombre", "monto")
    )
    return res
    raise NotImplementedError()

#Promedio de montos de ventas por día ordenado por fechas
    """
    select DATE(fecha_hora) as  fecha, AVG(monto) as promedio
    from ventas
    group by DATE(fecha_hora)
    order by fecha DESC
    """
async def solucion_3():
    # Implementa tu solución aquí
    # No olvides usar la función custom de la descripción
    res = await (
        Venta.annotate(fecha=TruncDate("fecha_hora"),promedio=Avg("monto")).group_by("fecha").order_by("fecha").values("fecha", "promedio")
    )
    return [
        (e["fecha"], float(e["promedio"]))
        for e in res
    ]
    raise NotImplementedError()
