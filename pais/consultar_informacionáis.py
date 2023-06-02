"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_basepais import client

db = client.paisecuador
coleccion = db.autores

print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one()
print(data_01)

print("Muestra todos los documentos de la base de datos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)