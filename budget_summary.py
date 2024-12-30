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
    st.subheader("Budget Allocation Timeline")
    
    # Sample budget allocation data
    allocation_data = {
        "Category": ["Rent", "Groceries", "Entertainment", "Utilities", "Savings"],
        "Allocation": [1000, 300, 150, 200, 350],
    }

    # Generate week start dates
    start_date = datetime(2024, 1, 1)  # Example start date
    week_dates = [start_date + timedelta(weeks=i) for i in range(5)]
    allocation_data["Week"] = week_dates

    # Convert to DataFrame
    timeline_df = pd.DataFrame(allocation_data)

    # Create the timeline visualization
    fig_timeline = px.timeline(
        timeline_df,
        x_start="Week",
        x_end="Week",
        y="Category",
        color="Category",
        title="Budget Allocation Timeline",
        labels={"Category": "Budget Category", "Allocation": "Amount Allocated"}
    )
    fig_timeline.update_yaxes(categoryorder="total ascending")  # Sort categories by total allocation
    fig_timeline.update_layout(
        xaxis_title="Time (Weeks)",
        yaxis_title="Budget Categories",
        showlegend=True,
    )
    st.plotly_chart(fig_timeline)

    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
