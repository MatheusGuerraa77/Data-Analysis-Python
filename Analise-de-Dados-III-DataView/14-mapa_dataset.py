import pandas as pd
import folium

#1-Importando o Dataset
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv'
dados_terremotos = pd.read_csv(url)

# 2 - Filtrar os dados para obter terremotos mais significativos

terremotos_significativos = dados_terremotos[dados_terremotos['mag'] >= 6.0]
print(terremotos_significativos)

# 3 - criar o Mapa
mapa_terremoto = folium.Map(location=[0,0], zoom_start=2)

# 4 - Adicio0na marcadores para terremotos significativos
for index, terremoto in terremotos_significativos.iterrows():
    folium.Marker(
        location=[terremoto['latitude'], terremoto['longitude']],
        popup=f'Magnitude:{terremoto['mag']}, Profundidade: {terremoto["depth"]}',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(mapa_terremoto)
    
mapa_terremoto.save('Analise-de-Dados-III-DataView/mapa_terremotos.html')