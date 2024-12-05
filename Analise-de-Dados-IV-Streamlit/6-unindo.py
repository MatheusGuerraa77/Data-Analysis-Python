import streamlit as st
import pandas as pd
import altair as alt

# Carregar o conjunto de dados Iris
iris_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

st.title("Dashbord com Dados Íris")
st.write("Este Dashboard apresenta informações sobre as espécies Íris")

#Obter as espécies únicas de íris para criar um seletor
species_list = iris_df["species"].unique()
selected_species = st.selectbox("Selecione a espécie de Íris", species_list)

#Filtrar o DataFrame com base na espécie selecionada
filtered_data = iris_df[iris_df["species"] == selected_species]

#Criar um gráfico de dispersão interativo com Altair
scatter_chart = alt.Chart(filtered_data).mark_circle().encode(
    x='sepal_length',
    y='sepal_width',
    color='species',
    tooltip=['species', 'sepal_length', 'sepal_width']
).properties(
    width=600,
    height=400
).interactive()

#Exibir o gráfico
st.altair_chart(scatter_chart, use_container_width=True)