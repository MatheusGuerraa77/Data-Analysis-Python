import pandas as pd

# Caminho para o arquivo Excel
caminho_arquivo = 'data1/livros.xlsx'
df = pd.read_excel(caminho_arquivo)

print(df)


# 1 -Visão geral dos dados
print(df.head())
print(df.tail())

# 2 -Verificando tipos de dados
print(df.dtypes)

# 3 -Estatísticas Descritivas
print(df.describe())
print(df[['Preço (R$)', 'Quantidade']].describe())