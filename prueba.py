import streamlit as st
import pandas as pd

hoja_calculo_df = pd.read_excel('Tabla.xlsx', sheet_name='Hoja1')

print(hoja_calculo_df)

st.title('Repositorio FinResp')

x = st.slider('x')
st.write(x, 'squared is', x * x)

# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)

BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label])

