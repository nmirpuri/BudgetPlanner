import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_investment_simulator():
    st.title("Investment Simulator")
    
    # User inputs
    st.subheader("Simulate Your Investment Growth")
    monthly_savings = st.number_input("Enter your monthly savings ($):", min_value=0.0, step=10.0)
    annual_return = st.number_input("Enter expected annual return (%):", min_value=0.0, step=0.1)
    
    # Simulation
    if monthly_savings > 0 and annual_return > 0:
        years = [5, 10, 20]
        growth = []
        for year in years:
            r = annual_return / 12 / 100  # Monthly interest rate
            n = year * 12  # Total months
            fv = monthly_savings * ((1 + r)**n - 1) / r
            growth.append(fv)
        
        # Display results
        st.subheader("Projected Growth")
        for year, value in zip(years, growth):
            st.write(f"In {year} years: ${value:,.2f}")
        
        # Plot growth
        fig, ax = plt.subplots()
        ax.plot(years, growth, marker='o')
        ax.set_title("Investment Growth Over Time")
        ax.set_xlabel("Years")
        ax.set_ylabel("Future Value ($)")
        st.pyplot(fig)
    else:
        st.write("Enter savings and return to simulate growth.")
    
    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
