#vibecoding - programar copiloto - IA Generativa

#procode - programação convecioanal

#procoding 

import streamlit as st
import pandas as pd 


st.title("Minha web page")

dados = pd.read_csv('dados.csv')
df = pd.DataFrame(dados)
st.write(dados)
st.image("img.png")

#gráficos

st.line_chart(df, x = "vendedor", y = "vendas")

st.map()

