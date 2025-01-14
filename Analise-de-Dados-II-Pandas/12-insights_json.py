import pandas as pd

# 1 - Importando o arquivo Json
df = pd.read_json('data1/series.json')

# 2 - Análise total de Episódios por Séries
temporadas_expandidas = []
for serie in df['series']:
    total_episodios = sum(temporada['episodios'] for temporada in serie['temporadas'])
    serie_info = {
        'titulo': serie['titulo'],
        'genero': serie['genero'],
        'total_episodios': total_episodios
    }
    temporadas_expandidas.append(serie_info)
    # print(temporadas_expandidas)
    
df_expandido = pd.DataFrame(temporadas_expandidas)
print(df_expandido)