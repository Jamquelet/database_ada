""" Tortoise nos ofrece una serie de funciones para interactuar con el modelo (mapeo de la tabla) de forma simple para operaciones CRUD (Create, Retrieve, Update, Delete). """


'Los siguientes ejemplos hacen uso del modelo User creado anteriormente.'
""" Creación de una instancia
Para crear una nueva instancia de Usuario, se puede utilizar el método create proporcionado. """

async def create_user():
    user = await User.create(name='John Doe', email='johndoe@example.com')
    print(f'Usuario creado: {user.name} ({user.email})')

run_async(create_user())

'El método create devuelve la instancia recién creada, que podemos utilizar o mostrar según sea necesario'

'----------------------------------------------------------------'

""" Obtención de una instancia
Para obtener una instancia de Usuario basada en ciertos criterios, puedes utilizan los métodos get o get_or_none. """

async def get_user(user_id):
    user = await User.get_or_none(id=user_id)
    if user:
        print(f'Usuario encontrado: {user.name} ({user.email})')
    else:
        print('Usuario no encontrado')

run_async(get_user(1))

""" En este ejemplo, utilizamos el método get_or_none en el modelo User para obtener una instancia de usuario basada en su ID. Si se encuentra la instancia, imprimimos su nombre y correo electrónico.

La diferencia entre get y get_or_none radica en que get lanzará una excepción si no encuentra la instancia, mientras que get_or_none retornará None, lo cual hace más fácil controlar este caso desde Python. """

'----------------------------------------------------------------'

""" Actualización de una instancia
Para actualizar una instancia existente de Usuario, puedes utilizar el método save. """
async def update_user(user_id):
    user = await User.get_or_none(id=user_id)
    if user:
        user.name = 'Jane Smith'
        user.email = 'janesmith@example.com'
        await user.save()
        print(f'Usuario actualizado: {user.name} ({user.email})')
    else:
        print('Usuario no encontrado')

run_async(update_user(1))

'En este ejemplo, utilizamos el método get_or_none en el modelo User para obtener una instancia existente de usuario basada en su ID. Luego, actualizamos los campos name y email de la instancia y utilizamos el método save para guardar los cambios en la base de datos.'

'----------------------------------------------------------------'

""" Eliminación de una instancia
Para eliminar una instancia de Usuario, puedes utilizar el método delete. """

async def delete_user(user_id):
    deleted_count = await User.filter(id=user_id).delete()
    if deleted_count > 0:
        print('Usuario eliminado')
    else:
        print('Usuario no encontrado')

run_async(delete_user(1))

'En este ejemplo, utilizamos el método filter en el modelo User para filtrar las instancias basadas en ciertos criterios (en este caso, el ID del usuario). Luego, utilizamos el método delete para eliminar las instancias filtradas. El método delete devuelve el número de instancias eliminadas, por lo que podemos verificar si se eliminó algún usuario y mostrar un mensaje en consecuencia.'

'----------------------------------------------------------------'

""" Filtrado de datos
El método filter en Tortoise ORM se utiliza para filtrar instancias de un modelo en función de ciertos criterios. Este se llama en el modelo mismo y acepta argumentos de palabras clave para definir los criterios de filtrado.

Ejemplos del uso de filter

Filtrar por igualdad """

async def filter_users():
    users = await User.filter(name='John Doe')
    for user in users:
        print(user.name, user.email)

run_async(filter_users())

""" En este ejemplo, utilizamos User.filter(name='John Doe') para filtrar las instancias de User que tienen el nombre igual a "John Doe". Luego, iteramos sobre las instancias filtradas y las imprimimos. """

'----------------------------------------------------------------'

'Filtrar con múltiples condiciones'
async def filter_users():
    users = await User.filter(name='John Doe', email__contains='example.com')
    for user in users:
        print(user.name, user.email)

run_async(filter_users())

""" En este ejemplo, utilizamos User.filter(name='John Doe', email__contains='example.com') para filtrar las instancias de User que tienen el nombre igual a "John Doe" y el correo electrónico que contiene "example.com". Observa el uso de email__contains, donde el doble guion bajo (__) se utiliza para especificar una operación de filtrado más específica. """

'----------------------------------------------------------------'

'Filtrar con operadores de comparación'
from tortoise.expressions import Q

async def filter_users():
    users = await User.filter(Q(name='John Doe') | Q(name='Jane Smith'))
    for user in users:
        print(user.name, user.email)

run_async(filter_users())

""" En este ejemplo, utilizamos User.filter(Q(name='John Doe') | Q(name='Jane Smith')) para filtrar las instancias de User que tienen el nombre "John Doe" o el nombre "Jane Smith". Observa el uso de Q para combinar múltiples condiciones con operadores lógicos (| en este caso).

Es importante notar que filter devuelve un objeto de consulta (QuerySet) en lugar de las instancias reales. Para obtener los resultados, generalmente utilizamos métodos adicionales, como all() para obtener todas las instancias filtradas o first() para obtener la primera instancia. (Tortoise ORM utiliza una sintaxis similar a Django ORM, por lo que muchas de las funcionalidades y conceptos son compartidos). """