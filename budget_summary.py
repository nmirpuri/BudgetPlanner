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

    # Timeline Allocation Visualization
    st.subheader("Budget Allocation for One Month")

    # Sample budget allocation data
    allocation_data = {
        "Category": ["Housing", "Transportation", "Food", "Health", "Entertainment", "Savings"],
        "Monthly Allocation": [1200, 400, 600, 300, 200, 500],
    }

    # Divide the monthly allocation equally among 4 weeks
    weekly_allocation = []
    for category, allocation in zip(allocation_data["Category"], allocation_data["Monthly Allocation"]):
        for week in range(1, 5):
            weekly_allocation.append({
                "Category": category,
                "Week": f"Week {week}",
                "Weekly Allocation": allocation / 4
            })

    # Convert to DataFrame
    timeline_df = pd.DataFrame(weekly_allocation)

    # Create the chart
    fig_timeline = px.bar(
        timeline_df,
        x="Week",
        y="Weekly Allocation",
        color="Category",
        barmode="stack",
        title="Weekly Budget Allocation for Each Category",
        labels={"Weekly Allocation": "Amount Allocated", "Week": "Weeks in Month"}
    )
    fig_timeline.update_layout(
        xaxis_title="Weeks",
        yaxis_title="Amount Allocated ($)",
        showlegend=True,
    )
    st.plotly_chart(fig_timeline)

    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
