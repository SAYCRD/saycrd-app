import streamlit as st

st.title("🔹 SAYCRD – Sacred Reflection Engine")
st.write("This is your ceremonial engine. Enter your truth below.")

user_input = st.text_area("Speak your truth:")
if st.button("Reflect"):
    st.write("You said:", user_input)
