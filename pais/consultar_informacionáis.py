"""
    Consultar información en una colección de MongoDB
    desde Python
"""
<<<<<<< HEAD:consultar_informacionáis.py
from enlace_basep import client

db = client.paisecuador
=======
from enlace_base import client

db = client.ciudadloja
>>>>>>> 0a2f48fea414d0e887a24306d54917e4074064a4:consultar_informacion.py
coleccion = db.autores

print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one()
print(data_01)

print("Muestra todos los documentos de la base de datos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)