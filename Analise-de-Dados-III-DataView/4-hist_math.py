import matplotlib.pyplot as plt
import numpy as np

# 1 - Dados Fictícios - Pontuações de um teste
pontuacoes = np.random.randint(50, 100, 100)

# 2 - Criando o histograma
plt.figure(figsize=(8, 5))
plt.hist(
    pontuacoes,
    bins=10,
    color='skyblue',
    edgecolor='black'
)

# 3 - Adicionando rótulos e título ao gráfico
plt.xlabel('Pontuação')
plt.ylabel('Frequência')
plt.title('Distribuição da Pontuações do Teste')

plt.show()