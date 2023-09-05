--declaracion, clausula,sentencia

--relación One to One (Uno a Uno): un registro de una tabla se relaciona directamente con un único registro en otra tabla
CREATE TABLE vehículo (
  id_vehículo SERIAL PRIMARY KEY,
  marca VARCHAR(50),
  modelo VARCHAR(50),
  id_motor_eléctrico INTEGER REFERENCES motor_electrico(id_motor_eléctrico),--()la llave primaria o las llaves primarias si es una llave primaria compuesta 
  id_motor_gasolina INTEGER REFERENCES motor_gasolina(id_motor_gasolina)
);

CREATE TABLE motor_eléctrico (
  id_motor_eléctrico SERIAL PRIMARY KEY,
  potencia VARCHAR(20)
);

CREATE TABLE motor_gasolina (
  id_motor_gasolina SERIAL PRIMARY KEY,
  cilindrada VARCHAR(20)
);

----------------------------------------------------------------

--relación One to Many (Uno a Muchos) es un tipo de relación donde un registro de una tabla se relaciona con varios registros en otra tabla.

CREATE TABLE usuario (
  id_usuario SERIAL PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50)
);

CREATE TABLE posts (
  id_post SERIAL PRIMARY KEY,
  id_usuario INTEGER, --clave externa
  texto TEXT,
  fecha_publicacion DATE,
  CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

/* La declaración CONSTRAINT fk_usuario define el nombre de la restricción de clave externa (puede tener cualquier nombre descriptivo). La cláusula FOREIGN KEY (id_usuario) indica que id_usuario es la columna de clave externa en la tabla posts que se relacionará con la columna id_usuario en la tabla usuario. la cláusula REFERENCES usuario(id_usuario) establece la tabla y columna de referencia para la clave externa. */


insert into usuario(id,nombre,apellido)
VALUES(1,'juan','perez'),(2,'Marias','lopez'),(3,'Carlos','Gomez');
insert into posts(id, id_usuario, texto, fecha_publicacion) values (1,	1,	'¡Hola a todos!', 2023-05-01),
(2,	1,	'¡Feliz día!',	2023-05-03),
(3,	2,	'Compartiendo una foto',	2023-05-05),
(4,	3,	'Nuevo artículo publicado',	2023-05-07),
(5,	1,	'¡Me encanta esta red social!',	2023-05-10);

--drop table posts;
--no deja eliminar por la restricion
delete from usuario where id = 1;
--tocaria que el constraint sea: set null,set default, restrict, no action,cascade
CREATE TABLE posts (
  id_post SERIAL PRIMARY KEY,
  id_usuario INTEGER, --clave externa
  texto TEXT,
  fecha_publicacion DATE,
  CONSTRAINT fk_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario) on delete set null;--a menos q la columna sea not null
);
--cascade: se borran todos los post tambien no queda nada de ese user


----------------------------------------------------------------

--Many-to-Many (muchos a muchos):asociación entre dos entidades, donde una entidad puede estar relacionada con múltiples instancias de la otra entidad y viceversa.
--Un estudiante puede inscribirse en múltiples cursos, y un curso puede tener varios estudiantes matriculados
--en una base de datos, se utiliza una tabla intermedia, a menudo llamada "tabla de enlace" o "tabla de intersección". Esta tabla actúa como un puente entre las dos entidades, y contiene las claves primarias (IDs) de los registros de las entidades relacionadas.
/* 
Tabla "Estudiantes":
- ID (clave primaria)
- Nombre
- Otros atributos del estudiante

Tabla "Cursos":
- ID (clave primaria)
- Nombre
- Otros atributos del curso

Tabla "Inscripciones":
- ID_Estudiante (clave foránea referenciando a la tabla "Estudiantes")
- ID_Curso (clave foránea referenciando a la tabla "Cursos")
- Otros atributos relacionados con la inscripción
 */

create table if not exist students (
  id serial primary key,
  name varchar(50)--varchar nombres peq, text codigo,mucho contenido
 );

 create table if not exist course (
  id serial primary key,
  nombre varchar(50)
 );

 create table if not exist inscription (
  id_student integer,
  id_course integer
 );

 ----------------------------------------------------------------

alter table inscription add column id serial primary key;

alter table inscription add column approved boolean;

alter table inscription add constraint ut_student_course unique(id_student, id_course);

alter table inscription add constraint fk_student foreign key (id_student) references students(id);

alter table inscription add constraint fk_course foreign key (id_course) references course(id); 

----------------------------------------------------------------

alter table students add column age integer;

insert into students (id, name, age) values
(1,'Juan', 20),
(2,'Maria', 22),
(3,'Carlos', 21);

insert into course (id, name) values
(1, 'mathematics'),
(2, 'history'),
(3, 'science');

insert into inscription () values 
(1,1,1, true),
(2,1,2, false),
(3,2,1, false),
(4,2,3 true),
(5,3,2 false);

--Multiples joins


