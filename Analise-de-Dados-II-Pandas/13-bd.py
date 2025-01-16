import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("sqlite:///pedidos.db")

df = pd.read_csv('data1/Pedidos.csv')

# 1 - Exportando para tabela
df.to_sql('pedidos', engine, index=False)