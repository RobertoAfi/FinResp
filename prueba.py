import pandas as pd
import streamlit as st

st.title('Repositorio FinResp')

data = pd.read_csv("Tabla.csv")

x = st.slider('x')
st.write(x, 'squared is', x * x)


