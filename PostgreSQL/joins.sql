
--Joins: Cuanto tenemos múltiples tablas relacionadas y queremos realizar consultas combinando sus valores, debemos usar JOINs. combinar registros de dos o más tablas en base a una condición de relación específica

--INNER JOIN: Devuelve únicamente los registros que tienen una coincidencia en ambas tablas.
SELECT columnas
FROM tabla1
INNER JOIN tabla2 ON condición_de_relación;

--LEFT JOIN: Devuelve todos los registros de la tabla izquierda (primera tabla mencionada) y los registros coincidentes de la tabla derecha (segunda tabla mencionada). Si no hay coincidencias en la tabla derecha, los valores serán nulos
SELECT columnas
FROM tabla1
LEFT JOIN tabla2 ON condición_de_relación;

--RIGHT JOIN: Devuelve todos los registros de la tabla derecha (segunda tabla mencionada) y los registros coincidentes de la tabla izquierda (primera tabla mencionada)
SELECT columnas
FROM tabla1
RIGHT JOIN tabla2 ON condición_de_relación;

--FULL JOIN: Devuelve todos los registros de ambas tablas
SELECT columnas
FROM tabla1
FULL JOIN tabla2 ON condición_de_relación;

/* 
Tabla: estudiantes
id	nombre	edad
1	Juan	20
2	María	22
3	Carlos	21

Tabla: materias
id	nombre
1	Matemáticas
2	Historia
3	Ciencias

Tabla: inscripciones
id	id_estudiante	id_materia	aprobado
1	1	1	true
2	1	2	false
3	2	1	false
4	2	3	true
5	3	2	false
 */

--INNER JOIN para combinar las tablas "estudiantes", "inscripciones" y "materias". La consulta selecciona los nombres de los estudiantes y el nombre de las materias en las que están inscritos. La condición de relación se establece utilizando las claves externas correspondientes (id_estudiante e id_materia).
SELECT estudiantes.nombre, materias.nombre
FROM estudiantes
INNER JOIN inscripciones ON estudiantes.id = inscripciones.id_estudiante
INNER JOIN materias ON inscripciones.id_materia = materias.id; 

-- LEFT JOIN para combinar las tablas "estudiantes" e "inscripciones". La consulta selecciona el nombre de los estudiantes y el estado de aprobación. LEFT JOIN, se asegura de que se incluyan todos los estudiantes, incluso aquellos que no tienen inscripciones. Si no hay coincidencia en la tabla de inscripciones, el valor de "aprobado" será nulo.
SELECT estudiantes.nombre, inscripciones.aprobado
FROM estudiantes
LEFT JOIN inscripciones ON estudiantes.id = inscripciones.id_estudiante;

--RIGHT JOIN para combinar las tablas "estudiantes" e "inscripciones". La consulta selecciona el nombre de los estudiantes y el estado de aprobación. RIGHT JOIN, se asegura de que se incluyan todas las inscripciones, incluso aquellas que no tienen un estudiante correspondiente
SELECT estudiantes.nombre, inscripciones.aprobado
FROM estudiantes
RIGHT JOIN inscripciones ON estudiantes.id = inscripciones.id_estudiante;

--FULL JOIN para combinar las tablas "estudiantes" e "inscripciones".FULL JOIN, se asegura de que se incluyan todos los registros de ambas tablas, sin importar si hay coincidencia o no
SELECT estudiantes.nombre, inscripciones.aprobado
FROM estudiantes
FULL JOIN inscripciones ON estudiantes.id = inscripciones.id_estudiante;


--ejemplo con la tabla one to many 
--inner join
select u.id as usuario_id, u.nombre, u.apellido, p.id as post_id
from usuario u
join post p on u.id = p.id_usuario
order by u.id;

--left join
select *
from usuario u --izq
left join post p on u.id = p.id_usuario --tabla derecha
order by u.id;

--right join
select *
from usuario u --izq
right join post p on u.id = p.id_usuario --tabla derecha
order by u.id;

--full join
select *
from usuario u --izq
full join post p on u.id = p.id_usuario --tabla derecha
order by u.id;


create table persona (
    id serial primary key,
    nombre varchar(50),
    edad integer
);

drop table if not exists compras;
create table compras(}
    id serial primary key,
    id_persona integer,
    producto varchar(255),
    precio decimal
    constraint fk_persona foreign key (id_persona) references persona(id)
    );
--constraint unique ()
--constraint check ()

insert into persona(id,nombre,edad) VALUES
(1, 'Juan', 25),
(2, 'Maria', 30),
(3, 'Carlos', 35),
(4, 'Laura', 28),
(5, 'Andres', 32);

insert into compras(id, id_persona, producto, precio) VALUES
(1, 1, 'Camisa', 25.99 ),
(2, 2, 'Reloj', 45.30),
(3, 3, 'Gorra', 13.00),
(4, 4, 'Chaqueta', 79.99),
(5, 5, 'Boligrafo', 32.99),
(6, 4, 'Corbata', 42.25),
(7, 1, 'Blusa', 2.55 ),
(8, 2, 'Falda', 28.55 );

--calcular el numero de compras por persona--persona uno hizo tales compras
select id_persona, count(*) as n_compras 
from compras 
group by id_persona

--obtener tambien el nombre
select p.id, p.nombre, count(*) as n_compras 
from compras c 
join persona p on c.id_persona = p.id
group by p.id, p.nombre;

--top 3 personas con mas compras
select p.id, p.nombre, count(*) as n_compras 
from compras c 
join persona p on c.id_persona = p.id
group by p.id, p.nombre
order by n_compras desc
limit 3;

/* 
Tabla "Clientes":
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
15	5	1	22.50	2023-06-11 19:30 */

--obtener la lista de productos comprados por el cliente Juan Pérez.utilizar una consulta SQL que involucre las tablas "Clientes", "Productos" y "Venta".

SELECT p.nombre AS nombre_producto
FROM Clientes c
JOIN Venta v ON c.id = v.id_cliente
JOIN Productos p ON v.id_producto = p.id
WHERE c.nombre = 'Juan Pérez';

/* La cláusula SELECT indica que queremos seleccionar el nombre de los productos.
En la cláusula FROM, especificamos las tablas que vamos a utilizar: "Clientes" (c), "Venta" (v) y "Productos" (p).
La cláusula JOIN se utiliza para unir las tablas basándonos en las relaciones establecidas por las claves primarias y foráneas. Unimos la tabla "Clientes" con la tabla "Venta" mediante la condición c.id = v.id_cliente, y luego unimos la tabla "Venta" con la tabla "Productos" mediante la condición v.id_producto = p.id.
La cláusula WHERE se utiliza para filtrar los resultados y especificamos que solo queremos los productos comprados por el cliente con nombre "Juan Pérez". */

----------------------------------------------------------------

/* Una subconsulta, también conocida como subquery, es una consulta que se incluye dentro de otra consulta principal, se utiliza para obtener datos más específicos o realizar cálculos basados en los resultados de otra consulta. La consulta principal puede hacer referencia a los resultados de la subquery como si fueran una tabla temporal.

Las subconsultas son útiles cuando se necesita combinar información de múltiples tablas o aplicar condiciones más complejas a los datos. Se pueden utilizar en diversas cláusulas, como:

Cláusula WHERE: Para filtrar los resultados de la consulta principal según ciertas condiciones basadas en los resultados de la subquery.
Cláusula FROM: Para tratar los resultados de la subquery como una tabla temporal y unirlos con otras tablas en la consulta principal.
Cláusula SELECT: Para incluir los resultados de la subquery como una columna adicional en los resultados de la consulta principal.
Ejemplo: Supongamos que tenemos dos tablas: "Clientes" y "Pedidos". Queremos obtener el nombre de los clientes que han realizado pedidos en una fecha específica. Para hacer esto, podríamos utilizar una subconsulta de la siguiente manera: */

SELECT DISTINCT nombre
FROM Clientes
WHERE id IN (
  SELECT cliente_id
  FROM Pedidos
  WHERE fecha = '2023-06-01'
);
/* la subconsulta se encuentra dentro de la cláusula WHERE de la consulta principal. La subconsulta selecciona los cliente_id de la tabla "Pedidos" que cumplen con la condición de tener una fecha igual a '2023-06-01'. Luego, la consulta principal selecciona los nombres de los clientes de la tabla "Clientes" cuyos id están presentes en los resultados de la subconsulta. */

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