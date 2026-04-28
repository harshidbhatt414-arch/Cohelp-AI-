import streamlit as st

# 1. State Management
if 'page' not in st.session_state:
    st.session_state.page = "HOME"

# 2. THE CSS SOLUTION (Beautiful Square Cards with no personal names)
st.markdown("""
    <style>
    .app-card {
        background-color: white;
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border: 1px solid #f0f0f0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-bottom: 10px;
    }
    .icon-box {
        font-size: 55px;
        margin-bottom: 15px;
    }
    .title-box {
        font-weight: 700;
        font-size: 20px;
        color: #1c1c1c;
    }
    /* Style for the button under the card */
    .stButton>button {
        border-radius: 12px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == "HOME":
    st.title("🤝 Cohelp AI Dashboard")
    # REMOVED THE NAME HERE
    st.subheader("Welcome! Select a tool to empower your business.")
    st.write("---")
    
    # Grid Layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="app-card"><div class="icon-box">🪄</div><div class="title-box">Prompt to PPT</div></div>', unsafe_allow_html=True)
        if st.button("Launch PPT Maker", key="btn_ppt", use_container_width=True):
            st.session_state.page = "PPT"
            st.rerun()

    with col2:
        st.markdown('<div class="app-card"><div class="icon-box">✉️</div><div class="title-box">AI Email Pro</div></div>', unsafe_allow_html=True)
        if st.button("Launch Email Writer", key="btn_email", use_container_width=True):
            st.session_state.page = "EMAIL"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="app-card"><div class="icon-box">📄</div><div class="title-box">Photo to PDF</div></div>', unsafe_allow_html=True)
        if st.button("Launch Scanner", key="btn_pdf", use_container_width=True):
            st.session_state.page = "PDF"
            st.rerun()

    with col4:
        st.markdown('<div class="app-card"><div class="icon-box">📊</div><div class="title-box">Data Analysis</div></div>', unsafe_allow_html=True)
        if st.button("Launch Analysis", key="btn_data", use_container_width=True):
            st.session_state.page = "DATA"
            st.rerun()

# --- BACK BUTTON LOGIC (Put this at the top of your other pages) ---
# if st.button("⬅️ Back to Apps"):
#     st.session_state.page = "HOME"
#     st.rerun()
