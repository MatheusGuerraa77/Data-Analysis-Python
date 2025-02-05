import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///pedidos.db')

# 1 - Total de vendas por região

consulta_1 = 'SELECT Regiao, SUM(Unidades) AS Total_Unidades_Vendidas FROM pedidos GROUP BY Regiao'
resultado_1 = pd.read_sql_query(consulta_1, engine)
print('Total de Vendas por região: \n')
print(resultado_1)

# 2 - Vendedor com o maior número de vendas 

consulta_2 =  'SELECT Vendedor, SUM(Unidades) AS Total_Unidades_Vendidas FROM pedidos GROUP BY Vendedor ORDER BY Total_Unidades_Vendidas DESC LIMIT 1'
resultado_2 = pd.read_sql_query(consulta_2, engine)
print(resultado_2)