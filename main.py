# main.py
import streamlit as st
from ui import render_home
from analyse import render_analyze
from update import render_update

page = st.query_params.get("page", "home")

if page == "analyze":
    render_analyze()
elif page == "update":
    render_update()
else:
    render_home()
