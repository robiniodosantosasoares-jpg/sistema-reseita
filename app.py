import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sistema Reseita", page_icon="💊", layout="wide")
st.title("💊 Sistema Reseita Doutor - Farmasia")
st.write("Doutor haruka reseita, Farmasia simu no fo remediu. La presiza papel!")

# Guarda lista iha memoria
if "reseitas" not in st.session_state:
    st.session_state.reseitas = []

tab1, tab2, tab3 = st.tabs(["👨‍⚕️ DOUTOR", "🏥 FARMASIA", "📋 LISTA TOMAK"])

# --- TAB DOUTOR ---
with tab1:
    st.header("👨‍⚕️ Doutor - Hakerek Reseita")
    with st.form("form_doutor"):
        naran = st.text_input("Naran Pasiente")
        tinan = st.number_input("Tinan", min_value=0, max_value=120, value=25)
        diagnosa = st.text_input("Diagnosa / Moras")
        remediu = st.selectbox("Remediu", ["Paracetamol", "Amoxicillin", "Vitamina C", "Omeprazole", "Ibuprofen", "Seluk..."])
        remediu_seluk = st.text_input("Se Seluk, hakerek iha ne'e")
        dosis = st.text_input("Dosis / Oin Sa Hemu", placeholder="Ex: 1 tablete, dala 3 loron ida")
        instrusaun = st.text_area("Instrusaun ba Farmasia")
        botao = st.form_submit_button("📤 HARUKA BA FARMASIA", use_container_width=True)
        if botao:
            if naran == "":
                st.error("Hakerek lai naran pasiente!")
            else:
                remediu_final = remediu_seluk if remediu == "Seluk..." else remediu
                st.session_state.reseitas.append({
                    "Data": datetime.now().strftime("%d/%m %H:%M"),
                    "Pasiente": naran,
                    "Tinan": tinan,
                    "Diagnosa": diagnosa,
                    "Remediu": remediu_final,
                    "Dosis": dosis,
                    "Instrusaun": instrusaun,
                    "Status": "⏳ Hei Farmasia"
                })
                st.success(f"Reseita {naran} haruka ona ba Farmasia!")
                st.rerun()

# --- TAB FARMASIA ---
with tab2:
    st.header("🏥 Farmasia - Simu Reseita")
    if len(st.session_state.reseitas) == 0:
        st.info("Seidauk iha reseita. Hein Doutor haruka.")
    else:
        for i, r in enumerate(st.session_state.reseitas):
            with st.expander(f"{r['Status']} - {r['Pasiente']} - {r['Remediu']} - {r['Data']}"):
                st.write(f"**Pasiente:** {r['Pasiente']} ({r['Tinan']} tinan)")
                st.write(f"**Diagnosa:** {r['Diagnosa']}")
                st.write(f"**Remediu:** {r['Remediu']}")
                st.write(f"**Dosis:** {r['Dosis']}")
                st.write(f"**Instrusaun:** {r['Instrusaun']}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ VERIFIED", key=f"v{i}", use_container_width=True):
                        st.session_state.reseitas[i]["Status"] = "✅ Verified"
                        st.rerun()
                with col2:
                    if st.button("💊 DISPENSED / FO ONA", key=f"d{i}", use_container_width=True):
                        st.session_state.reseitas[i]["Status"] = "💊 Dispensed"
                        st.rerun()

# --- TAB LISTA ---
with tab3:
    st.header("📋 Lista Reseita Tomak")
    if len(st.session_state.reseitas) == 0:
        st.info("Lista mamuk hela.")
    else:
        df = pd.DataFrame(st.session_state.reseitas)
        st.dataframe(df, use_container_width=True)
        if st.button("🗑️ Apaga Hotu"):
            st.session_state.reseitas = []
            st.rerun()
