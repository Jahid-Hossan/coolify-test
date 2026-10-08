import streamlit as st

st.set_page_config(page_title="Coolify Test", page_icon="🎉")

st.title("🎉 Hello from Coolify!")
st.write("This app is running on my Oracle VPS via Coolify.")
st.success("Deployment successful!")

name = st.text_input("What's your name?")
if name:
    st.write(f"Nice to meet you, **{name}**!")