create table if not exists Clientes (
	id serial primary key,
	nombre varchar(50),
	direccion varchar(50),
	email varchar(50)
);

create table if not exists Productos (
	id serial primary key,
	nombre varchar(50),
	descripcion varchar(50),
	precio decimal(10,2)
);

create table if not exists Ordenes (
	id serial primary key,
	cliente_id integer,
	producto_id integer,
	fecha timestamp,
	total decimal(10,2),
	constraint fk_cliente foreign key (cliente_id) references Clientes(id),
	constraint fk_producto foreign key (producto_id) references Productos(id)
);

create table if not exists Opiniones(
	id serial primary key,
	producto_id integer,
	cliente_id integer,
	opinion varchar(50),
	constraint fk_producto foreign key (producto_id) references Productos(id),
	constraint fk_cliente foreign key (cliente_id) references Clientes(id)
);

----------------------------------------------------------------

insert into Clientes(id, nombre,direccion, email) values 
(1, 'Juan Perez', 'Calle 123, Ciudad A', 'juan.perez@example.com'),
(2,	'Maria Lopez',	'Av. Principal, Ciudad B',	'maria.lopez@example.com'),
(3,	'Carlos Ramirez',	'Calle 456, Ciudad C',	'carlos.ramirez@example.com');

insert into Productos(id, nombre, descripcion, precio) values 
(1,	'Camiseta',	'Camiseta de algodon',	19.99),
(2,	'Pantalon',	'Pantalon de mezclilla', 39.99),
(3,	'Zapatos',	'Zapatos de cuero',	59.99);

insert into Ordenes(id, cliente_id, producto_id, fecha, total) values 
(1,	1,	2,	'2023-06-01 09:00:00',	39.99),
(2,	2,	1,	'2023-06-02 15:30:00',	19.99),
(3,	3,	3,	'2023-06-03 11:45:00',	59.99);

insert into Opiniones(id, producto_id, cliente_id, opinion) values
(1,	1,	2,	'Me encanta esta camiseta'),
(2,	2,	1,	'Los pantalones son geniales'),
(3,	3,	3,	'Los zapatos son muy comodos');

----------------------------------------------------------------

--Obtener el nombre del cliente, nombre del producto y fecha de todas las órdenes realizadas
select c.nombre as nombre_del_cliente, p.nombre as nombre_del_producto, o.fecha 
from ordenes o 
join clientes c on o.cliente_id = c.id 
join productos p on p.id = o.producto_id 
/*  SELECT 
    C.nombre AS nombre_cliente,
    P.nombre AS nombre_producto,
    O.fecha
FROM 
    Ordenes AS O
INNER JOIN 
    Clientes AS C ON O.cliente_id = C.id
INNER JOIN 
    Productos AS P ON O.producto_id = P.id;
 */

----------------------------------------------------------------

--Calcular el total de ventas por cliente
/* select c.id as cliente_id, c.nombre as nombre_cliente, sum(o.total) as total_ventas
from clientes c 
join ordenes o on c.id = o.cliente_id 
group by c.id, c.nombre 
order by total desc;
 */
select c.nombre as nombre_cliente, sum(o.total) as total_ventas
from clientes c 
join ordenes o on c.id = o.cliente_id 
group by c.nombre 
order by total_ventas asc;
----------------------------------------------------------------

--Obtener el nombre del cliente y la cantidad de opiniones que ha realizado

select c.nombre as nombre_cliente, count(o.opinion) as nro_opiniones
from opiniones o 
join clientes c  on o.cliente_id = c.id
group by c.nombre
order by c.nombre desc;


----------------------------------------------------------------
--Obtener el nombre del producto y el número de opiniones recibidas, ordenados de forma ascendente por el número de opiniones
/* select p.nombre as nombre_producto, count(o.opinion) as nro_opiniones
from opiniones o 
join productos p on o.producto_id = p.id 
group by p.nombre 
order by opiniones_recibidas asc; */

SELECT
    P.nombre AS nombre_producto,
    COUNT(O.id) AS numero_opiniones
FROM
    Productos AS P
LEFT JOIN
    Opiniones AS O ON P.id = O.producto_id
GROUP BY
    P.id, P.nombre 
ORDER BY
    nombre_producto, numero_opiniones ASC;
/* Tabla Clientes:

id	nombre	direccion	email
1	Juan Perez	Calle 123, Ciudad A	juan.perez@example.com
2	Maria Lopez	Av. Principal, Ciudad B	maria.lopez@example.com
3	Carlos Ramirez	Calle 456, Ciudad C	carlos.ramirez@example.com
Tabla Productos:

id	nombre	descripcion	precio
1	Camiseta	Camiseta de algodon	19.99
2	Pantalon	Pantalon de mezclilla	39.99
3	Zapatos	Zapatos de cuero	59.99
Tabla Ordenes:

id	cliente_id	producto_id	fecha	total
1	1	2	2023-06-01 09:00:00	39.99
2	2	1	2023-06-02 15:30:00	19.99
3	3	3	2023-06-03 11:45:00	59.99
Tabla Opiniones:

id	producto_id	cliente_id	opinion
1	1	2	Me encanta esta camiseta
2	2	1	Los pantalones son geniales
3	3	3	Los zapatos son muy comodos
Escribe las queries (en los archivos .sql) para realizar lo siguiente:

Crear las tablas
Insertar los datos
 */