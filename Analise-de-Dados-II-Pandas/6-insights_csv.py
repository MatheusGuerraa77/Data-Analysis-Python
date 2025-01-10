#Insights:
#1- Desempenho Vendas por Região
#2- Vendedor mais produtivo
#3- Itens mais vendidos
#4- Preço Médio por item
#5- Correlação entre unidade Vendida e Preço Unitário

import pandas as pd
df = pd.read_csv('data1/pedidos.csv')

df['Unidades'] = pd.to_numeric(df['Unidades'])
df['PrecoUnidade'] = pd.to_numeric(df['PrecoUnidade'])

#1 - Desempenho Vendas por Região
venda_regiao = df.groupby('Regiao')['Unidades'].sum()
print(venda_regiao)

# 2 - Vendedor mais produtivo
vendas_vendedor = df.groupby('Vendedor')['Unidades'].sum()
print(vendas_vendedor.idxmax())

# 3 - Total de unidades vendidas por item
total_unidades_item = df.groupby('Item')['Unidades'].sum()
print(total_unidades_item)

# 4 - Média de Preço por Item
media_preco_item = df.groupby('Item')['PrecoUnidade'].mean()
print(media_preco_item)

#5 - Correlação entre unidade Vendida e Preço Unitário
"""
A correlação pode variar entre -1 e 1, indicando a direção e a 
força da relação linear entre as variáveis.
Um valor próximo de 1 indica uma correlação positiva forte,
enquanto próximo de -1 indica correlação negativa forte.
Um valor próximo a 0 indica uma correlação fraca.
"""
correlacao = df['Unidades'].corr(df['PrecoUnidade'])
print(correlacao)
