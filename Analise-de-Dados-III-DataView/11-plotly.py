import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'StockA': [100 + i for i in range(100)],
    'StockB': [120 - i for i in range(100)],
    'StockC': [90 + (i *0.5) for i in range(100)],
}

df = pd.DataFrame(data)
print(df)

# 2 - Criando o gráfico de linhas interativas com Plotly

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockA'],
    mode='lines',
    name='Stock A'
))
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockB'],
    mode='lines',
    name='Stock B'
))
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['StockC'],
    mode='lines',
    name='Stock C'
))

# 3 - Layout do gráfico

fig.update_layout(
    title='Variação de Preço ao longo do tempo',
    xaxis_title = 'Data',
    yaxis_title = 'Preço',
    hovermode='x'
)

fig.show()