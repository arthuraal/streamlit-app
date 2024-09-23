import streamlit as st

st.title("App Otimizado para Celular")

# Ajustar o layout para caber em telas pequenas
st.text("Este app é acessível em dispositivos móveis!")

# Campos de entrada maiores para facilitar a interação no celular
name = st.text_input("Digite seu nome", max_chars=20)
st.write(f"Olá, {name}!")

# Botões maiores para facilitar a interação
if st.button("Clique Aqui"):
    st.write("Botão clicado!")
