"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.paisecuador
coleccion = db.autores

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Luis", "apellido": "Valencia",
"nacionalidad":"ecuatoriana", "numero_publicaciones": 100}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"pais": "ecuador", "presidente": "lasso", "lugares":"loja",
"poblacion": 200000},
{"pais": "ecuador", "presidente": "lasso", "lugares":"eloro",
"poblacion": 2000},
{"pais": "ecuador", "presidente": "lasso", "lugares":"azuay",
"poblacion": 100000}
]

coleccion.insert_many(lista)