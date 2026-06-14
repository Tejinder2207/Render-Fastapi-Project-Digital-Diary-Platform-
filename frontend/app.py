import streamlit as st
import requests
from datetime import date

API = "http://127.0.0.1:8000"

# Page config
st.set_page_config(page_title="Digital Diary", page_icon="📔", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    .title {
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>📔 Digital Diary Platform</h1>", unsafe_allow_html=True)

# Layout: 2 columns
col1, col2 = st.columns([1, 2])

# LEFT SIDE → Add Entry
with col1:
    st.markdown("### ✍️ Add New Entry")

    title = st.text_input("Title")
    content = st.text_area("Write your thoughts...")
    entry_date = st.date_input("Date", date.today())

    if st.button("💾 Save Entry"):
        res = requests.post(f"{API}/entries", json={
            "title": title,
            "content": content,
            "date": str(entry_date)
        })

        if res.status_code == 200:
            st.success("✅ Entry Saved!")
        else:
            st.error("❌ Error saving entry")

# RIGHT SIDE → Show Entries
with col2:
    st.markdown("### 📚 Your Entries")

    entries = requests.get(f"{API}/entries").json()

    if not entries:
        st.info("No entries yet. Start writing!")
    else:
        for e in entries:
            st.markdown(f"""
                <div class="card">
                    <h3>{e['title']}</h3>
                    <p><i>{e['date']}</i></p>
                    <p>{e['content']}</p>
                </div>
            """, unsafe_allow_html=True)

            if st.button("🗑 Delete", key=e["id"]):
                requests.delete(f"{API}/entries/{e['id']}")
                st.rerun()