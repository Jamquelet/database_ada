
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
