--Limitando resultados
--LIMIT y OFFSET son cláusulas que se utilizan en una consulta SQL para controlar el número de filas que se devuelven y desde qué posición se empieza a devolver en el conjunto de resultados.
--LIMIT. Permite limitar la cantidad de filas que se devuelven en el resultado de una consulta. Al especificar un número, se indica el límite máximo de filas que se desean obtener en el resultado.
SELECT * FROM tabla LIMIT 10;--Se devolverán solamente las primeras 10 filas de la tabla seleccionada.


/* OFFSET se utiliza para indicar la posición desde la cual se deben devolver las filas. Al especificar un número, se indica el desplazamiento o el número de filas que se deben saltar antes de comenzar a devolver los resultados. */
SELECT * FROM tabla OFFSET 20;--La consulta devolverá todas las filas de la tabla, pero comenzará a partir de la posición 21, omitiendo las primeras 20 filas.

--se puede controlar tanto el número de filas a devolver como la posición de inicio
SELECT * FROM tabla OFFSET 10 LIMIT 5;
