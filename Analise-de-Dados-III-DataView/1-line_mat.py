import matplotlib.pyplot as plt

# 1 - Dados fictícios - Vendas ao longo dos meses
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
vendas = [150, 200, 180, 300, 250, 400]

# 2 - Criando o gráfico de linha 
plt.figure(figsize=(8, 5))
plt.plot(
    meses,
    vendas,
    marker='o',
    linestyle='-',
    color='blue',
    label='Vendas'
)

# 3 - Adicionando rótulos e título ao gráfico
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Vendas ao longo dos Meses')
plt.legend()
plt.grid(True)

# 4 - Exibindo o gráfico
plt.show()