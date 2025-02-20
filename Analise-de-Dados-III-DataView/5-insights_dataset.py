import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data1/pedidos.csv')

# Gráfico 1 - Quantidade de unidades vendidas por região
plt.figure(figsize=(8, 6))
df.groupby('Regiao')['Unidades'].sum().plot(kind='bar', color='skyblue')
plt.title('Quantidade de Unidades Vendidas por Regiao')
plt.xlabel('Região')
plt.ylabel('Total de Unidades Vendidas')
plt.xticks(rotation=45)
plt.show()

# Gráfico 2 - Distribuição das vendas por item(pizza)
plt.figure(figsize=(8, 6))
df['Item'].values_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição das Vendas por Item')
plt.axis('equal')
plt.show()

# Gráfico 3 - Relação entre preço unitário e quantidade de unidades
plt.figure(figsize=(8, 6))
plt.scatter(
    df['PrecoUnidade'],
    df['Unidades'],
    color='orange'
)
plt.title('Relação entre Preço Unitário e Quantidade de Unidades')
plt.xlabel('Preço Unitário')
plt.ylabel('Quantidade de Unidades')
plt.grid(True)
plt.show()

# Gráfico 4- Quantidade de unidades vendidas ao longo do tempo
# Convertendo a coluna DataPedido para o formato de data

df['DataPedido'] = pd.to_datetime(df['DataPedido'])

plt.figure(figsize=(10, 6))
df.groupby('DataPedido')['Unidades'].sum().plot(kind='line', marker='o', color='green')
plt.title('Quantidade de Unidades Vendidas ao Longo do Tempo')
plt.xlabel('Data do Pedido')
plt.ylabel('Total de Unidades Vendidas')
plt.grid(True)
plt.show()

# Gráfico 5 - Qunatidade de unidades Vendidas por Estado em cada região
pivot = df.pivot_table(
    index='Estado',
    columns='Regiao',
    values='Unidades',
    oggfunc='sum',
    fill_value=0
)
plt.figure(figsize=(10, 6))
pivot.plot(kind='bar', stacked=True)
plt.title('Quantidade de Unidades Vendidas por Estado em cada Região')
plt.xlabel('Estado')
plt.ylabel('Total de Unidades Vendidas')
plt.legend(title='Regiao', Loc='upper left', bbox_to_anchor=(1.05, 1))
plt.xticks(rotation=45)