import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

def render_budget_goals():
    st.title("Savings Planner with Milestones")
    
    # User inputs
    st.subheader("Set Your Savings Goal")
    goal = st.number_input("Enter your savings goal ($):", min_value=0.0, step=100.0)
    current_savings = st.number_input("Enter your current savings ($):", min_value=0.0, step=100.0)
    target_date = st.date_input("Target Date for Goal", min_value=datetime.now().date())
    
    # Calculate progress and monthly savings needed
    if goal > 0 and target_date > datetime.now().date():
        days_left = (target_date - datetime.now().date()).days
        monthly_savings_needed = (goal - current_savings) / (days_left / 30.0)
        
        st.write(f"Days Left: {days_left} days")
        st.write(f"Monthly Savings Needed: ${monthly_savings_needed:.2f}")
        
        # Display progress
        progress = (current_savings / goal) * 100
        st.write(f"Progress: {progress:.2f}%")
        st.progress(min(progress / 100, 1.0))
        
        # Milestones
        milestones = [goal * x / 4 for x in range(1, 5)]
        st.write("### Milestones")
        for i, milestone in enumerate(milestones, 1):
            milestone_progress = min(current_savings / milestone, 1.0) * 100
            st.write(f"Milestone {i}: ${milestone:.2f} ({milestone_progress:.2f}% completed)")
            st.progress(min(milestone_progress / 100, 1.0))
        
        # Savings over time chart
        st.write("### Savings Growth Over Time")
        dates = [datetime.now().date() + timedelta(days=x * 30) for x in range(int(days_left / 30) + 1)]
        savings_projection = [current_savings + monthly_savings_needed * i for i in range(len(dates))]
        df = pd.DataFrame({"Date": dates, "Savings": savings_projection})
        st.line_chart(df.set_index("Date"))
    
    else:
        st.write("Enter a goal and target date to calculate progress.")
    
    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
