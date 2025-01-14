import pandas as pd

caminho_arquivo = 'data1/livros.xlsx'
df = pd.read_excel(caminho_arquivo)
print(df)

# 1 - Gênero- Quantidade de livros e preço médio por gênero
genero_info = df.groupby('Gênero').agg({
    'Título': 'count',
    'Preço (R$)': 'mean'
})
print(genero_info)

# 2 - livro mais caro e mais barato
livro_mais_caro = df[df['Preço (R$)'] == df['Preço (R$)'].max()]
livro_mais_barato = df[df['Preço (R$)'] == df['Preço (R$)'].min()]
print(livro_mais_caro)
print(livro_mais_barato)

# 3 - Distribuição de Ano de Publicação
print(df['Ano de Publicação'].value_counts())

# 4 - Relação entre preço e quantidade
correlacao = df['Preço (R$)'].corr(df['Quantidade'])
print(correlacao)