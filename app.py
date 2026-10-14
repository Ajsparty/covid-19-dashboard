# quick covid dashboard demo
# still just sample data, haven't hooked up the real jhu csv yet

import streamlit as st
import pandas as pd

st.set_page_config(page_title="COVID-19 Analytics Dashboard", layout="wide")
st.title("COVID-19 Global Analytics Dashboard")
st.caption("demo version")

st.info("Sample data only for now. Real version would pull from the Johns Hopkins repo and do maps + time series.")

if st.button("Load Sample Data"):
    df = pd.DataFrame({
        'Country': ['USA', 'India', 'Brazil', 'France', 'Germany'],
        'Confirmed': [103000000, 45000000, 38000000, 41000000, 39000000],
        'Deaths': [1120000, 530000, 710000, 170000, 180000]
    })
    st.dataframe(df)
    st.bar_chart(df.set_index('Country')['Confirmed'])