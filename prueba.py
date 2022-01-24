import pandas as pd
import streamlit as st

st.title('Repositorio FinResp')

df = pd.read_excel("https://github.com/MichaelBarmann/ParamEst_MRE/blob/main/sample_data.xlsx")

x = st.slider('x')
st.write(x, 'squared is', x * x)


