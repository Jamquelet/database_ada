"""
documentación oficial: https://www.mongodb.com/docs/manual/core/document/ 
operaciones de CRUD en MongoDB: https://www.mongodb.com/docs/manual/crud/

Qué es MongoDB?
➢ sistema de Base de datos no relacional (NoSQL)
➢ Utiliza el paradigma de bases de datos basado en documentos
➢ Estructura de datos dinámica
➢ Escalamiento: Horizontal y vertical

Server -> Databases -> Collection -> Document

--------------------------------

json:  Se parece a un dict en python, contiene los valores NULL y True - False
{
    "glosary": {
    
    }
}
 """
# ----------------------------------------------------------------#

"""INSTALACION 
lsb_release -a = ubuntu 22.04
cd ~/Descargas
sudo dpkg -i nombre_del_archivo.deb = instalarlo con el compando dpkg
sudo apt-get install -f = dependencias faltantes
sudo systemctl status mongod = verificar si se esta ejecutando
sudo systemctl start mongod = iniciar el servicio

tar -zxvf mongodb-compass-<versión>-linux-x64.tar.gz = mongo compas

tar -zxvf studio-3t-linux-x64.tar.gz = robo3t descomprime
chmod +x studio-3t-linux-x64.sh = permisos de ejecucion
./studio-3t-linux-x64.sh = ejecutar el script
nueva conexion= mongodb://localhost


-Instalar mongo db community server en tu computadora recomendada la version estable (current release): https://www.mongodb.com/try/download/community 
-Instalar el cliente de robo 3t: https://robomongo.org/ #editor similar a dbeaber para mongo
Usando el cliente de robo 3t conectate a la base de datos local:                                  Connection String URI Format — MongoDB Manual
#Conexion: new connection -> url: mongodb://localhost
Crea una base de datos llamada ejercicio1
Crea dentro de la base de datos una colección llamada usuarios con click derecho sobre collections
Crea dentro de la colección usuarios 3 documentos de ejemplo:
Un usuario con nombre y edad.
Un usuario con nombre, apellido y edad.
Un usuario con solo nombre.
 """

#----------------------------------------------------------------#

""" {"_comentario":"// /*js*/ //add database -> name_database -> add new collection -> producto -> add new document"} """

{
    "nombre": "papitas",
    "fabricante": "lays",
    "precio": 10
}

{
    "nombre": "pepsi",
    "fabricante": "pepsico",
    "precio": 8,
    "cantidad": "2L"
}

#----------------------------------------------------------------#

""" Quiz 

¿Qué es mongo DB?
R//sistema de gestión de bases de datos no relacional (NoSQL), orientado a documentos

¿En cuál formato se almacena la información en MongoDB?
R//BSON

Dentro de una base de datos de mongoDB las agrupaciones de información más grandes se conocen como: COLECCIONES

Cada registro dentro de una base de datos de MongoDB es un: DOCUMENTO

Para insertar un único registro dentro de MongoDB se debe usar:
R// db.collection.insertOne()

Para actualizar varios registros dentro de MongoDB debemos utilizar:
R// db.collection.updateMany()

La versión gratuita de MongoDB para descargar e instalar de forma local en tu ordenador se llama:
R// MongoDB Community Server

 """

 #----------------------------------------------------------------#
