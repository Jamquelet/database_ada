""" Tortoise nos ofrece una serie de funciones para interactuar con el modelo (mapeo de la tabla) de forma simple para operaciones CRUD (Create, Retrieve, Update, Delete). """


'Los siguientes ejemplos hacen uso del modelo User creado anteriormente.'
""" Creación de una instancia
Para crear una nueva instancia de Usuario, se puede utilizar el método create proporcionado. """

async def create_user():
    user = await User.create(name='John Doe', email='johndoe@example.com')
    print(f'Usuario creado: {user.name} ({user.email})')

run_async(create_user())
