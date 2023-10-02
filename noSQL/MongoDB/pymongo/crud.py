collection = ['archivo -> conexion_ada']

#documento a insertar
new_document = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john@example.com'
}

#----------------------------------------------------------------

#insertar el documento en la colección
result = collection.insert_one(new_document)
print('Insert ID', result.inserted_id) 

#----------------------------------------------------------------

#leer todos los documentos en la colección
all_documents = collection.find() # si no se da argumento los trae todos, el find es iterable

for document in all_documents:
    print(document)

#----------------------------------------------------------------

#actualizar un documento por algún campo(en este ejemplo usando el campo name)
query = {'name': 'John Doe'}
new_values = {'$set': {'age': 31}} #actualizar la edad a 31

result = collection.update_one(query, new_values)

print('Documentos modificados:', result.modified_count)

#----------------------------------------------------------------

#eliminar un documento por algun campo
query = {'name': 'John Doe'}
result = collection.delete_one(query)

print('Documentos eliminados:', result.deleted_count)