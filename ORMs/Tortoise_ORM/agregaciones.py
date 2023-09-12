""" Agregaciones
En Tortoise ORM, las agregaciones se utilizan para realizar cálculos y operaciones sobre un queryset.

Para utilizar agregaciones sobre un queryset, debemos usar la función annotate para agregar resultados a las consultas. """

'----------------------------------------------------------------'

'Contar instancias'
from tortoise.functions import Count

async def count_users():
    count = await User.annotate(total=Count('id')).first()
    print(f'Total de usuarios: {count.total}')

run_async(count_users())

""" En este ejemplo, utilizamos Count('id') para contar el número total de instancias de User. Luego, utilizamos el método annotate para agregar el resultado de la agregación a la consulta y obtenemos el resultado utilizando first(). Finalmente, mostramos el total de usuarios. """

'----------------------------------------------------------------'

'Sumar valores'
from tortoise.functions import Sum

async def sum_values():
    total_sum = await Transaction.annotate(total_amount=Sum('amount')).first()
    print(f'Total de suma: {total_sum.total_amount}')

run_async(sum_values())

""" En este ejemplo, utilizamos Sum('amount') para sumar los valores de la columna amount en la tabla Transaction. Luego, utilizamos annotate y first() para obtener el resultado y mostramos la suma total. """

'----------------------------------------------------------------'

'Calcular el promedio'
from tortoise.functions import Avg

async def calculate_average():
    average = await Product.annotate(avg_price=Avg('price')).first()
    print(f'Precio promedio: {average.avg_price}')

run_async(calculate_average())

""" Es importante tener en cuenta que las agregaciones se realizan en el nivel de la base de datos, lo que significa que se aprovecha la funcionalidad nativa de la base de datos subyacente para calcular los resultados de manera eficiente. """

'----------------------------------------------------------------'

'ejemplo del uso de agregaciones y group by'

from tortoise import Model, Tortoise, fields, run_async
from tortoise.functions import Avg, Count, Sum


class Author(Model):
    name = fields.CharField(max_length=255)


class Book(Model):
    name = fields.CharField(max_length=255)
    author: fields.ForeignKeyRelation[Author] = fields.ForeignKeyField(
        "models.Author", related_name="books"
    )
    rating = fields.FloatField()


async def main():
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    a1 = await Author.create(name="author1")
    a2 = await Author.create(name="author2")
    for i in range(10):
        await Book.create(name=f"book{i}", author=a1, rating=i)
    for i in range(5):
        await Book.create(name=f"book{i}", author=a2, rating=i)

    ret = await Book.annotate(count=Count("id")).group_by("author_id").values("author_id", "count")
    print(ret)
run_async(main())

'salida del anterior codigo'
[{'author_id': 1, 'count': 10}, {'author_id': 2, 'count': 5}]

""" Este ejemplo define dos modelos: Author y Book. Book tiene una relación de clave externa (ForeignKeyField) con Author, lo que significa que cada libro está asociado a un autor. Además, Book tiene un campo rating para almacenar una calificación.

La función main es una función asíncrona que se ejecuta como punto de entrada. Dentro de la función main, se inicializa Tortoise ORM con una base de datos SQLite en memoria (db_url="sqlite://:memory:") y se generan los esquemas necesarios.

Luego, se crean instancias de Author y Book utilizando el método create. Se crean 10 libros asociados a author1 y 5 libros asociados a author2, cada uno con un rating incremental.

A continuación, se realiza una consulta utilizando el método annotate, que permite agregar anotaciones a la consulta. En este caso, se agrega una anotación count que cuenta la cantidad de registros en la tabla Book utilizando la función de agregación Count. Luego, se realiza una agrupación (group_by) por author_id y se obtienen los valores de author_id y count utilizando el método values.

Finalmente, se imprime el resultado de la consulta, que mostrará el recuento de libros agrupados por el ID del autor. """
