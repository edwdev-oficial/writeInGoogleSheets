import pandas as pd
import plotly.express as px
import streamlit as st
import gspread
from google.oauth2 import service_account
from streamlit_gsheets import GSheetsConnection


st.set_page_config(layout='wide')
st.title('Carregar Dados, Ler e Editar Planilha Google Sheets')

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client=gspread.authorize(credentials)
sh = client.open('editplan').worksheet('Página1')

conn = st.connection("gsheets", type=GSheetsConnection)
datas = conn.read(
    worksheet="Página1",
    ttl=0,
)
df = pd.DataFrame(datas)

cartao = st.text_input("Cartao", key="cartao")
data = st.text_input("Data", key="data")
descricao = st.text_input("Descrição", key="descricao")
vencimento = st.text_input("Vencimento", key="vencimento")
valor = st.text_input("Valor", key="valor")

def salvar():  
    
    valor_atualizado = valor
    valor_formatado = str(valor_atualizado).replace('.', '').replace(',', '.')
    row = [cartao, data, descricao, vencimento, valor_formatado]
    sh.append_row(row)

    # Limpando os inputs
    st.session_state['cartao'] = ""
    st.session_state['data'] = ""
    st.session_state['descricao'] = ""
    st.session_state['vencimento'] = ""
    st.session_state['valor'] = ""

st.button("Salvar", on_click=salvar)
df['data'] = pd.to_datetime(df['data'], dayfirst=True)
df['Vencimento'] = pd.to_datetime(df['Vencimento'], dayfirst=True)
st.write(df)
