--permite aplicar otro query sobre dicha tabla temporal que resulta de un query

/* Una subconsulta, también conocida como subquery, es una consulta que se incluye dentro de otra consulta principal, se utiliza para obtener datos más específicos o realizar cálculos basados en los resultados de otra consulta. La consulta principal puede hacer referencia a los resultados de la subquery como si fueran una tabla temporal.

Las subconsultas son útiles cuando se necesita combinar información de múltiples tablas o aplicar condiciones más complejas a los datos. Se pueden utilizar en diversas cláusulas, como:

Cláusula WHERE: Para filtrar los resultados de la consulta principal según ciertas condiciones basadas en los resultados de la subquery.

Cláusula FROM: Para tratar los resultados de la subquery como una tabla temporal y unirlos con otras tablas en la consulta principal.

Cláusula SELECT: Para incluir los resultados de la subquery como una columna adicional en los resultados de la consulta principal.

Ejemplo: Supongamos que tenemos dos tablas: "Clientes" y "Pedidos". Queremos obtener el nombre de los clientes que han realizado pedidos en una fecha específica. Para hacer esto, podríamos utilizar una subconsulta de la siguiente manera: */

SELECT DISTINCT nombre
FROM Clientes
/* id del cliente este en la lista que hicieron pedidos en esta fecha. selecciono el nombre de los clientes que estan en la lista resultante del in()*/
WHERE id IN ( 
  SELECT cliente_id
  FROM Pedidos
  WHERE fecha = '2023-06-01'
);

/* la subconsulta se encuentra dentro de la cláusula WHERE de la consulta principal. La subconsulta selecciona los cliente_id de la tabla "Pedidos" que cumplen con la condición de tener una fecha igual a '2023-06-01'. Luego, la consulta principal selecciona los nombres de los clientes de la tabla "Clientes" cuyos id están presentes en los resultados de la subconsulta. */

--mismo ejemplo con join
select distinct c.nombre
from clientes c 
join pedidos p on c.id = p.id_cliente
where p.fecha = '2023-06-01';


----------------------------------------------------------------

--Agregaciones con relaciones

--Número de personas distintas que compraron el producto X:
SELECT COUNT(DISTINCT v.id_cliente) AS numero_personas
FROM Venta v
WHERE v.id_producto = X;

--Nombre del producto más vendido (ordenar por nombre también)
SELECT p.nombre AS nombre_producto
FROM Productos p
JOIN Venta v ON p.id = v.id_producto
GROUP BY p.id, p.nombre
ORDER BY COUNT(*) DESC, p.nombre ASC
LIMIT 1;
--Esta consulta se une la tabla "Productos" con la tabla "Venta" y agrupa los resultados por el ID y nombre del producto. Luego, se ordenan los resultados según la cantidad de ventas en orden descendente y se limita a un solo resultado, obteniendo así el nombre del producto más vendido.

--Persona que gastó más:
SELECT c.nombre AS nombre_persona, SUM(v.monto) AS total_gastado
FROM Clientes c
JOIN Venta v ON c.id = v.id_cliente
GROUP BY c.id, c.nombre
ORDER BY total_gastado DESC
LIMIT 1;
--une la tabla "Clientes" con la tabla "Venta" y agrupa los resultados por el ID y nombre del cliente. Luego, se calcula la suma total de los montos gastados por cada cliente y se ordenan los resultados según el total gastado en orden descendente. Finalmente, se limita a un solo resultado para obtener la persona que gastó más.

--Lista de productos de la persona que más gastó (usando subqueries):
SELECT p.nombre AS nombre_producto
FROM Productos p
JOIN Venta v ON p.id = v.id_producto
WHERE v.id_cliente = (
  SELECT v2.id_cliente
  FROM Venta v2
  GROUP BY v2.id_cliente
  ORDER BY SUM(v2.monto) DESC
  LIMIT 1
);
--Esta consulta utiliza una subconsulta para obtener el ID del cliente que gastó más. Luego, se une la tabla "Productos" con la tabla "Venta" y se filtra por el cliente obtenido en la subconsulta. Esto devolverá la lista de productos comprados por la persona que más gastó.