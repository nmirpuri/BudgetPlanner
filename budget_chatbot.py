import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def render_budget_chatbot():
    st.title("Personal Budget ChatBot")

    st.title("Budget Chatbot")
    st.write("Ask any questions about budgeting, categories, or financial advice.")
    user_input = st.text_input("You:")
    if user_input:
        st.write("Chatbot: Here's a response to your question!")  # Replace with chatbot logic
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
