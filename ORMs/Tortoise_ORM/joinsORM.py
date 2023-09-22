from tortoise import fields
from tortoise.models import Model

class Estudiante(Model):
    nombre = fields.CharField(max_length=50)
    edad = fields.IntField()
    curso = fields.ForeignKeyField("models.Curso", related_name="estudiantes")


class Curso(Model):
    id = fields.IntField(pk=True)
    nombre = fields.CharField(max_length=50)


""" JOINs implícitos al realizar un filtrado
Cuando se usa el operador __ en el método .filter(), se realizan JOINs implícitos para acceder a los atributos de modelos relacionados. Este es un enfoque muy conveniente porque te permite aplicar filtros en campos de modelos relacionados sin tener que escribir la sentencia JOIN explícitamente.

Por ejemplo, si deseas encontrar todos los estudiantes que están inscritos en el curso Matemáticas, podrías hacer algo como esto: """

# estudiantes_matematicas = await Estudiante.filter(curso__nombre='Matemáticas').all()

""" Aquí, curso__nombre='Matemáticas' utiliza un JOIN implícito para filtrar los registros de Estudiante basados en el campo nombre de la tabla Curso. """


""" Este enfoque es especialmente útil porque minimiza la cantidad de código SQL manual que necesitas escribir, haciendo que tu código sea más legible y mantenible.

JOINs explícitos
select_related
El método select_related realiza un "JOIN" en SQL para obtener datos relacionados en una sola consulta. Esto es útil cuando tienes una relación "uno a muchos" y quieres obtener información del lado "uno" de la relación. En otras palabras, se usa principalmente para relaciones "ForeignKey". """

# Obtener todos los estudiantes que están inscritos en un curso específico junto con los detalles del curso
async def obtener_estudiantes_del_curso(curso_id):
    estudiantes = await Estudiante.filter(curso_id=curso_id).select_related("curso").all()
    for estudiante in estudiantes:
        print(estudiante.nombre, estudiante.curso.nombre)

""" En este ejemplo, select_related("curso") ejecuta un JOIN con la tabla Curso. Esto significa que la información del curso se recupera en la misma consulta que se usa para recuperar la información del estudiante.

prefetch_related
Por otro lado, prefetch_related realiza múltiples consultas pero las hace de manera eficiente para minimizar el número de llamadas a la base de datos. Esto es especialmente útil en relaciones "muchos a muchos" o "uno a muchos" cuando estás trabajando del lado "muchos" de la relación. """

# Obtener todos los cursos y los estudiantes inscritos en cada uno
async def obtener_cursos_y_estudiantes():
    cursos = await Curso.all().prefetch_related("estudiantes")
    for curso in cursos:
        print(curso.nombre)
        for estudiante in curso.estudiantes:
            print("  -", estudiante.nombre)

""" Aquí, prefetch_related("estudiantes") primero realiza una consulta para obtener todos los cursos. Luego, realiza una segunda consulta para obtener todos los estudiantes asociados con esos cursos. Finalmente, Tortoise ORM combina estos datos de manera eficiente en el lado de Python.

Relaciones no cargadas
Si intentas acceder a un atributo relacionado sin utilizar select_related o prefetch_related, Tortoise lanzará una excepción informándote que intentaste acceder a una relación que no ha sido cargada previamente.

Por ejemplo, si tienes algo como esto: """
async def obtener_estudiantes_del_curso(curso_id):
    estudiantes = await Estudiante.filter(curso_id=curso_id).all()
    for estudiante in estudiantes:
        print(estudiante.nombre, estudiante.curso.nombre)  # Esto lanzará una excepción

""" En este caso, se lanzará una excepción al intentar acceder a estudiante.curso.nombre, ya que la relación no ha sido cargada (es decir, no se aplicó el join para obtener los datos por la relación).

Otra opción es cargar la relación posteriormente utilizando fetch_related en un objeto ya recuperado: 
"""
async def obtener_estudiantes_del_curso(curso_id):
    estudiantes = await Estudiante.filter(curso_id=curso_id).all()
    for estudiante in estudiantes:
        await estudiante.fetch_related('curso')  # Esto carga la relación
        print(estudiante.nombre, estudiante.curso.nombre)  # Esto funcionará correctamente

""" Usar fetch_related en este caso hará que se realice una consulta adicional a la base de datos por cada estudiante en el ciclo, lo cual no es muy eficiente (ya que terminarás realizando 
�
+
1
N+1 queries pequeñas, lo cual es muy costoso, en vez de una sola consulta grande pero eficiente). Por eso es preferible usar select_related o prefetch_related cuando conoces de antemano que vas a necesitar acceder a datos relacionados. """