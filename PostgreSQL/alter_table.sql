--modificar una tabla que ya existe, para esto se usa la instrucción ALTER TABLE.

--Agregar una columna a una tabla
ALTER TABLE nombre_tabla ADD COLUMN nombre_columna tipo_dato;

--Modificar el tipo de datos de una columna:
ALTER TABLE nombre_tabla ALTER COLUMN nombre_columna TYPE nuevo_tipo_dato;

--Renombrar una columna:
ALTER TABLE nombre_tabla RENAME COLUMN nombre_columna TO nuevo_nombre;

--Eliminar una columna de una tabla:
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna;

--Agregar restricciones a una tabla:
ALTER TABLE nombre_tabla ADD CONSTRAINT nombre_restriccion restriccion;
--restricciones de clave primaria, restricciones de clave externa o restricciones de verificación.

--También se puede utilizar esta instrucción para realizar otras modificaciones, como agregar índices, cambiar el nombre de una tabla, cambiar el espacio de tablas, entre otros.