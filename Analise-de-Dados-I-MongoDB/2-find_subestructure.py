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

# 5 - Verificando se os laureados possuem prêmios
qtd = db.laureates.count_documents({})
print(qtd)

qtd_prizes = db.laureates.count_documents({
    'prizes':{
        '$exists': True
    }
})
print(qtd_prizes)

# 6 - Verificação se o prize está preenchido
prize_contain = db.laureates.count_documents({
    'prizes.0':{
        '$exists': True
    }
})
print(prize_contain)

# 7 - Verificação dos Laureados que tenham mais de um prêmio
prize_mult = db.laureates.count_documents({
    'prizes.1':{
        '$exists': True
    }
})
print(prize_mult)