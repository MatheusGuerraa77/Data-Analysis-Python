from pymongo import MongoClient
import timeit

# 1 - Estabelece conexão com o mongoDB e o Database

client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1 - Todos os prêmios compartilhados entre 3 pessoas

for doc in db.prizes.find({
    'laureates.share':'3'
}):
    print('{year} {category}'.format(**doc))
    
print('\n')