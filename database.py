import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def salvar_no_postgress(dados: Vendas):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()

        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, qtde, produto) VALUES (%s,%s,%s,%s,%s)"
        )

        cursor.execute(insert_query,(
            dados.email,
            dados.data,
            dados.valor,
            dados.qtde,
            dados.produto.value
        ))

        conn.commit()
        cursor.close()
        conn.close()

        st.success("Dados inseridos com sucesso!")
    except Exception as e:
        st.error(f"Erro ao salvar os dados no banco: {e}")