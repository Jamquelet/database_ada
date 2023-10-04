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

""" 
Consultar todos los documentos en una colección:
db.miColeccion.find()

Consultar documentos que cumplan con una condición específica:
db.miColeccion.find({ campo: valor })

----------------------------------------------------------------

Operadores de Comparación:

Igualdad: $eq
Mayor que: $gt
Menor que: $lt
Mayor o igual que: $gte
Menor o igual que: $lte
No igual: $ne

db.miColeccion.find({ edad: { $gte: 18, $lte: 30 } })

----------------------------------------------------------------

Operadores Lógicos:

AND: $and
OR: $or
NOT: $not

db.miColeccion.find({ $or: [{ edad: { $lt: 18 } }, { profesion: "Estudiante" }] })

----------------------------------------------------------------

Operadores de Elemento:

$exists: Verificar si un campo existe en un documento.
$type: Filtrar documentos por tipo de dato.

db.miColeccion.find({ campo: { $exists: true, $type: "string" } })

----------------------------------------------------------------

Consultas de Texto Completo (índices de texto):

$text: Realizar búsquedas de texto completo en campos indexados.

db.miColeccion.find({ $text: { $search: "palabra" } })

----------------------------------------------------------------

Consultas Geoespaciales:

Realizar consultas basadas en coordenadas geográficas utilizando operadores como $near y $geoWithin.

db.miColeccion.find({ ubicacion: { $near: { $geometry: { type: "Point", coordinates: [longitud, latitud] }, $maxDistance: distanciaEnMetros } } })

----------------------------------------------------------------

Agregación:

Utilizar el framework de agregación para realizar operaciones más complejas, como agrupar, proyectar y calcular estadísticas en documentos.

db.miColeccion.aggregate([
  { $group: { _id: "$categoria", total: { $sum: 1 } } },
  { $sort: { total: -1 } }
])

----------------------------------------------------------------

OPERACIONES DE CONSULTA

Ejemplo de Curso MongoDB - 8 operaciones de consulta
db = empresa, collection = empleados con dos documentos que tienen los atributos:

{
"_id": ObjectId("60cece336644999a80947"),
"nombres" : "Jaime",
"apellidos" : "Code",
"experiencia" : 7.0,
"nacimiento" : ISODate("1991-03-27t05:00:00.000z"),
"estado" : 1.0,
"telefono" : ["958984", "885595"],
"identidad" : {
    "sexo" : "M",
    "pais" : "PERU",
    "cedula" : "111230088",
    "estadoCivil" : "s"
  }
} 

#alternativas de busquedas con el operador find
db.getCollection('empleados').find({}) #salen todos los registros

#buscar un valor en particular

db.getCollection('empleados').find({"estado" : 1 }) #aquellos cullo estado sea 1

db.getCollection('empleados').find({"estado" : {$in: [1,0] }}) #que tengan un estado entre 1 y 0, no busca en un rango de valores, busca la coincidencia exacta si es que esta alguno de estos valores en el atributo estado

db.getCollection('empleados').find({"experiencia" : {$lt: 8 }}) #buscar por un criterio de menor a algun valor. Por atributo(gt, gte, lt, lte) lowar than, lower than equals, greater than equals

#operador and para realizar una busqueda donde tenga dos atributos que no son excluyentes que si o si se deben coincidir para dar un resultado}
db.getCollection('empleados').find({"estado" : 1, "experiencia" : {$lt: 8 }})

#operador or 
db.getCollection('empleados').find({ $or: [ {"estado" : 0}, {"experiencia" : {$lt: 8 }}] }) # un criterio o el otro, si coinciden los dos muestra los dos

#Operación AND y OR
db.getCollection('empleados').find({ "nombres":"Jaime", $or: [ {"estado" : 0}, {"experiencia" : {$lt: 8 }}] }) # el nombre seria mandatorio, el or puede o no se puede resolver

#busqueda en arreglos
db.getCollection('empleados').find({ "telefonos":["958984", "885595"] }) #regresa el elemento que tiene ese criterio, si solo de deja un telefono no da ninguna coincidencia, busca con exactitud todo el contenido del atributo, si no no lo resuelve

#$all
db.getCollection('empleados').find({ "telefonos":{$all: ["958984"] }}) #si lo resuelve, all busca alguno de esos elementos dentro de cualquier posicion del arreglo

#busqueda anidada
db.getCollection('empleados').find({ "identidad.sexo": "M" }) #buscar si la identidad del documento es masculino

db.getCollection('empleados').find({ "identidad.pais": "PERU" }) 


----------------------------------------------------------------

OPERACIONES DE AGREGACIÓN

#count()
db.getCollection('empleados').count() #cantidad de documentos en una collection

#distinct()
db.getCollection('empleados').distinct("experiencia") # atributo que queremos hacer esa distincion, los repetidos se cuenta como uno solo

# $ para hacer referencia al atributo 

# aggregate $group
db.getCollection('empleados').aggregate([{$group : {_id : "$experiencia", x : {$sum : 1 }}} ]) #contar los empleados agrupados por su experiencia

#$avg | average
db.getCollection('empleados').aggregate([{$group : {_id : "$estado", x : {$avg : "$experiencia" }}} ]) # calcular el promedio de experiencias agrupados por estado

# $max | maximun
db.getCollection('empleados').aggregate([{$group : {_id : "$estado", x : {$max : "$experiencia" }}} ]) # calcular la experiencia maxima agrupado por el estado

# $min | minumun
db.getCollection('empleados').aggregate([{$group : {_id : "$estado", x : {$min : "$experiencia" }}} ]) #calcular el minimo 

# $first # devuelve ese atributo pero de la primera coincidencia del conjunto de resultados 
db.getCollection('empleados').aggregate([{$group : {_id : "$estado", x : {$first : "$telefonos" }}} ]) # segun algun criterio que quiera agrupar, por ej por el estado quisiera extraer o devolver otro atributo por ej los telefonos

# $last # finales
db.getCollection('empleados').aggregate([{$group : {_id : "$estado", x : {$last : "$telefonos" }}} ])
 """