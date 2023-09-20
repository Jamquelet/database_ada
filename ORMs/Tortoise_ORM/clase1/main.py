'''Código de configuracion para inicializar Tortoise ORM y preparar la conexión a la base de datos'''


from tortoise import Tortoise, run_async
from models import User

async def main():
    await Tortoise.init(
        db_url='postgres://postgres:######@localhost:5432/###', #'postgres://username:password@localhost:5432/database'
        modules={'models': ['models']},
    )
    await Tortoise.generate_schemas(safe=True) #crear todas las tablas que esten en el archivo models, safe true evitar problema si la tabla ya existe da error, create table if not exists
    
    #crear instancia
    #user = await User.create(name='Jeison', email='jei@example.com')

    """   #Obtener-recuperar: retrieve
    user = await User.get_or_none(id=1)
    #print(user.__repr__()) 
    print(user)
    #dame el user o retorna none si el user no existe """

    """  #actualizar datos
    user.name = 'John'
    user.email = 'john@example.com'
    await user.save()
    """
    
    #eliminar
    user = await User.get_or_none(name='Jeison')
    await user.delete()

    #select where #select * from user where name='Jeison' in sql
    users = await User.filter(name='Jeison') #.all()
    print(users)

    #delete one people
    await User.filter(name='Jeison', email='jei@example.com').delete()

    #actualizar en una linea
    await User.filter(name='Jeison', email='jei@example.com').update(email='jeison@example.com')

run_async(main()) 

""" User.bulk_create([
    users(...),
    users(...)]) """

'--------------------------------------------------------------------------------'

#sqlite3
""" from tortoise import Tortoise, run_async

async def main():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['main']},
    )
    await Tortoise.generate_schemas(safe=True)
    
    # A partir de aquí, puedes utilizar Tortoise ORM para interactuar con la base de datos

run_async(main()) """

