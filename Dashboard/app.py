import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1-Importando os Dados
data = pd.read_csv("Dashboard/data/Pedidos.csv")
df = pd.DataFrame(data)

def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    
    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
    with aba1:
        display_dataframe(df)
    with aba2:
        pass
    with aba3:
        pass
#Função para exibir o DataFrame
def display_dataframe(data):
    st.header("Visualização do DataFrame")
    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data['Regiao'].unique(),
        data['Regiao'].unique()
    )
    filtered_data = data[data['Regiao'].isin(selected_region)]
    st.write(filtered_data)
    
# Execução do aplicativo
if __name__ == "__main__":
    main()