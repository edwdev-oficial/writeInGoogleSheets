import pandas as pd
import plotly.express as px
import streamlit as st
import gspread
from datetime import date
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

def carregar_dados(ttl_value):
    conn = st.connection("gsheets", type=GSheetsConnection)
    datas = conn.read(
        worksheet="Página1",
        ttl=ttl_value,
    )
    return datas

cartao = st.selectbox(
   "Cartão",
   ["", "Itaú Platnun", "Itaú Singnature", "Nubank"],
    key="cartao"
)
data = st.date_input("Data", format="DD/MM/YYYY", key="data")
descricao = st.text_input("Descrição", key="descricao")
vencimento = st.date_input("Vencimento", format="DD/MM/YYYY", key="vencimento")
valor = st.text_input("Valor", key="valor")

def salvar():  
    
    valor_atualizado = valor
    valor_formatado = str(valor_atualizado).replace('.', '').replace(',', '.')
    date_obj = data
    data_formatada = date_obj.strftime("%d/%m/%Y")
    vencimento_obj = vencimento
    vencimento_formatado = vencimento_obj.strftime("%d/%m/%Y")
    row = [cartao, data_formatada, descricao, vencimento_formatado, valor_formatado]
    sh.append_row(row)

    # Limpando os inputs
    st.session_state.cartao = ""
    st.session_state['data'] = date.today()
    st.session_state['descricao'] = ""
    st.session_state['vencimento'] = date.today()
    st.session_state['valor'] = ""

if st.button("Salvar", on_click=salvar):
    force_update = True
    df = pd.DataFrame(carregar_dados(0))
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['Vencimento'] = pd.to_datetime(df['Vencimento'], dayfirst=True)
    st.write(df)    
else:
    df = pd.DataFrame(carregar_dados(600))
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['Vencimento'] = pd.to_datetime(df['Vencimento'], dayfirst=True)
    st.write(df)
