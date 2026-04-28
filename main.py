import streamlit as st

# 1. State Management (To handle clicking the icons)
if 'page' not in st.session_state:
    st.session_state.page = "HOME"

# 2. THE CSS SOLUTION (This makes the icons look like apps)
st.markdown("""
    <style>
    /* The Square Container */
    .app-card {
        background-color: white;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: transform 0.3s ease;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 180px;
    }
    .app-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-color: #4e73df;
    }
    .app-icon {
        font-size: 50px;
        margin-bottom: 10px;
    }
    .app-title {
        font-weight: bold;
        color: #333;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HOME PAGE ---
if st.session_state.page == "HOME":
    st.title("🤝 Cohelp AI Dashboard")
    st.write("Welcome back, Harshid. Select a tool to begin.")
    
    # Create 2 columns for the square grid
    col1, col2 = st.columns(2)

    with col1:
        # Square 1: PPT
        st.markdown('<div class="app-card"><div class="app-icon">🪄</div><div class="app-title">Prompt to PPT</div></div>', unsafe_allow_html=True)
        if st.button("Open PPT Maker", key="ppt", use_container_width=True):
            st.session_state.page = "PPT"
            st.rerun()

    with col2:
        # Square 2: Email
        st.markdown('<div class="app-card"><div class="app-icon">✉️</div><div class="app-title">Email Pro</div></div>', unsafe_allow_html=True)
        if st.button("Open Email Writer", key="email", use_container_width=True):
            st.session_state.page = "EMAIL"
            st.rerun()

    col3, col4 = st.columns(2)

    with col3:
        # Square 3: PDF
        st.markdown('<div class="app-card"><div class="app-icon">📄</div><div class="app-title">Photo to PDF</div></div>', unsafe_allow_html=True)
        if st.button("Open Scanner", key="pdf", use_container_width=True):
            st.session_state.page = "PDF"
            st.rerun()

    with col4:
        # Square 4: Data
        st.markdown('<div class="app-card"><div class="app-icon">📊</div><div class="app-title">Data Analysis</div></div>', unsafe_allow_html=True)
        if st.button("Open Analysis", key="data", use_container_width=True):
            st.session_state.page = "DATA"
            st.rerun()

# --- OTHER PAGES ---
elif st.session_state.page == "PPT":
    st.button("⬅️ Back Home", on_click=lambda: st.session_state.update({"page": "HOME"}))
    st.header("🪄 Prompt to PPT Creator")
    # Add your PPT code here...

# (Repeat for other pages...)
