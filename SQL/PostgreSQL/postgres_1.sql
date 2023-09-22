--standard query lenguaje SQL
--postgresqltutorial.com
--Transacciones ACID = Atomicidad (Atomicity): Unidad indivisible - Consistencia (Consistency): estado valido a estado valido - Aislamiento (Isolation): transacciones no interfieren entre si - Durabilidad (Durability): cambios persistean incluso en fallas

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY, --autoincrementable PK
    nombre VARCHAR(50),
    edad INTEGER
);

INSERT INTO usuarios (nombre, edad) VALUES ('John', 25);

SELECT * FROM usuarios WHERE edad = 10;

SELECT * FROM usuarios WHERE edad != 25; --(diferente de): El operador != se utiliza en la cláusula WHERE para comparar si dos valores no son iguales --no sea igual a 25

SELECT * FROM usuarios WHERE correo IS NULL;--(es nulo): El operador IS NULL se utiliza para verificar si un valor en una columna es nulo --la consulta seleccionará todos los registros de la tabla "usuarios" donde la columna "correo" sea nula

--(Si quisieramos buscar las filas que si tienen un valor, o sea que no son nulas, se utiliza el operador IS NOT NULL)

SELECT * FROM usuarios WHERE edad IN (20, 25, 30);--comparar un valor con un conjunto de valores posibles --columna "edad" sea igual a 20, 25 o 30

SELECT * FROM usuarios WHERE edad BETWEEN 20 AND 30;--valores dentro de un rango especificado. Este operador se utiliza en combinación con el operador AND --esté dentro del rango de 20 a 30 (ambos inclusivos).

--LIKE se utiliza para comparar un valor de una columna con un patrón de texto.
--% se utiliza para representar cualquier cantidad de caracteres
--  ( _ ) representar un único carácter.

SELECT * FROM empleados WHERE nombre LIKE 'Juan%'; --Buscar registros que comiencen con un determinado prefijo: todos los empleados cuyo nombre comience con "Juan".


SELECT * FROM clientes WHERE email LIKE '%@gmail.com'; --Buscar registros que terminen con un determinado sufijo: Esta consulta seleccionará todos los clientes cuya dirección de correo electrónico termine en "@gmail.com".

SELECT * FROM productos WHERE nombre LIKE '%camiseta%';--Buscar registros que contengan una secuencia específica en cualquier posición: todos los productos cuyo nombre contenga la palabra "camiseta" en cualquier posición.

SELECT * FROM empleados WHERE nombre LIKE 'M_rtin';--Buscar registros que tengan un carácter específico en una posición determinada: Esta consulta seleccionará todos los empleados cuyo nombre comience con "M", tenga una tercera letra "r" y una cuarta letra "t", seguidas de "in".

-- ILIKE : Realiza una búsqueda de coincidencias sin tener en cuenta las diferencias de mayúsculas y minúsculas. Por ejemplo, nombre ILIKE 'juan%' seleccionará tanto "Juan" como "juan".

----------------------------------------------------------------

--Tipos de datos:  NUMERIC (para valores numéricos de precisión variable), TEXT (para cadenas de texto de longitud ilimitada) y JSON (para almacenar datos JSON).

CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INTEGER,
    salario INTEGER
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100), --VARCHAR se utiliza para almacenar cadenas de texto de longitud variable
    descripcion VARCHAR(255),
    precio NUMERIC(8, 2)
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    es_miembro BOOLEAN --almacenar valores de verdadero (true) o falso (false).
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    fecha_pedido DATE, --almacenar fechas-- año mes dia
    total NUMERIC(10, 2)--cuantos numeros antes de la coma soporta, y cuantos numeros despues de la coma soporta, el precio no va a exceder 10 numeros antes de la coma y no va a exceder 2 numeros despues de la coma
);

CREATE TABLE registros (
    id SERIAL PRIMARY KEY,
    fecha_hora TIMESTAMP, --almacenar fechas y horas exacta --unixtimestamp.com
    valor FLOAT
);

--Actualizacion de datos

UPDATE nombre_tabla --cambiar valores en una tabla, se utiliza la instrucción UPDATE, esta permite actualizar uno o más campos de uno o varios registros en función de una condición específica
SET columna1 = valor1, columna2 = valor2, ...
WHERE condicion; --Si no se proporciona ninguna condición, la actualización se aplicará a todos los registros de la tabla.

UPDATE empleados --aumentar el salario de todos los empleados mayores de 30 años en un 10%
SET salario = salario * 1.1 
WHERE edad > 30;

--Eliminacion de datos

DELETE FROM nombre_tabla --Cuando se requiere eliminar filas de una tabla dada una condición
WHERE condicion; --Si no se proporciona ninguna condición, se eliminarán todos los registros de la tabla.

DELETE FROM empleados
WHERE salario < 1000;--eliminar todos los empleados cuyo salario sea menor de 1000

--db lab 3

CREATE TABLE productos(
    id serial PRIMARY KEY,
    nombre varchar(50),
    categoria varchar(50),
    precio decimal(10,2),
    cantidad integer
);

INSERT INTO productos (id, nombre, categoria, precio, cantidad) VALUES
(1, 'Camiseta', 'Ropa', 19.99, 50),
(2, 'Zapatos', 'Calzado', 59.99, 20),
(3, 'Pantalón', 'Ropa', 29.99, 30),
(4,	'Gorra', 'Accesorios', 9.99, 100),
(5,	'Bufanda',	'Accesorios', 14.99, 40),
(6,	'Vaso',	'Hogar', 4.99,	80),
(7,	'Libreta', 'Papelería',	2.99, 120),
(8,	'Reloj', 'Accesorios', 39.99, 15),
(9,	'Juguete', 'Infantil',	12.99, 70),
(10, 'Bolso', 'Accesorios', 24.99, 25);

SELECT nombre, precio FROM productos WHERE categoria = 'Accesorios' and precio >= 20;

SELECT nombre, cantidad FROM productos WHERE cantidad <= 50;

UPDATE productos 
SET cantidad = cantidad + 10
WHERE categoria = 'Ropa';

DELETE FROM productos WHERE precio < 10;