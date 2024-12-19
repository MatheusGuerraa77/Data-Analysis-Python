from pymongo import MongoClient

# 1 - Estabelece conexão com o mongoDB e o Database
client = MongoClient()
db = client['nobel']

prizes = db['prizes']
laureates = db['laureates']

# 1 - Lista o Mapeamentode gêneros
# Agregação processar os dados em uma coleção
# e produzir o resultado que foi gerado
print(db.laureates.distinct('gender'))
print(db.laureates.count_documents({'gender':'female'}))
print(db.laureates.count_documents({'gender':'male'}))
print(db.laureates.count_documents({'gender':'org'}))

# 2 - Lista o mapeamento da categoria dos prêmios
print(db.laureates.distinct('prizes.category'))

# Alguns prêmios foram compartilhados

# 3 - Quais categorias do prêmio, alem de física tem laureado com ações trimestrais?
print(db.laureates.distinct(
    'prizes.category',
    {
        'prizes.share':'4'}
))

print(db.prizes.distinct(
    'category',
    {'laureates.share':'4'}
))

# 4 - Quais categorias de Laureados que ganharam mais prêmios
print(db.laureates.distinct(
    'prizes.category',
    {'prizes.1':{
        '$exists': True
    }}
))