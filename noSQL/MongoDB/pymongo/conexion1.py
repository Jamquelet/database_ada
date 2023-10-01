#MongoDB en Python
#descargar MongoDB desde el sitio web oficial: https://www.mongodb.com/try/download/community
#Instala la biblioteca de MongoDB para Python, pymongo, utilizando pip
#---->pip install pymongo

#código básico para conectar con MongoDB, insertar un documento en una colección y luego consultar todos los documentos de esa colección:

import noSQL.MongoDB.pymongo.conexion1 as conexion1

# Conexión a MongoDB (asegúrate de que la URL y el puerto sean correctos)
client = conexion1.MongoClient("mongodb://localhost:27017/")

# Seleccionar una base de datos
db = client["miBaseDeDatos"]

# Seleccionar una colección
collection = db["miColeccion"]

# Datos que deseas insertar
data_to_insert = {
    "nombre": "Ejemplo",
    "edad": 30,
    "ocupacion": "Desarrollador"
}

# Insertar un documento en la colección
insert_result = collection.insert_one(data_to_insert)
print("Documento insertado con ID:", insert_result.inserted_id)

# Consultar todos los documentos en la colección
cursor = collection.find({})
print("Documentos en la colección:")
for document in cursor:
    print(document)

# Cerrar la conexión a MongoDB
client.close()

#otras operaciones como actualizaciones, eliminaciones, consultas más avanzadas y agregaciones