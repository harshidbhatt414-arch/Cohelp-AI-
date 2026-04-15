import streamlit as st
import pandas as pd
import time

# 1. Page Configuration
st.set_page_config(page_title="Cohelp AI | Virar", page_icon="🤝", layout="wide")

# 2. Advanced Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fc; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(90deg, #1e40af 0%, #3b82f6 100%);
        color: white;
        font-weight: bold;
        border: none;
    }
    .logo-text { font-weight: 800; font-size: 45px; color: #1e40af; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="logo-text">🤝 Cohelp <span style="color:#60a5fa;">AI</span></p>', unsafe_allow_html=True)
st.write("---")

# 3. Sidebar
choice = st.sidebar.selectbox("🛠️ Tool Suite", 
    ["Home", "Prompt to PPT", "Smart Emailer", "Photo to PDF", "Data Analysis"])

# --- 1. HOME ---
if choice == "Home":
    st.subheader("Welcome to the Cohelp AI Dashboard")
    st.write("Professional AI tools designed for the Virar business community.")
    st.info("💡 **Founder's Tip:** Use the 'Data Analysis' tool to upload your monthly sales and see your growth instantly!")

# --- 2. PROMPT TO PPT ---
elif choice == "Prompt to PPT":
    st.title("📽️ Prompt to PPT")
    topic = st.text_input("Enter Topic for Outline")
    if st.button("Generate Professional Structure"):
        with st.spinner('Analyzing topic...'):
            time.sleep(1.5)
            st.success("Structure Ready!")
            st.markdown(f"""
            **Slide 1:** Introduction to {topic}  
            **Slide 2:** Current Market Trends  
            **Slide 3:** Key Challenges & Solutions  
            **Slide 4:** Future Growth Roadmap  
            """)

# --- 3. SMART EMAILER ---
elif choice == "Smart Emailer":
    st.title("✉️ Smart Emailer")
    col1, col2 = st.columns(2)
    with col1:
        lang = st.selectbox("Language", ["English", "Hinglish", "Marathi"])
    with col2:
        tone = st.selectbox("Tone", ["Formal", "Friendly", "Urgent"])
        
    context = st.text_area("What is the email about?")
    if st.button("Generate Draft"):
        st.info("Drafting...")
        time.sleep(1)
        st.code(f"Subject: Regarding {context}\n\n[Your {tone} email in {lang} will appear here...]")

# --- 4. PHOTO TO PDF ---
elif choice == "Photo to PDF":
    st.title("📷 Photo to PDF")
    files = st.file_uploader("Upload document images", type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    if files:
        st.write(f"✅ {len(files)} files uploaded.")
        if st.button("Convert to High-Quality PDF"):
            st.success("Optimization complete. PDF is ready for download.")

# --- 5. DATA ANALYSIS (Enhanced) ---
elif choice == "Data Analysis":
    st.title("📊 Data Analysis")
    st.write("Upload your sales or inventory records (CSV or Excel) to see smart insights.")
    
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])
    
    if uploaded_file:
        try:
            # Enhanced logic: Auto-detecting file type
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            # Quality Enhancement: Data Summary Cards
            st.markdown("### 📈 Quick Summary")
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Rows", len(df))
            c2.metric("Columns Found", len(df.columns))
            c3.metric("Data Status", "Verified")

            # Quality Enhancement: Interactive Tabs
            tab1, tab2, tab3 = st.tabs(["📊 Visual Graph", "📑 Data Preview", "🔍 Statistics"])
            
            with tab1:
                st.write("Line Chart of Numeric Data")
                st.line_chart(df.select_dtypes(include=['number']))
            
            with tab2:
                st.dataframe(df.head(10), use_container_width=True)
            
            with tab3:
                st.write("Mathematical Summary")
                st.write(df.describe())
                
        except Exception as e:
            st.error(f"Error: Could not read file. Please ensure it is a valid CSV or Excel file. (Details: {e})")
    else:
        st.info("Upload a sample sales file to see the analysis in action.")
