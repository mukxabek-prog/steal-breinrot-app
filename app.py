import streamlit as st
import requests

# Sahifa sozlamalari (Dizayn uchun)
st.set_page_config(page_title="Steal a Brainrot", page_icon="🚀")

# Telegram ma'lumotlari
BOT_TOKEN = "8112666081:AAGtROwNttf6lsApMQUxszHoC8xf7rB0s4A"
CHAT_ID = "8088597011"

# UI Dizayn
st.title("✨ Steal a Brainrot")
st.markdown("---")
st.write("Ilovamizga xush kelibsiz! Eng yaxshi brainrotlar shu yerda.")

# Google orqali kirish (simulyatsiya - Streamlitda autentifikatsiya uchun oson yo'l)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    if st.button("Google orqali kirish", type="primary"):
        # Telegramga xabar yuborish
        msg = "✅ Yangi foydalanuvchi tugmani bosdi!"
        requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
        
        st.session_state.logged_in = True
        st.rerun()
else:
    # Muvaffaqiyatli kirgandan keyingi holat
    st.success("Assalomu alaykum!")
    st.balloons() # Chiroyli effekt
    st.info("Ilova ustida ishlayapmiz, tez orada tayyor bo'ladi! 🛠️")
