import streamlit as st
import pandas as pd
from pathlib import Path

caminho_compras = Path(__file__).parent / 'datasets/compras.csv'
print(caminho_compras)

df_compras = pd.read_csv(caminho_compras, sep=";", decimal=",")

st.dataframe(df_compras)