""" 
-> Queries en MongoDB:
documentación:  https://www.mongodb.com/docs/manual/tutorial/query-documents/

En MongoDB, un "query" (consulta en español) se refiere a una solicitud de información de la base de datos. Un query en MongoDB se compone de un conjunto de criterios de búsqueda que se aplican a los documentos almacenados en una colección. Estos criterios pueden incluir condiciones como igualdad, desigualdad, comparación, y operadores lógicos para combinar varias condiciones.

----------------------------------------------------------------

-> Operadores de queries MongoDB - https://www.w3schools.com/mongodb/mongodb_query_operators.php

En MongoDB, los operadores de consulta (query operators en inglés) son símbolos o palabras clave que se utilizan para construir consultas avanzadas en las que se especifican criterios de búsqueda más precisos. Estos operadores se utilizan dentro de la sintaxis básica de una consulta de MongoDB para construir criterios de búsqueda más complejos.

Algunos de los operadores de consulta más comunes en MongoDB son:

-$eq: Se utiliza para encontrar documentos con un campo específico que sea igual a un valor dado.
-$ne: Se utiliza para encontrar documentos con un campo específico que no sea igual a un valor dado.
-$gt: Se utiliza para encontrar documentos con un campo específico que sea mayor que un valor dado.
-$lt: Se utiliza para encontrar documentos con un campo específico que sea menor que un valor dado.
-$gte: Se utiliza para encontrar documentos con un campo específico que sea mayor o igual que un valor dado.
-$lte: Se utiliza para encontrar documentos con un campo específico que sea menor o igual que un valor dado.
-$in: Se utiliza para buscar documentos en los que un campo específico coincida con cualquier valor de un conjunto dado de valores.
-$nin: Se utiliza para buscar documentos en los que un campo específico no coincida con ningún valor de un conjunto dado de valores.
-$or: Se utiliza para combinar múltiples criterios de búsqueda con una cláusula "OR".
-$and: Se utiliza para combinar múltiples criterios de búsqueda con una cláusula "AND".

----------------------------------------------------------------

Agregaciones MongoDB - https://www.mongodb.com/docs/drivers/node/current/fundamentals/aggregation/

Las agregaciones en MongoDB son una herramienta muy poderosa para procesar y analizar datos en una base de datos. Las agregaciones son una serie de operaciones que se aplican a los datos de una colección, con el objetivo de obtener información útil o resumida sobre esos datos.

En MongoDB, las agregaciones se construyen utilizando un conjunto de operaciones para filtrar, transformar y agrupar datos de una colección. Las operaciones de agregación se realizan en una serie de etapas, donde cada etapa aplica una operación específica a los datos y pasa el resultado a la siguiente etapa. Las etapas se pueden utilizar para realizar una amplia variedad de tareas, como filtrar documentos, agrupar documentos por campos específicos, realizar cálculos estadísticos, combinar colecciones y más.

-$match: Filtra los documentos de una colección según ciertos criterios de búsqueda.
-$group: Agrupa los documentos de una colección por uno o más campos y realiza operaciones de agregación sobre los grupos.
-$project: Permite seleccionar o excluir campos específicos de los documentos de una colección.
-$sort: Ordena los documentos de una colección según uno o más campos.
-$limit: Limita el número de documentos que se devuelven en una consulta.
-$skip: Salta un número determinado de documentos en una consulta.

 """