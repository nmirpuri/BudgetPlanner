import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Function to render the Goal-Oriented Savings Planner page
def render_budget_goals():
    st.title("Goal-Oriented Savings Planner")
    
    # User inputs
    st.subheader("Set Your Savings Goal")
    goal_name = st.text_input("What are you saving for? (e.g., Planning a Vacation, Buying a New Car, Saving for an Emergency Fund)")
    goal_amount = st.number_input("Enter your savings goal ($):", min_value=0.0, step=100.0)
    current_savings = st.number_input("Enter your current savings ($):", min_value=0.0, step=100.0)
    target_date = st.date_input("Target Date for Goal", min_value=datetime.now().date())
    
    if goal_name and goal_amount > 0 and target_date > datetime.now().date():
        # Calculate savings details
        days_left = (target_date - datetime.now().date()).days
        weeks_left = days_left / 7
        months_left = days_left / 30
        weekly_savings_needed = (goal_amount - current_savings) / max(weeks_left, 1)
        monthly_savings_needed = (goal_amount - current_savings) / max(months_left, 1)
        
        # Milestones
        st.write(f"### Goal: {goal_name}")
        st.write("### Milestones:")
        milestones = [(datetime.now().date() + timedelta(days=30 * i)).strftime("%B %Y") for i in range(int(months_left) + 1)]
        milestone_amounts = [current_savings + (monthly_savings_needed * i) for i in range(len(milestones))]
        for milestone, amount in zip(milestones, milestone_amounts):
            st.write(f"- Save ${amount:.2f} by {milestone}")
        
        # Display savings breakdown
        st.write(f"### Savings Breakdown:")
        st.write(f"- Weekly Savings Needed: **${weekly_savings_needed:.2f}**")
        st.write(f"- Monthly Savings Needed: **${monthly_savings_needed:.2f}**")
        
        # Recommendations for saving
        st.write("### Recommendations to Save:")
        recommendations = [
            "Limit dining out to once a week.",
            "Cancel unused subscriptions.",
            "Create a grocery list and stick to it to avoid impulse buying.",
            "Sell items you no longer need.",
            "Set up automatic transfers to your savings account."
        ]
        for rec in recommendations:
            st.write(f"- {rec}")
        
        # Motivational section
        st.subheader("Why It’s Worth It")
        st.write(f"💡 Remember: Achieving your goal of **{goal_name}** means it will soon become a reality!")
        st.write("Saving is not about depriving yourself; it's about deciding you love your future self just as much as your present self.")
    else:
        st.write("Please fill out all fields to calculate your savings plan.")
    
    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
