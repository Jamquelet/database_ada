'''instalar: docs.sqlalchemy.org = pip install SQLAlchemy o conda install sqlalchemy

En un notebook con ! se conecta directamente con la termina !pip install SQLAlchemy ''' 

""" Supongamos que tenemos una base de datos con una tabla llamada "Usuarios" que contiene información sobre los usuarios registrados en nuestra aplicación, incluyendo los campos "id", "nombre" e "email". """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Configurar la conexión a la base de datos
engine = create_engine('sqlite:///usuarios.sqlite', echo=True) # crear una conexion con la base de datos con un archivo usuarios.sqlite para que funcione la extension en vsc.#echo para mostrar el sql que hay detras
Session = sessionmaker(bind=engine) #creo una session con la que me conecto a la base de datos
session = Session() # inicializo la session

#documentation: engine configuration engine = create_engine('postgresql+psycopg2://localhost:)
#url de conexion postgresql desde el dbeaver: edit conection - Server - URL sin el jdbc:

# Definir la clase Usuario
#crear tabla
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nombre={self.nombre}, email={self.email})"

#crea las tablas 
Base.metadata.create_all(engine)


#como creo una instancia de la tabla usuarios- cada instancia del objeto es una fila de la tabla
u1 = Usuario(nombre='Dad Lovelace', email='dadlovelace@gmail.com',)
print(u1)
session.add(u1) #interactuar con la db, agregar esa fila  y la mandamos a la base de datos
session.commit()

u2 = Usuario(nombre='Julio', email='jjuuull@gmail.com',)
print(u2)
session.add(u2) #interactuar con la db, agregar esa fila  y la mandamos a la base de datos
session.commit()

# Consulta utilizando SQLAlchemy.sacar los datos
usuarios = session.query(Usuario).all()#dame todos los usuarios

#iterar sobre estos datos
for usuario in usuarios:
    print(usuario.nombre, usuario.email)


"""  definimos la clase Usuario utilizando SQLAlchemy, donde cada columna de la tabla se representa como un atributo de clase. Luego, utilizamos session.query(Usuario).all() para realizar una consulta que obtiene todos los registros de la tabla y almacenamos los resultados en la variable usuarios. Finalmente, recorremos los objetos Usuario obtenidos e imprimimos su nombre y correo electrónico.

La línea session.query(Usuario).all() genera un SQL equivalente a SELECT * FROM Usuarios, de hecho podemos ejecutar consultas SQL directamente desde python de la siguiente forma """

#interfaz de bajo nivel de sqlite para python, ejecuta consultas, queries puros, manda desde pythonel query

import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Consulta utilizando SQL puro
cursor.execute("SELECT nombre, email FROM Usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario[0], usuario[1])

# Cerrar la conexión a la base de datos
conn.close()

""" En este caso, hemos establecido una conexión a la base de datos utilizando sqlite3, luego ejecutamos una consulta SQL directamente mediante cursor.execute() y recuperamos los resultados con cursor.fetchall(). Finalmente, iteramos sobre los resultados y los imprimimos en pantalla. """

""" La principal diferencia radica en que, con SQLAlchemy, podemos utilizar una interfaz orientada a objetos, trabajar con consultas más expresivas (como filtros, ordenamientos, etc.) y aprovechar las funcionalidades adicionales que el ORM proporciona, como relaciones entre tablas y transacciones. En contraste, con SQL puro, debemos construir manualmente las consultas en formato de cadena y manejar directamente la conexión y el cursor de la base de datos.

Una de las otras grandes diferencias, es que los ORMs sanitizan los inputs, evitando así que nos puedan realizar ataques como inyecciones SQL. """