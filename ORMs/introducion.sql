--Un ORM (Object-Relational Mapping) es una técnica de programación que permite mapear las entidades de una base de datos relacional a objetos en un lenguaje de programación orientado a objetos.
--Actúa como una capa de abstracción entre una base de datos y una aplicación, permitiendo a los desarrolladores trabajar con objetos y clases en lugar de tablas y consultas SQL directamente.

--El propósito principal de un ORM es facilitar la comunicación y manipulación de datos entre una aplicación y una base de datos relacional.  Al utilizar un ORM, los desarrolladores pueden interactuar con los datos de la base de datos mediante operaciones en objetos y clases, lo que simplifica el proceso de persistencia y consulta de información. El ORM se encarga de traducir estas operaciones en consultas SQL que se ejecutan en la base de datos subyacente.

/* Los beneficios de utilizar un ORM son varios:

Abstracción de la base de datos: Los ORM ocultan los detalles específicos de la base de datos, permitiendo que los desarrolladores trabajen con una interfaz orientada a objetos coherente y consistente, independientemente del motor de base de datos subyacente.

Productividad: Al proporcionar una capa de abstracción, los ORM simplifican la interacción con la base de datos, reduciendo la cantidad de código repetitivo y permitiendo un desarrollo más rápido.

Mantenibilidad: Al utilizar un ORM, los cambios en la estructura de la base de datos se pueden abordar más fácilmente, ya que las modificaciones necesarias se limitan principalmente al mapeo de objetos.

Portabilidad: Los ORM suelen ser independientes de la base de datos, lo que facilita la portabilidad de la aplicación a diferentes entornos. */

--Django ORM para Python, Ruby on Rails para Ruby, SQLAlchemy para Python, entre otros. Cada ORM tiene sus propias características y ventajas, por lo que es importante seleccionar el que mejor se adapte a los requisitos y preferencias del proyecto.

----------------------------------------------------------------

/* a. ¿Qué es un ORM? : 
Una herramienta para la manipulación de bases de datos.

b. En SQLAlchemy, ¿cuál de las siguientes opciones representa una consulta utilizando SQL puro?: 
session.execute("SELECT * FROM users WHERE name = 'Jhon'").fetchone()

c. ¿Qué función de Tortoise ORM se utiliza para realizar una agregación como el promedio de un campo?: 
AVG 

d. En Tortoise ORM, ¿cómo se realiza una consulta que involucre una relación entre tablas utilizando joins?: 
await TABLE.filter(field_related_field_value = value)

e. En Tortoise ORM, ¿cuál es la forma correcta de realizar una consulta para obtener todas las ventas realizadas en una fecha específica?:
await Venta.filter(fecha_hora_date = date)
 */


----------------------------------------------------------------

/* Parte 7: CRUD con ORM
Para realizar la siguiente tarea primero necesitarás crear el mapeo de las tablas a Tortoise

La tarea consiste en crear un CRUD por terminal

Ejecutar el programa en un while infinito
Listar las tablas con un número al lado (Para que el usuario seleccione con cuál operar)
Listar las operaciones (crear, listar, obtener, eliminar)
Dada una selección
Crear: leer los datos por terminal campo por campo y al final insertar a la db
Listar: mostrar todas las filas de la tabla
Obtener: filtrar por id
Eliminar: filtrar por id
Con esto creas una interfáz básica para poder crear datos mediante terminal, imagina que desplegaras este sistema para que los usuarios vayan registrando la información terminarías con una base de datos similar a la que te dimos aquí, a partir de estos datos es que podemos realizar consultas analíticas!. En el siguiente curso verás cómo generar reportes a partir de datos!. */