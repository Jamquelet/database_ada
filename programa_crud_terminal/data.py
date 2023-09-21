""" from models import *

async def fill_data():
    categorias = [
        {'nombre': 'Electronicos'},
        {'nombre': 'Ropa'}
        {'nombre': 'Hogar'},
        {'nombre': 'Deportes'},
        {'nombre': 'Juguetes'},
    ]
    categorias = [Categoria(**categoria)for categoria in categorias]
    for categoria in categorias: 
        await categoria.save()

    productos = [
        {1, 'Televisor', 'Sony', 1, 1000},
        {2, 'Laptop', 'HP', 1, 800},
        {, 'Camisa', 'Zara', 2, 50},
        {4, 'Pantalon', 'Levis', 2, 70},
        {5, 'Sarten', 'T-fal', 3, 30},
        {6, 'Toalla', 'Cannon', 3, 20},
        {7, 'Pelota', 'Nike', 4, 15},
        {8, 'Raqueta', 'Wilson', 4, 50},
        {9, 'Muñeca', 'Barbie', 5, 25},
        {10, 'Carro', 'Hot Wheels', 5, 10}
    ]
 """