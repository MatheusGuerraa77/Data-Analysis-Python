import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.header('Botão')

if st.button('Mensagem'):
    st.write('Olá mundo')
else:
    st.write('Adeus')

st.header('Botão de Download')

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

my_large_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name="large_df.csv",
    mime="text/csv",
)

st.header('utilizando Checkbox')

aceito = st.checkbox('Eu aceito o termo de uso')

if aceito:
    st.write('Parabéns por ter lido os termos de uso')
else:
    st.write('Leia os termos de uso')
    
st.header('Utilizando RadioBox')

genero = st.radio(
    'Qual seu gênero de filme preferido',
    ('Comedia', 'Drama', 'Documentario'))

st.header('utilizando o SelectBox')
opcao = st.selectbox(
    'Escolha a opção para entrar em contato',
    ('Email', 'Fone Residencial', 'Fone Celular'))

st.write('Você selecionou:', opcao)

st.header('Utilizando MultiSelect')

opcoes = st.multiselect(
    'Qual suas cores preferidas',
    ['Green', 'Yellow', 'Red', 'blue'],
    ['Yellow', 'Red']
)

st.write('Você selecionou', opcoes)