import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

from database import salvar_no_postgress


def main():
    st.title("Sistema de CRM e Vendas - Front Simples")
    email = st.text_input(" Email do vendedor")
    data = st.date_input("Data da venda")
    hora = st.time_input("Hora da venda", value=time(9,0))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    qtde = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto",["Zapflow com Gemini", "Zapflow com ChatGPT", "Zapflow com Lhama"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)

            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                qtde = qtde,
                produto= produto
            )

            st.write(venda)
            salvar_no_postgress(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")

        st.write("**Dados da venda**")
        st.write(f" Email do vendedor: {email}")
        st.write(f"Data/hora da venda: {data_hora}")
        st.write(f"Valor da venda: {valor}")
        st.write(f"Quantidade de produtos: {qtde}")
        st.write(f"Produto: {produto}")


if __name__ =="__main__":
    main()