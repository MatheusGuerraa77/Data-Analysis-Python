import matplotlib.pyplot as plt

# 1 - Dados Fictícios - Quantidade de Produtos vendidos por vendedor

vendedores = ['João', 'Maria', 'Pedro', 'Ana']
quantidade_vendida = [45, 60, 30, 55]

# 2 - Criando o gráfico de barras
plt.figure(figsize=(8,5))
plt.bar(
    vendedores,
    quantidade_vendida,
    color='green'
)

# 3 - Adicionando rótulos e título ao gráfico
plt.xlabel('Vendedores')
plt.ylabel('Quantidade vendida')
plt.title('Quantidade de Produtos Vendidos por Vendedor')



# 4 - Exibir Gráfico
plt.show()