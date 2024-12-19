from pymongo import MongoClient

# 1 - Estabelece conexão com o mongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 2 - Buscando o primeiro documento
walter = db.laureates.find_one({
    'firstname':'Walter',
    'surname':'Kohn'
})
print(walter)

# 3 - Pesquisando em uma subestrutura 
california = db.laureates.count_documents({
    'prizes.affiliations.name': 'University of California'
})
print(california)

san_francisco = db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})
print(san_francisco)

# 4 - Conta Documentos que não possua uma informação
no_country = db.laureates.count_documents({
    'bornCountry':{
        '$exists': False
    }
})
print(no_country)
