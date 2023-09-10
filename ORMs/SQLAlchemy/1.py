""" Supongamos que tenemos una base de datos con una tabla llamada "Usuarios" que contiene información sobre los usuarios registrados en nuestra aplicación, incluyendo los campos "id", "nombre" e "email". """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String

# Configurar la conexión a la base de datos
engine = create_engine('sqlite:///usuarios.db')
Session = sessionmaker(bind=engine)
session = Session()

# Definir la clase Usuario
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)

# Consulta utilizando SQLAlchemy
usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(usuario.nombre, usuario.email)


"""  definimos la clase Usuario utilizando SQLAlchemy, donde cada columna de la tabla se representa como un atributo de clase. Luego, utilizamos session.query(Usuario).all() para realizar una consulta que obtiene todos los registros de la tabla y almacenamos los resultados en la variable usuarios. Finalmente, recorremos los objetos Usuario obtenidos e imprimimos su nombre y correo electrónico.

La línea session.query(Usuario).all() genera un SQL equivalente a SELECT * FROM Usuarios, de hecho podemos ejecutar consultas SQL directamente desde python de la siguiente forma """

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