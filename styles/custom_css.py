import streamlit as st

def inject_css():
    st.markdown("""
    <style>
        .stApp { background-color: #f8f9fa; }
        .header {
            background: linear-gradient(135deg, #1e5799, #207cca);
            color: white;
            padding: 1.5rem 1rem;
            border-radius: 0 0 15px 15px;
        }
        .kpi-card {
            background: white;
            border-radius: 10px;
            padding: 15px;
            text-align: center;
            height: 120px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        .kpi-title { color: #6c757d; font-size: 1rem; }
        .kpi-value { font-size: 1.8rem; font-weight: 700; color: #333; }
        .kpi-growth { font-size: 0.9rem; font-weight: 600; }
        .positive { color: #28a745; }
        .negative { color: #dc3545; }
        .section-title { border-left: 4px solid #1e5799; padding-left: 10px; color: #333; margin-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)
