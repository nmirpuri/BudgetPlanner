import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

def render_budget_summary():
    st.title("Expense Breakdown")
    
    # Expense data for Pie Chart and Bar Chart
    data = {
        'Category': [
            'Housing', 'Transportation', 'Food', 
            'Health', 'Debt & Savings', 'Personal & Family', 
            'Entertainment & Travel', 'Miscellaneous'
        ],
        'Amount': [
            sum(st.session_state["housing_values"].values()),
            sum(st.session_state["transportation_values"].values()),
            sum(st.session_state["food_values"].values()),
            sum(st.session_state["health_values"].values()),
            sum(st.session_state["debt_savings_values"].values()),
            sum(st.session_state["personal_family_values"].values()),
            sum(st.session_state["entertainment_travel_values"].values()),
            sum(st.session_state["miscellaneous_values"].values())
        ]
    }
    df = pd.DataFrame(data)
    
    # Pie Chart
    fig_pie = px.pie(df, values='Amount', names='Category', title='Expense Distribution')
    st.plotly_chart(fig_pie)
    
    # Bar Chart
    plt.figure(figsize=(10, 5))
    plt.bar(df['Category'], df['Amount'], color='skyblue')
    plt.title('Expense Breakdown')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    st.pyplot(plt)

     st.subheader("Budget Allocation Table")

    # Calculate the total budget and percentages
    total_budget = df['Amount'].sum()
    df['Percentage'] = (df['Amount'] / total_budget) * 100
    
    # Create and display the table
    st.dataframe(df.round({'Amount': 2, 'Percentage': 2}))

    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
