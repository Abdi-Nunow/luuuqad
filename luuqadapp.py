# 📄 app.py
import streamlit as st
import requests
import urllib.parse

st.title("kaliga is bar")
st.write("Ku qor erayo ama jumlado, dooro luqadda aad rabto, oo riix Turjum!")

# Geli qoraalka
input_text = st.text_area("Geli erayo ama jumlado:", "")

# Luqadaha la heli karo
languages = {
    'Ingiriisi': 'en',
    'Isbaanish': 'es',
    'Faransiis': 'fr',
    'Carabi': 'ar',
    'Somali': 'so',
    'Jarmal': 'de'
}
target_lang = st.selectbox("Dooro luqadda loo turjumayo:", list(languages.keys()))

if st.button("🔄 Turjum"):
    if input_text.strip() == "":
        st.warning("Fadlan geli qoraalka aad rabto.")
    else:
        encoded_text = urllib.parse.quote(input_text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={languages[target_lang]}&dt=t&q={encoded_text}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            translated = response.json()[0][0][0]
            st.success(f"**Natiijada:** {translated}")
        except Exception as e:
            st.error(f"Turjumaaddu ma shaqeyn: {e}")
