import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def show_growth_trends(filtered_df):
    st.markdown("""<div class="section-title"><h2>Growth Trends</h2></div>""", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Quarterly Trend", "Category Comparison"])

    with tab1:
        df = filtered_df.groupby(['Year', 'Quarter', 'Quarter_Date'])['Registrations'].sum().reset_index()
        fig = px.line(df, x='Quarter_Date', y='Registrations', markers=True)
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        df = filtered_df.groupby(['Year', 'Category'])['Registrations'].sum().reset_index()
        fig = px.bar(df, x='Year', y='Registrations', color='Category', barmode='group')
        fig.update_layout(height=450)
        st.plotly_chart(fig, use_container_width=True)

def show_manufacturer_performance(filtered_df):
    st.markdown("""<div class="section-title"><h2>Manufacturer Performance</h2></div>""", unsafe_allow_html=True)
    df = filtered_df.groupby(['Manufacturer', 'Category']).agg(
        Total=('Registrations', 'sum'),
        YoY=('YoY_Growth', 'mean'),
        QoQ=('QoQ_Growth', 'mean')
    ).reset_index()

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns), fill_color='blue', font=dict(color='white')),
        cells=dict(values=[df[c] for c in df.columns])
    )])
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def show_growth_analysis(filtered_df):
    st.markdown("""<div class="section-title"><h2>Growth Analysis</h2></div>""", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        top = filtered_df.groupby('Manufacturer')['YoY_Growth'].mean().nlargest(5).reset_index()
        top['Growth'] = top['YoY_Growth'].apply(lambda x: f"{x:.1f}%")
        fig = px.bar(top, x='Growth', y='Manufacturer', orientation='h', text='Growth')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        df = filtered_df.groupby('Manufacturer').agg(
            YoY=('YoY_Growth', 'mean'),
            QoQ=('QoQ_Growth', 'mean'),
            Total=('Registrations', 'sum')
        ).reset_index()
        fig = px.scatter(df, x='YoY', y='QoQ', size='Total', color='Manufacturer')
        st.plotly_chart(fig, use_container_width=True)
