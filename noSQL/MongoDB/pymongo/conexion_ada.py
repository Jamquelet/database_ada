#conda install -c anaconda pymongo
#!pip install pymongo

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

username = ''
password = ''
cluster_url = 'cluster0.ovluabh.mongodb.net' #connect -> drivers -> python

#construir la URL de conexión
connection_url = f'mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority'

#crear una instancia del cliente de MongoDB
client = MongoClient(connection_url, server_api=ServerApi('1'))

#seleccionar la base de datos
db = client['clase_atlas_ada']

#ejemplo: crear colección
db.create_collection('users')

#ejemplo: acceder a una colección y realizar una consulta
collection = db['users']

#----------------------------------------------------------------

