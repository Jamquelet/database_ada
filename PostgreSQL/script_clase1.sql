create table usuarios(
    id serial PRIMARY KEY, 
    nombre VARCHAR(50),
    edad INTEGER
);

INSERT INTO usuarios (nombre, edad) VALUES('Jhon', 25);

select * from usuarios where edad = 25;

insert into usuarios (nombre, edad) values
('Ana', 28),
('Pedro', 35),
('María', 42),
('Luis', 22),
('Sofía', 19),
('Mario', 40),
('Sofloques', 200);

SELECT * FROM usuarios WHERE edad = 22;

SELECT * FROM usuarios WHERE edad != 42;

--para comparar nulos: IS NULL o IS NOT NULL

select * from usuarios where edad in (28, 35, 22);('María', 42),

select * from usuarios where nombre like '%sof%'; --contiene una subcadena

select * from usuarios where nombre like 'Mari_';

--Tabla Empleados

create table empleados (
    id serial primary key,
    nombre varchar(50),
    edad integer,
    salario integer
);

insert into empleados (id,nombre,edad,salario) values 
(1, 'Juan', 30, 30000),
(2, 'Maria', 25, 25000),
(3, 'Pedro', 40, 40000),
(4, 'Laura', 28, 28000),
(5, 'Andres', 35, 35000,
(6, 'Ana', 22, 22000),
(7, 'Carlos', 45, 38000),
(8, 'Sofia', 33, 35000),
(9, 'Miguel', 27, 27000),
(10, 'Valentina', 29, 29000);

select nombre from empleados where edad 

update empleados
set salario = salar