import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.set_page_config(layout='wide')
st.title('Carregar Dados, Ler e Editar Planilha Google Sheets')

conn = st.connection("gsheets", GSheetsConnection)
data = conn.read(
    worksheet="Página1",
    ttl=0
)
df = pd.DataFrame(data)



df