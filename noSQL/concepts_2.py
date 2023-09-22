""" Desnormalización

Desnormalizar datos en una base de datos distribuida puede ofrecer varios beneficios en términos de rendimiento y eficiencia de las consultas. A continuación, se presentan algunas razones por las cuales desnormalizar datos puede ser beneficioso en este contexto:

1.Reducción de la necesidad de unir tablas: En una base de datos distribuida, las consultas que involucran múltiples nodos pueden ser costosas en términos de rendimiento debido a la necesidad de realizar operaciones de unión (join) entre tablas. Al desnormalizar los datos y combinar información relacionada en una única tabla, se evita la necesidad de unir datos entre nodos diferentes, lo que puede mejorar significativamente el rendimiento de las consultas.

2.Reducción del tráfico de red: Al desnormalizar datos, se puede minimizar la cantidad de datos que se deben transferir a través de la red entre nodos. En una base de datos distribuida, el tráfico de red puede ser un cuello de botella, por lo que reducir la transferencia de datos entre nodos puede mejorar la eficiencia y la velocidad de las consultas.

3.Mejora de la escalabilidad: Al desnormalizar datos, se pueden distribuir y replicar los datos relevantes en diferentes nodos de manera más eficiente. Esto puede ayudar a distribuir la carga de trabajo y mejorar la escalabilidad del sistema, ya que se evita la necesidad de realizar uniones costosas entre nodos.

Supongamos que tenemos dos tablas relacionadas: "Usuarios" y "Pedidos".

Tabla "Usuarios":
- id_usuario (clave primaria)
- nombre
- dirección

Tabla "Pedidos":
- id_pedido (clave primaria)
- id_usuario (clave externa)
- fecha
- total

Para desnormalizar estos datos, podríamos agregar información de los usuarios directamente en la tabla de pedidos:

Tabla "Pedidos" (desnormalizada):
- id_pedido (clave primaria)
- id_usuario (clave externa)
- nombre_usuario
- dirección_usuario
- fecha
- total

Al desnormalizar los datos de esta manera, evitamos la necesidad de unir las tablas "Usuarios" y "Pedidos" para obtener información del usuario asociado a un pedido. Esto puede mejorar el rendimiento de las consultas que necesitan acceder a la información del usuario al eliminar la necesidad de operaciones de unión entre nodos diferentes.

Es importante tener en cuenta que la desnormalización también tiene sus desventajas potenciales, como la duplicación de datos y la posible inconsistencia si los datos desnormalizados no se actualizan correctamente. """

#----------------------------------------------------------------#

""" Distribución de carga de trabajo

La distribución de carga de trabajo para un query en una base de datos distribuida se realiza a través de un proceso llamado planificación de consultas distribuidas. Este proceso implica determinar cómo se ejecutará y distribuirá la consulta en los nodos de la base de datos distribuida para maximizar el rendimiento y la eficiencia.

A continuación, se describen los pasos generales involucrados en la distribución de carga de trabajo para un query en una base de datos distribuida:

1.Análisis de la consulta: Se examina la consulta para comprender su estructura, los datos involucrados y los operadores utilizados. Esto incluye la identificación de las tablas y las condiciones de filtrado, las operaciones de unión, agregación u otras operaciones específicas.

2.Descomposición de la consulta: La consulta se descompone en subconsultas más pequeñas que pueden ejecutarse en nodos individuales. Por ejemplo, si la consulta involucra una unión entre dos tablas, cada tabla se puede consultar de forma separada en los nodos respectivos antes de combinar los resultados.

3.Determinación de los nodos relevantes: Se identifican los nodos que contienen los datos necesarios para ejecutar cada subconsulta. Esto se basa en el esquema de distribución de datos utilizado en la base de datos distribuida, como el sharding o la replicación.

4.Planificación de ejecución: Se crea un plan de ejecución distribuido que define el orden y la forma en que se ejecutarán las subconsultas en los nodos relevantes. Esto puede incluir el envío de consultas a nodos específicos, la coordinación entre nodos para combinar resultados parciales y la optimización de la utilización de recursos.

5.Recolección de resultados: Una vez que cada subconsulta se ha ejecutado en los nodos respectivos, se recopilan los resultados parciales y se combinan para obtener el resultado final de la consulta. Esto puede implicar operaciones adicionales, como la agregación, la clasificación o la eliminación de duplicados. """

#----------------------------------------------------------------#
""" 
¿Qué es una base de datos distribuida?
R// Un sistema de gestión de bases de datos que almacena datos en múltiples servidores interconectados

¿Cuál es uno de los beneficios de desnormalizar datos en una base de datos distribuida?
R// Reducción de la necesidad de operaciones de unión(join) entre tablas

¿Qué son las clustering columns en una base de datos de columnas anchas (wide column)?
R// Columnas utilizadas para organizar y ordenas los datos dentro de una partición

¿Qué es el sharding en una base de datos distribuida?
R//La técnica de dividir y distribuir los datos entre múltiples nodos o servidores

¿Cuál es uno de los objetivos de la distribución de carga de trabajo en una base de datos distribuida?
R// Maximizar el rendimiento y la eficiencia de las consultas

¿Cuál es uno de los pasos involucrados en la distribución de carga de trabajo para un query en una base de datos distribuida?
R//Análisis de la consulta y determinación de los nodos relevantes """