import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="🌍 AI Translator & Is-barasho", layout="centered")

st.title("🌍 AI Translator Tool & Is-barasho")
st.write("Ku qor erayo/jumlado, dooro luqadda aad rabto, oo turjum. Sidoo kale, dadka kale la baro!")

# Geli qoraalka turjumaada
st.header("🔄 Qaybta Turjumaada")
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

if st.button("Turjum"):
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

# 🔗 Qaybta Is-barasho (Community)
st.header("👥 Qaybta Is-barasho")
st.write("Ku qor magacaaga, wadanka aad joogto, iyo WhatsApp number si dadka kale ula xiriiraan.")

# Foomka is-barasho
with st.form("isbarasho_form"):
    name = st.text_input("Magacaaga:")
    country = st.text_input("Wadanka aad joogto:")
    whatsapp = st.text_input("WhatsApp Number:")
    my_lang = st.selectbox("Luqadda aad ku hadasho:", list(languages.keys()))
    submitted = st.form_submit_button("Ku dar liiska")

    if submitted and name.strip() and country.strip() and whatsapp.strip():
        # Ku keydi liiska session_state
        if "community" not in st.session_state:
            st.session_state.community = []
        st.session_state.community.append({
            'name': name,
            'country': country,
            'whatsapp': whatsapp,
            'lang': my_lang
        })
        st.success(f"**{name}** oo jooga **{country}** (WhatsApp: {whatsapp}) ayaa la diiwaan geliyay!")

# Muuji dadka is-barashada
if "community" in st.session_state and st.session_state.community:
    st.subheader("📜 Dadka Ku Jira Liiska:")
    for person in st.session_state.community:
        st.markdown(f"- **{person['name']}** ({person['country']}) | 📞 WhatsApp: `{person['whatsapp']}` | 💬 Luqad: {person['lang']}")
else:
    st.info("Liiska weli waa madhan. Noqo qofka ugu horeeya!")

