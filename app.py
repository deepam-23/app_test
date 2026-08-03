import streamlit as st
st.title("My first streamlit app")
name=st.text_input("Enter your name")
if st.button("Submit"):
  st.write(f"Hello,{name}")
