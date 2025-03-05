import seaborn as sns
import plotly.express as px

print(sns.get_dataset_names())

# 1 - Carregar o dataset Diamonds
data = sns.load_dataset('diamonds')

print(data)

# 2 - Criando gráfico de dispersão interativo com Plotly
fig = px.scatter(
    data,
    x='carat',
    y='price',
    color='cut',
    size='depth',
    hover_data=['x', 'y'],
    title='Dispersão de Diamantes: Peso vs Preço'
)

# 3 - Mostrar gráfico
fig.show()