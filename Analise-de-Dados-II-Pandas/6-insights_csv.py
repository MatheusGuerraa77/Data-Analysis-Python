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