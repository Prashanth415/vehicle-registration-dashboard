import streamlit as st
from data.generator import load_data
from utils.kpis import display_kpis
from utils.plots import show_growth_trends, show_manufacturer_performance, show_growth_analysis
from styles.custom_css import inject_css

# Configure Streamlit page
st.set_page_config(
    page_title="Vehicle Registration Analytics",
    page_icon="🚗",
    layout="wide"
)

# Inject CSS
inject_css()

# Load Data
df = load_data()

# Header
st.markdown("""
<div class="header">
    <h1>Vehicle Registration Analytics</h1>
    <h3>Investor-focused insights into vehicle registration trends in India</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("Dashboard Filters")
years = sorted(df['Year'].unique())
selected_years = st.sidebar.slider("Select Year Range", min_value=min(years), max_value=max(years), value=(2023, 2025))
categories = df['Category'].unique()
selected_categories = st.sidebar.multiselect("Vehicle Categories", options=categories, default=categories)
manufacturers = st.sidebar.multiselect(
    "Manufacturers", 
    options=df['Manufacturer'].unique(), 
    default=['Maruti', 'Hero', 'Mahindra', 'Tata', 'Honda']
)

# Filtered Data
filtered_df = df[
    (df['Year'].between(selected_years[0], selected_years[1])) &
    (df['Category'].isin(selected_categories)) &
    (df['Manufacturer'].isin(manufacturers))
]

# Display sections
display_kpis(filtered_df)
show_growth_trends(filtered_df)
show_manufacturer_performance(filtered_df)
show_growth_analysis(filtered_df)

# Footer
st.markdown("---")
st.caption("**Data Source**: Simulated Vahan Dashboard | **Disclaimer**: Synthetic data for demonstration.")
