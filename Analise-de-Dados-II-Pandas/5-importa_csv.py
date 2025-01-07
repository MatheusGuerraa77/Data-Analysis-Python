import pandas as pd

# 1 - Importando dataset com delimitador vírgula
df = pd.read_csv('data1/pedidos.csv')
print(df)
print(type(df))

# 2 - Importando dataset com delimitador ponto e vírgula
df2 = pd.read_csv('data1/pedidos2.csv', sep=';')
print(df2)

# 3 - Lê primeiros registros
print(df.head(10))

# 4 - Lê últimos registros
print(df.tail())

print(df.shape)

print(df.dtypes)

# 5 - Ordenação de Valores
print(df.sort_values(by='Unidades', ascending=False))

# 6 - Estados com mais vendas
print(df['Estado'].value_counts())