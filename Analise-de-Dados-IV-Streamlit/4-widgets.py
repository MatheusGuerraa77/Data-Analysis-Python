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

st.header('Utilizando o Slider')

idade = st.slider('Quantos anos você tem?', 0, 100, 25)
st.write('Eu tenho', idade, 'anos de idade')

st.header('utilizando o Select Slider')

cor = st.select_slider(
    'Selecione a cor',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favourite color is', cor)

import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)