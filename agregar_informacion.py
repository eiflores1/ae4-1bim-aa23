"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.ciudadloja
coleccion = db.autores

lista = [
{"ciudad": "loja", "parroquia": "vilcabamba", "lugares":"paque",
"poblacion": 200},
{"ciudad": "loja", "parroquia": "elvalle", "lugares":"parque",
"poblacion": 2000},
{"ciudad": "loja", "parroquia": "sucre", "lugares":"centro",
"poblacion": 100000}
]

coleccion.insert_many(lista)