import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st

@st.cache_data
def load_data():
    return generate_data()

def generate_data():
    categories = ['2W', '3W', '4W']
    manufacturers = {
        '2W': ['Hero', 'Honda', 'TVS', 'Bajaj', 'Suzuki'],
        '3W': ['Mahindra', 'Piaggio', 'Bajaj', 'Atul Auto'],
        '4W': ['Maruti', 'Hyundai', 'Tata', 'Mahindra', 'Kia', 'Toyota']
    }

    years = list(range(2020, 2026))
    quarters = ['Q1', 'Q2', 'Q3', 'Q4']
    data = []

    for year in years:
        for quarter in quarters:
            for category in categories:
                for mfg in manufacturers[category]:
                    base = {'2W': 150000, '3W': 30000, '4W': 200000}[category]
                    year_idx = years.index(year)
                    growth_factor = 1.05 ** year_idx
                    seasonality = {'Q1': 1.15, 'Q2': 0.95, 'Q3': 0.90, 'Q4': 1.0}[quarter]
                    mfg_factor = {
                        'Hero': 1.0, 'Honda': 1.1, 'TVS': 0.95, 'Bajaj': 1.05, 'Suzuki': 0.9,
                        'Mahindra': 1.0, 'Piaggio': 1.15, 'Atul Auto': 0.85,
                        'Maruti': 1.2, 'Hyundai': 1.1, 'Tata': 1.15, 'Kia': 1.25, 'Toyota': 0.95
                    }[mfg]
                    randomness = np.random.uniform(0.95, 1.05)
                    reg = int(base * growth_factor * seasonality * mfg_factor * randomness)

                    data.append({
                        'Year': year,
                        'Quarter': quarter,
                        'Quarter_Date': datetime(year, (quarters.index(quarter)*3)+1, 1),
                        'Category': category,
                        'Manufacturer': mfg,
                        'Registrations': reg
                    })

    df = pd.DataFrame(data)
    df.sort_values(by=['Manufacturer', 'Year', 'Quarter'], inplace=True)
    df['QoQ_Growth'] = df.groupby('Manufacturer')['Registrations'].pct_change() * 100
    df['YoY_Growth'] = df.groupby(['Manufacturer', 'Quarter'])['Registrations'].transform(
        lambda x: x.pct_change(periods=4) * 100
    )
    return df
