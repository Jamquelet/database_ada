create table if not exist ventas(
    producto VARCHAR(255) primary key not null,
    cantidad INTEGER,
    precio DECIMAL
);

insert into ventas (producto, cantidad, precio)
VALUES
('producto 1', 5, 10.50),
('producto 2', 8, 15.75),
('producto 3', 3, 20.00),
('producto 4', 12, 3.50),
('producto 5', 6, 12.25),
('producto 6', 10, 18.50),
('producto 7', 4, 14.00),
('producto 8', 7, 11.80),
('producto 9', 9, 16.90);

drop table ventas; --elimina tablas y vistas de una base de datos

select * from ventas
offset 2 limit 3;

select * from ventas
--ordenas por la cantidad de productos
ORDER BY cantidad desc;

--agregaciones: datos que resuman cierta estructura, SUM,AVG,MAX,MIN,COUNT, COUNT DISTINCT

select SUM(cantidad) as 'TotalVentas' --se utilizan comillas para que respete el nombre, sin ellas que en minuscula
from ventas; 

----------------------------------------------------------------

select producto, SUM(cantidad) as total_ventas
from ventas
group by producto; --si esta duplicado suma todas las entradas producto 2, 5; producto 2, 10; solo muestra un producto 2, 15

select producto,  fecha, SUM(cantidad) as total_ventas
from ventas
group by producto, fecha; --total ventas por producto y fecha

select producto, AVG(cantidad) as promedio_ventas
from ventas
group by producto;

select producto, MAX(cantidad) as max_ventas, MIN(cantidad) as min_ventas
from ventas
group by producto;

----------------------------------------------------------------
--filtrado luego de una agregaccion

select producto, MAX(cantidad) as max_ventas, MIN(cantidad) as min_ventas
from ventas
group by producto
having MIN(cantidad) > 3;--productos numero de ventas mayor igual a dos

select producto, SUM(cantidad) as total_ventas
from ventas
group by producto
having SUM(cantidad) > 100;

----------------------------------------------------------------

--orden de ejecucion de operaciones
SELECT DISTINCT  --6 --7 distinc eliminar instancias repetidas
  columna, AGG_FUNC(columna_o_expression), ...
FROM
  tabla T JOIN otra_tabla O ON T.columna = O.column  --1 --2 join
WHERE --3
  condición
GROUP BY --4
  columna
HAVING --5
  condición
ORDER BY --8
  columna ASC/DESC
LIMIT n OFFSET m; --9