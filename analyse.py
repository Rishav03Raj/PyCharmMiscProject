import streamlit as st
import pandas as pd

DATA_FILE = "portfolio_data.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def render_analyze():
    st.title("📊 Analyze Portfolio")

    df = load_data()
    if df.empty:
        st.info("No data available yet. Add some entries to get started.")
        return

    # Total P/L
    st.subheader("🔢 Total Portfolio Summary")
    total_pl = df['P/L'].sum()
    st.metric("Total Realised P/L (All Users, All Accounts)", f"₹{total_pl:,.2f}")

    # Per-person analysis
    st.subheader("📁 Individual Portfolio Summary")
    selected_name = st.selectbox("Select Person", df['Name'].unique())
    filtered = df[df['Name'] == selected_name]
    summary = filtered.groupby('Share')['P/L'].sum().reset_index()
    st.dataframe(summary)

    total = filtered['P/L'].sum()
    st.markdown(f"**Total Realised P/L for {selected_name}:** ₹{total:,.2f}")

    if st.sidebar.button("🏠 Back to Home"):
        st.query_params["page"] = "home"
        st.rerun()

    if st.sidebar.button("📤 Go to Update"):
        st.query_params["page"] = "update"
        st.rerun()
