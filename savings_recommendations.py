import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def render_savings_recommendations():
    st.title("Savings Recommendations")
    
    # User input for expenses
    st.subheader("Enter your expenses")
    categories = ['Dining', 'Entertainment', 'Shopping', 'Subscriptions', 'Other']
    expenses = {category: st.number_input(f"{category} ($):", min_value=0.0, step=10.0) for category in categories}
    
    # Analyze expenses and suggest savings
    recommendations = []
    potential_savings = {}
    for category, amount in expenses.items():
        if amount > 200:  # Arbitrary threshold
            recommendations.append(f"Consider reducing {category} expenses.")
            potential_savings[category] = amount * 0.2  # 20% savings potential
    
    # Display recommendations
    st.subheader("Recommendations:")
    if recommendations:
        for rec in recommendations:
            st.write(f"- {rec}")
    else:
        st.write("Your expenses are well-balanced!")
    
    # Display potential savings chart
    if potential_savings:
        st.subheader("Potential Savings Chart")
        df_savings = pd.DataFrame({'Category': list(potential_savings.keys()), 'Savings': list(potential_savings.values())})
        fig = px.pie(df_savings, values='Savings', names='Category', title='Potential Savings by Category')
        st.plotly_chart(fig)
    
    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
