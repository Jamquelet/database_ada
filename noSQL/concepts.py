""" Paradigmas de bases de datos

Hasta ahora trabajamos con el paradigma de bases de datos más utilizado, el relacional, sin embargo existen otros seis paradigmas muy útiles:

1.Key-Value (Clave-Valor): En este paradigma, los datos se almacenan como pares clave-valor, donde cada valor está asociado a una clave única. Los datos se pueden acceder y recuperar mediante la clave correspondiente. Es un modelo simple y eficiente, ideal para casos de uso en los que la velocidad de recuperación de datos es crucial, como cachés o sistemas de sesiones. Algunos ejemplos populares de bases de datos de clave-valor son Redis y DynamoDB.

2.Wide Column (Columnas Anchas): Este paradigma se basa en la idea de almacenar datos en tablas con columnas flexibles y no estructuradas. A diferencia de las bases de datos relacionales tradicionales, donde las filas son rígidas y tienen un número fijo de columnas, las bases de datos de columnas anchas permiten agregar nuevas columnas dinámicamente. Este modelo es particularmente útil para casos de uso con datos muy variables o con necesidades de escalabilidad, como análisis de big data. Un ejemplo conocido de base de datos de columnas anchas es Apache Cassandra.

3.Document Oriented (Orientada a Documentos): En este paradigma, los datos se almacenan en documentos, generalmente en formatos como JSON o BSON. Cada documento contiene toda la información relacionada en una estructura autónoma, similar a un registro individual. Los datos se pueden consultar y manipular a través de consultas basadas en el contenido del documento. Este modelo es útil cuando se trabaja con datos semi-estructurados o no estructurados, y se utiliza en aplicaciones web, almacenamiento de contenido y análisis de registros. MongoDB es un ejemplo popular de base de datos documental.

4.Graph (Grafo): En este paradigma, los datos se representan como nodos interconectados en un grafo, donde los nodos representan entidades y las aristas representan las relaciones entre ellas. Este modelo es especialmente útil para casos de uso donde la relación y el análisis de las conexiones entre los datos son fundamentales, como redes sociales, recomendaciones y análisis de dependencias. Neo4j es una base de datos de grafo popular y ampliamente utilizada.

5.Search Engine (Motor de Búsqueda): Este paradigma se centra en la búsqueda y recuperación eficiente de información textual o no estructurada. Los datos se indexan y se pueden buscar utilizando consultas de texto completo o criterios de búsqueda avanzados. Este modelo es comúnmente utilizado en aplicaciones donde la búsqueda es la funcionalidad principal, como motores de búsqueda web y sistemas de recuperación de información. Ejemplos populares de bases de datos de motores de búsqueda son Elasticsearch y Apache Lucene.

6.Multi-Model (Multi-Modelo): Este paradigma combina múltiples paradigmas de bases de datos en un solo sistema. Permite trabajar con diferentes modelos de datos (como clave-valor, documento, columna ancha, etc.) dentro de la misma base de datos, lo que brinda flexibilidad y adaptabilidad en función de los requisitos específicos de cada caso de uso. Esto permite aprovechar las fortalezas de diferentes modelos de datos y simplificar la arquitectura general del sistema. Algunos ejemplos de bases de datos multi-modelo son ArangoDB y Couchbase. """

#----------------------------------------------------------------#

""" SQL vs NoSQL

Las bases de datos SQL y NoSQL son dos enfoques diferentes para almacenar y recuperar datos. Aquí te explico las principales diferencias entre ambos:

Bases de datos SQL (Structured Query Language):

1.Estructura de datos: Las bases de datos SQL siguen un modelo relacional, donde los datos se organizan en tablas con filas y columnas. Cada tabla tiene un esquema predefinido que define la estructura de los datos, incluyendo el tipo de datos y las restricciones.

2.Lenguaje de consulta: SQL es el lenguaje estándar utilizado para interactuar con bases de datos SQL. Permite realizar consultas complejas y relacionales utilizando sentencias como SELECT, INSERT, UPDATE y DELETE.

3.Transacciones y ACID: Las bases de datos SQL son conocidas por cumplir con las propiedades ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad). Esto garantiza que las transacciones sean consistentes y seguras, con operaciones atómicas y la capacidad de deshacer cambios en caso de error.

4.Escalabilidad vertical: Tradicionalmente, las bases de datos SQL se han escalado verticalmente, es decir, aumentando la capacidad de hardware de un servidor único. Sin embargo, también existen opciones para la escalabilidad horizontal, como la replicación y la fragmentación de datos.

----------------------------------------------------------------


Bases de datos NoSQL (Not Only SQL):

1.Estructura de datos: Las bases de datos NoSQL se diseñan para almacenar datos no estructurados o semi estructurados, y no siguen el modelo relacional. Los datos se pueden almacenar en diferentes formatos, como documentos, pares clave-valor, columnas anchas o gráficos.

2.Flexibilidad del esquema: Las bases de datos NoSQL ofrecen una mayor flexibilidad en cuanto al esquema de los datos. No se requiere un esquema predefinido, lo que permite agregar o modificar campos fácilmente sin afectar otros documentos o registros.

3.Modelos de consulta: Los modelos de consulta en bases de datos NoSQL varían según el tipo de base de datos. Algunas bases de datos NoSQL admiten consultas similares a SQL, mientras que otras utilizan interfaces y lenguajes específicos para acceder y manipular los datos.

4.Escalabilidad horizontal: Las bases de datos NoSQL se han diseñado para escalar horizontalmente, distribuyendo los datos en múltiples servidores o nodos. Esto permite un alto rendimiento y escalabilidad, ya que los datos se pueden distribuir y procesar en paralelo.
 """

 #----------------------------------------------------------------#

"""  Bases de datos distribuidas

Una base de datos distribuida es un sistema en el que los datos se almacenan y se gestionan en múltiples nodos o servidores interconectados. En lugar de tener un único servidor centralizado, la carga de trabajo y los datos se distribuyen entre diferentes nodos de la red. Cada nodo en la base de datos distribuida tiene su propio almacenamiento local y puede procesar consultas y transacciones de forma independiente.

El funcionamiento de una base de datos distribuida implica los siguientes aspectos clave:

1.Distribución de datos: Los datos se dividen y se almacenan en diferentes nodos de la red. Esto se puede hacer mediante particionamiento, donde los datos se dividen en particiones o rangos y se asignan a diferentes nodos, o mediante replicación, donde se copian los datos en varios nodos para mejorar la disponibilidad y la tolerancia a fallos.

2.Coordinación y sincronización: Para garantizar la coherencia de los datos distribuidos, se requiere coordinación y sincronización entre los nodos. Esto se logra a través de protocolos de concurrencia y control de transacciones, como el bloqueo distribuido y los algoritmos de consenso. Estos mecanismos aseguran que las transacciones se ejecuten correctamente y se mantenga la integridad de los datos.

3.Optimización de consultas: Las consultas y operaciones pueden distribuirse y ejecutarse en paralelo en diferentes nodos para mejorar el rendimiento y la escalabilidad. Los optimizadores de consultas en bases de datos distribuidas deben tener en cuenta la distribución de datos y las características de la red para generar planes de ejecución eficientes.

4.Tolerancia a fallos: Las bases de datos distribuidas están diseñadas para ser resistentes a fallos, lo que significa que pueden continuar operando incluso si uno o varios nodos fallan. Esto se logra mediante la replicación de datos y la capacidad de recuperación ante fallos, donde los nodos pueden recuperarse o reemplazarse sin afectar la disponibilidad de los datos. """

#----------------------------------------------------------------#

""" Distribución de los datos

Para distribuir datos eficientemente se utilizan las Clustering columns y el concepto de Shards

-Clustering Columns (Columnas de Agrupación)

En el contexto de las bases de datos de columnas anchas (wide column), las clustering columns se refieren a las columnas utilizadas para organizar y ordenar los datos dentro de una partición. Estas columnas definen el orden de las filas almacenadas dentro de una partición y determinan cómo se realizará el acceso a los datos.

Las clustering columns permiten ordenar las filas en función de un criterio específico, lo que facilita las consultas que requieren recuperar datos en un orden particular. Por ejemplo, si se tiene una tabla que almacena datos de ventas con clustering columns basadas en la fecha y el ID del producto, se puede acceder a las filas en función de una fecha específica o en función del orden del ID del producto.

El uso de clustering columns también puede mejorar el rendimiento de las consultas que necesitan recuperar un rango de datos, ya que los datos están organizados de manera eficiente y pueden ser accedidos en un orden secuencial.

-Sharding

Sharding es una técnica utilizada en bases de datos distribuidas para dividir y distribuir los datos entre múltiples nodos o servidores, conocidos como shard o fragmento. Cada shard es responsable de almacenar y gestionar un subconjunto de los datos totales de la base de datos.

La idea detrás del sharding es escalar horizontalmente el sistema distribuyendo la carga de trabajo y los datos entre varios nodos. Esto permite un mejor rendimiento y una mayor capacidad para manejar grandes volúmenes de datos y cargas de trabajo intensivas.

Al utilizar sharding, se divide el conjunto de datos en base a ciertos criterios, como el rango de valores de una clave o el hash de una clave. Cada shard se hace responsable de un subconjunto de datos que cumple con esos criterios. De esta manera, las consultas y transacciones pueden dirigirse a los shards específicos que contienen los datos relevantes, lo que permite una distribución equitativa de la carga y un mejor rendimiento en general.

El sharding también puede proporcionar redundancia y tolerancia a fallos, ya que los datos se pueden replicar en varios shards. Si un shard falla, los datos aún están disponibles en los otros shards.

Sin embargo, el sharding también introduce desafíos adicionales, como la necesidad de coordinación y sincronización entre los shards, y la gestión de consultas que abarcan múltiples shards. Además, el diseño y la elección de los criterios de sharding adecuados son aspectos críticos para garantizar un rendimiento y una escalabilidad óptimos en una base de datos distribuida. """