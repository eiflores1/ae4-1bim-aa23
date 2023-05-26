"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.ciudadloja
coleccion = db.autores

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario
# proceso que agrega un solo documento
data_01 = {"nombre": "Luis", "apellido": "Valencia",
"nacionalidad":"ecuatoriana", "numero_publicaciones": 100}

# coleccion.insert_one(data_01)

# proceso que agrega una lista de documentos
lista = [
{"ciudad": "Loja", "comidas": "cecina", "lugares":"eolicos",
"poblacion": 200000},
{"ciudad": "Loja", "comidas": "repe", "lugares":"vilcabamba",
"poblacion": 10000},
{"ciudad": "Loja", "comidas": "fritada", "lugares":"malacatos",
"poblacion": 15000}
]

coleccion.insert_many(lista)