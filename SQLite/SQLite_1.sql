--  NULL, INTEGER: 8BYTES,  REAL:FLOAT, TEXT, BLOB:datos binarios, NUMERIC, DATE, BOOLEAN

-- CREATE TABLE user(id INT PRIMARY KEY, name TEXT, prise REAL, img BLOB);
-- INSERT INTO user(id, name)  VALUES (1, "Luke");

-- ctrl shif q :EJECUTA

--click derecho sobre la db editor sql, open sql console

--Crear tabla
CREATE TABLE personas (
	ID INTEGER PRIMARY KEY NOT NULL,
	nombre TEXT,
	direccion TEXT,
	edad INT
);

--Insertar datos
INSERT INTO personas(ID, nombre, direccion, edad)
VALUES (1,'Juan', 'Calle Principal 123', 15);

--Puedo omitir la PK ya q es secuencial
INSERT INTO personas(nombre, direccion, edad)
VALUES ('Pepe', 'Casa sobre la colina', 20);

--Bulk INSERT 
INSERT INTO personas(nombre, direccion, edad)
VALUES
	('Maria', 'Avenida Central 456', 30),
	('Pedro', 'Calle Secundaria 789', 8),
	('Juan', 'Avenida Terciaria', 10),
	('Cristina', 'Calle Colombia 11', 29);

--ALTER TABLE personas 
--ADD COLUMN edad INT;


--Leer datos
--SELECT columna1, columna2, ...
--FROM nombre_tabla
--SELECT *
SELECT nombre
FROM personas;
--leer datos unicos
SELECT DISTINCT nombre --distinct aplica para las columnas que yo solicite
FROM personas;

--Filtrado de datos
--SELECT columna1, columna2, ...ABORT
--FROM nombre_tabla
--WHERE condicion; (= < > <= >= !=) (AND OR)
SELECT *
FROM personas
WHERE edad >= 18;

SELECT DISTINCT nombre --dame los nombres de todos los usuarios mayores de 18
FROM personas
WHERE edad >= 18;

SELECT DISTINCT nombre, direccion --dame los nombres y la direccion de todos los usuarios mayores de 18
FROM personas
WHERE edad >= 18;

--Filtrado con multiples condiciones
SELECT DISTINCT nombre --nombres entre >= 20 y < 30
FROM personas
WHERE edad >= 20 AND edad < 30;

SELECT DISTINCT nombre --otra forma de escribir el query >= 20 y < 30
FROM personas
WHERE edad BETWEEN 20 AND 29;--between especifico entre numeros


--Otro ejemplo
CREATE TABLE agents (
	'agent_code' TEXT NOT NULL PRIMARY KEY,
	'agent_name' TEXT,
	'workin_area' TEXT,
	'commision' INT,
	'phone_no' TEXT,
	'country' TEXT
);
INSERT INTO agents VALUES('A007','Ramasonder','Bangalore', '0.15','1123.213121', 'Bolivia'); 
INSERT INTO agents VALUES('A003','Alex','London', '0.13','0023.213255', 'Peru'); 
INSERT INTO agents VALUES('A008','Alford','New York', '0.12','0599.213121', 'Chile'); 
INSERT INTO agents VALUES('A011','Ravi Kumar','Chennai', '0.15','4563.2871', 'Canada'); 
INSERT INTO agents VALUES('A010','Santakumar','Bangalore', '0.14','0123.9874', 'USA'); 
INSERT INTO agents VALUES('A005','Lucia','San José', '0.12','0323.213121', 'Colombia'); 
INSERT INTO agents VALUES('A001','Anderson','Brisban', '0.13','0983.213121', 'Ecuador'); 
INSERT INTO agents VALUES('A002','Subbarao','Mumbai', '0.14','0113.213121', 'Bolivia'); 
INSERT INTO agents VALUES('A006','Mukesh','Torento', '0.11','2223.213121', 'Colombia'); 
INSERT INTO agents VALUES('A004','McDen','Bangalore', '0.15','3323.213121', 'USA'); 
INSERT INTO agents VALUES('A009','Ivan','London', '0.15','4423.213121', 'Chile'); 
INSERT INTO agents VALUES('A012','Benjamin','Bogota', '0.11','5523.213121', 'Mexico'); 