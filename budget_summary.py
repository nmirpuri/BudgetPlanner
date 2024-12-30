import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def render_budget_summary():
  
    st.title("Expense Breakdown")
    data = {
        'Category': ['Housing', 'Transportation', 'Food', 'Health', 'Debt & Savings', 'Personal & Family', 'Entertainment & Travel', 'Miscellaneous'],
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
    fig = px.pie(df, values='Amount', names='Category', title='Expense Distribution')
    st.plotly_chart(fig)
    
    # Bar Chart
    plt.bar(df['Category'], df['Amount'])
    plt.title('Expense Breakdown')
    st.pyplot(plt)

# Sample budget allocation data
    start_date = datetime(2024, 1, 1)  # Example start date

# Generate week start dates
    week_dates = [start_date + timedelta(weeks=i) for i in range(len(data["Week"]))]

# Replace "Week" column with actual dates
    data["Week"] = week_dates
    data = {
      "Category": ["Rent", "Groceries", "Entertainment", "Utilities", "Savings"],
      "Allocation": [1000, 300, 150, 200, 350],
      "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
    }

# Convert data into a DataFrame
    df = pd.DataFrame(data)

# Expand the data for each week
    timeline_data = []
    for category, allocation in zip(data["Category"], data["Allocation"]):
        for week in data["Week"]:
            timeline_data.append({"Category": category, "Allocation": allocation, "Week": week})

# Create a new DataFrame for the timeline
    timeline_df = pd.DataFrame(timeline_data)

# Create the timeline visualization
    fig = px.timeline(
        timeline_df,
        x_start="Week",
        x_end="Week",
        y="Category",
        color="Category",
        title="Budget Allocation Timeline",
        labels={"Category": "Budget Category", "Allocation": "Amount Allocated"},
    )

    fig.update_yaxes(categoryorder="total ascending")  # Sort categories by total allocation
    fig.update_layout(
        xaxis_title="Time (Weeks)",
        yaxis_title="Budget Categories",
        showlegend=True,
    )

# Show the visualization
    fig.show()


    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
