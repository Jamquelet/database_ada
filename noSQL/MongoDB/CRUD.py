""" crud nativo en mongo

Create
db.collection.insertOne()
db.collection.insertMany()

#----------------------------------------------------------------

Read
db.collection.find()

#----------------------------------------------------------------

Update
db.collection.updateOne()
db.collection.updateMany()

#----------------------------------------------------------------

Delete
db.collection.deleteOne()
db.collection.deleteMany()

 """

 #----------------------------------------------------------------

"""  {
    "nombre": "papitas",
    "fabricante": "lays",
    "precio": 10
}

{
    "nombre": "pepsi",
    "fabricante": "pepsico",
    "precio": 8,
    "cantidad": "2L"
} """

#----------------------------------------------------------------

"""digamos que nos equivocamos incertando la propiedad

db.productos.insertOne({
    "nombe": "pimienta"
})    

db.productos.updateOne(  #actualizar el nombre
    {"nombe": "pimienta"}, 
    {
        "$set": {"nombre": "pimienta"}
    } 
)

db.productos.updateOne(
    {"nombe": "pimienta"}, 
    {
        "$unset": {"nombe": null} #se borra la propiedad
    } 
)

db.productos.insertOne({
    "nombre": "Doritos",
    "fabricante": "pepsico"
})

#leer datos

db.productos.find() #  si no se le manda nada lee todas las entradas

db.productos.find({"fabricante": "pepsico"})

db.productos.find({"precio": {"$lte: 9}}) # lt - lte: less menor que equal: menor o igual que
 

#deleteOne : elimina el primero q encuentra

db.productos.deleteOne({"nombre": "pimienta})

"""