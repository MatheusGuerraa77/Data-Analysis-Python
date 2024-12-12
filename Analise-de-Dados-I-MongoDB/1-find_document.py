from pymongo import MongoClient

# 1 - Estabelece conexão com o mongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 2 - Filtra documentos por gênero
print(db.laureates.count_documents({'gender':'female'}))
print(db.laureates.count_documents({'gender':'male'}))

# 3 - Contar documentos pelo país que morreu
print(db.laureates.count_documents({'diedCountry':'France'}))

# 4 - Filtro composto com algumas informações
filter_doc = {
    "diedCountry": 'France',
    'gender': 'female',
    'bornCity': 'Warsaw'
}
print(db.laureates.count_documents(filter_doc))
print(db.laureates.find_one(filter_doc))

"""
Marie Curie ganhou pelas descobertas dos elementos radio e polônio

"""