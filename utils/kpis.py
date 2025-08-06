import streamlit as st

def display_kpis(filtered_df):
    st.markdown("""<div class="section-title"><h2>Key Performance Indicators</h2></div>""", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    total = filtered_df['Registrations'].sum()
    col1.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Registrations</div>
        <div class="kpi-value">{total:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

    yoy = filtered_df['YoY_Growth'].mean()
    qoq = filtered_df['QoQ_Growth'].mean()
    yoy_status = "positive" if yoy > 0 else "negative"
    qoq_status = "positive" if qoq > 0 else "negative"

    col2.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg. YoY Growth</div>
        <div class="kpi-value">{abs(yoy):.1f}%</div>
        <div class="kpi-growth {yoy_status}">{"▲" if yoy > 0 else "▼"} {yoy:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg. QoQ Growth</div>
        <div class="kpi-value">{abs(qoq):.1f}%</div>
        <div class="kpi-growth {qoq_status}">{"▲" if qoq > 0 else "▼"} {qoq:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

    top = filtered_df.groupby('Manufacturer')['Registrations'].sum().idxmax()
    top_val = filtered_df.groupby('Manufacturer')['Registrations'].sum().max()

    col4.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Leading Manufacturer</div>
        <div class="kpi-value">{top}</div>
        <div class="kpi-growth">{top_val:,.0f} registrations</div>
    </div>
    """, unsafe_allow_html=True)
