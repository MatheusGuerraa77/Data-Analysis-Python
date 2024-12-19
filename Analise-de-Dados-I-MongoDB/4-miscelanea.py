from pymongo import MongoClient

# 1 - Estabelece conexão com o mongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']


#ERRADO
print(db.laureates.count_documents({
    'prizes':{
        'category':'physics',
        'share':'1'
    }
}))

# 2- Todos os Laureados que possuem prêmio em física e compartilhado
print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category':'physics',
            'share':'1'
        }
    }
}))

# 3 - Todos os Laureados que possem prêmio em física compartilhado antess de 1945
print(db.laureates.count_documents({
    'prizes':{
        '$elemMatch':{
            'category':'physics',
            'share':'1',
            'year':{'$lt': '1945'}
        }
    }
}))