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
"""digamos que nos equivocamos incertando la propiedad

db.productos.insertOne({
    "nombe": "pimienta"
})    

db.productos.update(
    {"nombe": "pimienta"}, 
    {
        "$set": {"nombre": "pimienta"}
    } 
)

db.productos.update(
    {"nombe": "pimienta"}, 
    {
        "$unset": {"nombe": null} #se borra la propiedad
    } 
)
"""