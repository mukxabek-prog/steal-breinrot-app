import streamlit as st
from streamlit_oauth import OAuthComponent # Aynan shu nom bilan import qilinadi
import requests
import json

# Telegram konfiguratsiyasi
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"

st.title("✨ Steal a Brainrot")

# OAuth sozlamalari
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"

# Komponentni yaratish va chaqirish
oauth2 = OAuthComponent(
    "google",
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI,
    "openid email profile"
)

result = oauth2.authorize_button("Google orqali kirish", "primary")

if result:
    st.success("Assalomu alaykum!")
    # Telegramga ma'lumot yuborish
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Yangi kirish!")
    st.info("Ilova ustida ishlayapmiz, tez orada tayyor bo'ladi! 🛠️")
