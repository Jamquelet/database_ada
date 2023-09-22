
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

select c.name
from students s
join inscriptions i on s.id = i.id_student
join course c on c.id = i.id_course
where s.name = 'Maria' and approved = false;


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

----------------------------------------------------------------
--multiples joins

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

SELECT c.nombre, p.nombre, v.monto, v.fecha
FROM Clientes c
JOIN Venta v ON c.id = v.id_cliente
JOIN Productos p ON v.id_producto = p.id
WHERE c.nombre = 'Juan Pérez';

/* La cláusula SELECT indica que queremos seleccionar el nombre de los productos.
En la cláusula FROM, especificamos las tablas que vamos a utilizar: "Clientes" (c), "Venta" (v) y "Productos" (p).
La cláusula JOIN se utiliza para unir las tablas basándonos en las relaciones establecidas por las claves primarias y foráneas. Unimos la tabla "Clientes" con la tabla "Venta" mediante la condición c.id = v.id_cliente, y luego unimos la tabla "Venta" con la tabla "Productos" mediante la condición v.id_producto = p.id.
La cláusula WHERE se utiliza para filtrar los resultados y especificamos que solo queremos los productos comprados por el cliente con nombre "Juan Pérez". */


----------------------------------------------------------------


create table Clientes (
id serial primary key,
nombre varchar(50)
);
insert into Clientes (id, nombre) values 
(1,	'Juan Pérez'),
(2,	'María López'),
(3,	'Carlos Gómez'),
(4,	'Laura Ramírez'),
(5,	'Andrés Torres');

create table Productos (
  id serial primary key,
  nombre varchar(50)
);

insert into Productos (id,	nombre) values
(1,	'Camisa'),
(2,	'Pantalón'),
(3,	'Zapatos'),
(4, 'Bolso'),
(5, 'Reloj'),
(6, 'Bufanda');

create table Venta (
  id serial primary key,
  id_cliente integer,
  id_producto integer,
  monto integer,
  date timestamp,
  constraint fk_cliente foreign key (id_cliente) references Clientes(id);
  constraint fk_producto foreign key (id_producto) references Productos(id);
);

insert into Venta (id,	id_cliente,	id_producto,	monto,	date) values
(1,	1,	3,	50.00,	'2023-06-01 10:15'),
(2,	2,	2,	35.50,	'2023-06-02 14:20'),
(3,	3	,1,	20.00,	'2023-06-03 12:45'),
4,	4,	5,	80.00,	'2023-06-04 16:30'),
5	,5,	4,	45.50,	'2023-06-05 09:10'),
6,	1,	6,	15.00,	'2023-06-06 11:25'),
7,	2, 3,	50.00,	'2023-06-07 13:40'),
8,	3,	4,	40.00,	'2023-06-08 15:55'),
9,	4,	1	,25.00,	'2023-06-09 17:00'),
10,	5,	2,	30.50,	'2023-06-10 08:45'),
11,	1,	5	,70.00,	'2023-06-11 10:20'),
12,	2,	6	,18.00,	'2023-06-11 12:35'),
13,	3,	3	,45.00,	'2023-06-11 14:50'),
14,	4,	4	,60.00,	'2023-06-11 17:05'),
15,	5,	1	,22.50,	'2023-06-11 19:30'); 


