import pandas as pd

#1-Dados Fictícios (Livros)
dados = {
    'Título':['Aventuras no Espaço', 'O Mistério do Castelo', 'História Antiga', 'A Arte da Guerra'],
    'Autor':['João Silva', 'Maria Santos', 'Pedro Oliveira', 'Ana Costa'],
    'Gênero':['Ficção Científica', 'Mistério', 'História', 'Filosofia'],
    'Ano de Publicação':[2015, 2018, 2016, 2014],
    'Preço (R$)':[25.50, 19.99, 30.00, 15.75],
    'Quantidade':[100, 85, 120, 150]
}

#2-Criando o Dataframe
df = pd.DataFrame(dados)

print(df)

#3-Exportando para Planilha Excel
nome_arquivo = 'data1/livros.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f'Arquivo {nome_arquivo} criado com sucesso!')