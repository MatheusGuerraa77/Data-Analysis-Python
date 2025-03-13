import folium 

# 1 - Criando um mapa centrado em uma localização específica
mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

# 2 - Adicionar Marcações para Cafeteiras
cafeteiras = [
    {'localização':[-23.5673, -46.6483], 'nome': 'Cafeteira A'},
    {'localização':[-23.5685, -46.6621], 'nome': 'Cafeteira B'},
    {'localização':[-23.5489, -46.6366], 'nome': 'Cafeteira C'},
    {'localização':[-23.5550, -46.6250], 'nome': 'Cafeteira D'}
    
]
for cafe in cafeteiras:
    folium.Marker(
        location=cafe['localização'],
        popup=cafe['nome'],
        icon=folium.Icon(color='green', icon='coffee')
    ).add_to(mapa)
    
mapa.save('Analise-de-Dados-III-DataView/mapa.html')