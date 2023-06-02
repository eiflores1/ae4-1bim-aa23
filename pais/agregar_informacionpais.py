"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_basep import client

db = client.paisecuador
coleccion = db.autores

lista = [
{"pais": "ecuador", "presidente": "lasso", "lugares":"loja",
"poblacion": 200000},
{"pais": "ecuador", "presidente": "lasso", "lugares":"eloro",
"poblacion": 2000},
{"pais": "ecuador", "presidente": "lasso", "lugares":"azuay",
"poblacion": 100000}
]

coleccion.insert_many(lista)