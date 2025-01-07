import pandas as pd

# 1 - Importando dataset com delimitador vírgula
df = pd.read_csv('data1/pedidos.csv')
print(df)
print(type(df))

# 2 - Importando dataset com delimitador ponto e vírgula
df2 = pd.read_csv('data1/pedidos2.csv', sep=';')
print(df2)