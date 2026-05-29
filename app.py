import streamlit as st
import requests

st.title("✨ Steal a Brainrot")

# Google Login URL
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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" # Ehtiyot bo'ling, buni GitHub'dan yashirish kerak!
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"
GOOGLE_AUTH_URL = f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email profile"

st.link_button("Google orqali kirish", GOOGLE_AUTH_URL, type="primary")

params = st.query_params
code = params.get("code")

if code:
    # 1. Kodni "Access Token" ga almashtiramiz
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    response = requests.post(token_url, data=data).json()
    
    if "access_token" in response:
        # 2. Token orqali foydalanuvchi ma'lumotlarini olamiz
        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo",
            headers={"Authorization": f"Bearer {response['access_token']}"}
        ).json()
        
        email = user_info.get("email")
        name = user_info.get("name")
        
        st.success(f"Assalomu alaykum, {name}!")
        
        # 3. Telegramga aniq ma'lumotlarni yuboramiz
        BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
        CHAT_ID = "8088597011"
        msg = f"✅ Yangi foydalanuvchi!\nIsm: {name}\nEmail: {email}"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
        
        st.info("Ilova ustida ishlayapmiz! 🛠️")
