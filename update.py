import streamlit as st
import pandas as pd
import os
import hashlib

DATA_FILE = "portfolio_data.csv"

if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Name", "Account", "Month", "Share", "P/L", "Upload_ID"]).to_csv(DATA_FILE, index=False)

def load_data():
    return pd.read_csv(DATA_FILE)

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def render_update():
    st.title("🔄 Update Portfolio Data")

    df = load_data()

    st.subheader("Add or Upload Data")
    method = st.radio("Input Method", ["Manual", "Upload"])

    if method == "Manual":
        name = st.selectbox("Name", ["Rishav", "Mom", "Sister", "Papa", "Friend1", "Friend2"])
        account = st.selectbox("Account", ["Groww", "Neo", "Other"])
        month = st.selectbox("Month", pd.date_range('2023-01-01', periods=12, freq='MS').strftime('%B'))
        share = st.text_input("Share Name")
        pl = st.number_input("Profit/Loss", step=100.0)
        if st.button("Add Entry"):
            df = pd.concat([
                df,
                pd.DataFrame([[name, account, month, share, pl, "manual"]], columns=df.columns)
            ], ignore_index=True)
            save_data(df)
            st.success("Entry added")

    else:
        name = st.selectbox("Name", ["Rishav", "Mom", "Sister", "Papa", "Friend1", "Friend2"])
        account = st.selectbox("Account", ["Groww", "Neo", "Other"])
        month = st.selectbox("Month", pd.date_range('2023-01-01', periods=12, freq='MS').strftime('%B'))
        uploaded = st.file_uploader("Upload Excel", type=['xlsx', 'xls'])

        if uploaded:
            file_hash = hashlib.md5(uploaded.getvalue()).hexdigest()
            if 'Upload_ID' in df.columns and file_hash in df['Upload_ID'].astype(str).values:
                st.warning("This file has already been uploaded. Skipping duplicate upload.")
            else:
                try:
                    xls = pd.ExcelFile(uploaded)
                    sheet = xls.parse(xls.sheet_names[0], header=None)
                    header_row_idx = None
                    for i, row in sheet.head(20).iterrows():
                        if row.astype(str).str.contains('Stock name', case=False, na=False).any() and \
                           row.astype(str).str.contains('Realised P&L', case=False, na=False).any():
                            header_row_idx = i
                            break
                    if header_row_idx is None:
                        raise ValueError("Header row with 'Stock name' not found.")

                    sheet = xls.parse(xls.sheet_names[0], header=header_row_idx)
                    sheet.columns = [str(c).strip() for c in sheet.columns]
                    columns_lower = [c.lower().strip() for c in sheet.columns]

                    if 'stock name' not in columns_lower or 'realised p&l' not in columns_lower:
                        raise ValueError(f"Required columns not found. Found: {list(sheet.columns)}")

                    col_map = {c.lower().strip(): c for c in sheet.columns}
                    df_text = sheet.astype(str)
                    unreal_idxs = df_text[df_text.apply(
                        lambda row: row.str.contains('Unrealised', na=False, case=False).any(), axis=1
                    )].index
                    end_idx = unreal_idxs[0] if len(unreal_idxs) else len(sheet)

                    realised_df = sheet.iloc[:end_idx][[col_map['stock name'], col_map['realised p&l']]].copy()
                    realised_df.columns = ['Share', 'P/L']
                    realised_df['P/L'] = pd.to_numeric(realised_df['P/L'], errors='coerce').fillna(0)
                    summary = realised_df.groupby('Share')['P/L'].sum().reset_index()

                    charges_section = sheet.iloc[:header_row_idx].astype(str)
                    total_charges = 0.0
                    for _, row in charges_section.iterrows():
                        if row.str.contains('Total Charges', case=False, na=False).any():
                            for i in range(len(row) - 1):
                                if 'total charges' in str(row[i]).lower():
                                    try:
                                        total_charges = float(str(row[i + 1]).replace(',', '').strip())
                                    except:
                                        total_charges = 0.0
                                    break
                            break

                    st.subheader("Upload Preview")
                    st.dataframe(summary)
                    st.markdown(f"**Total Charges:** ₹{total_charges:,.2f}")
                    net_pl = summary['P/L'].sum() - total_charges
                    st.markdown(f"**Net Profit (after charges):** ₹{net_pl:,.2f}")

                    if st.button("Confirm Upload"):
                        for _, r in summary.iterrows():
                            df = pd.concat([
                                df,
                                pd.DataFrame([[name, account, month, r['Share'], r['P/L'], file_hash]], columns=df.columns)
                            ], ignore_index=True)
                        save_data(df)
                        st.success("File processed and data saved.")
                except Exception as e:
                    st.error(f"File error: {e}")

    reset_name = st.selectbox("Select Name to Reset", ["Rishav", "Mom", "Sister", "Papa", "Friend1", "Friend2"], key="reset_name")
    reset_account = st.selectbox("Select Account to Reset", ["Groww", "Neo", "Other"], key="reset_account")
    if st.button("Reset Data"):
        df = df[~((df['Name'] == reset_name) & (df['Account'] == reset_account))]
        save_data(df)
        st.success(f"Data for {reset_name} in {reset_account} account has been reset.")

    # Use experimental_set_query_params for navigation (deprecated but needed for setting)
    if st.sidebar.button("🏠 Back to Home"):
        st.query_params["page"] = "home"
        st.rerun()

    if st.sidebar.button("📤 Go Analyse"):
        st.query_params["page"] = "analyze"
        st.rerun()
