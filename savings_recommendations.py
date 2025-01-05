import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def render_savings_recommendations():
    st.title("Learn About Budgeting Methods")

    # Budgeting method descriptions
    budgeting_methods = {
        "50/30/20 Rule": (
            "This method divides your income into three categories:\n"
            "- **50% for Needs**: Essentials like housing, groceries, utilities, transportation, etc.\n"
            "- **30% for Wants**: Non-essentials like dining out, entertainment, travel, etc.\n"
            "- **20% for Savings**: Includes savings, investments, and paying off debt."
        ),
        "Envelope Method": (
            "Allocate cash into different envelopes for each spending category. "
            "Once an envelope is empty, you cannot spend more in that category until next month."
        ),
        "Zero-Based Budgeting": (
            "Assign every dollar of your income to a specific purpose, ensuring your income minus expenses equals zero."
        ),
        "Pay Yourself First": (
            "Prioritize saving by setting aside a fixed percentage of your income before allocating funds to other expenses."
        ),
    }

    # Dropdown for selecting a budgeting method
    method = st.selectbox(
        "Select a budgeting method to learn more:",
        ["Choose a method", "50/30/20 Rule", "Envelope Method", "Zero-Based Budgeting", "Pay Yourself First"]
    )

    # Display description of the selected method
    if method != "Choose a method":
        st.subheader(f"About the {method}")
        st.write(budgeting_methods[method])

        # If the user selects the 50/30/20 rule
        if method == "50/30/20 Rule":
            st.subheader("Implement the 50/30/20 Rule")

            # Input for total income
            total_income = st.number_input("Enter your monthly income:", min_value=0.0, step=100.0)

            if total_income > 0:
                # Calculate allocations
                needs = total_income * 0.50
                wants = total_income * 0.30
                savings = total_income * 0.20

                # Display the allocations
                st.write("### Allocations")
                st.write(f"- **Needs (50%)**: ${needs:.2f}")
                st.write(f"- **Wants (30%)**: ${wants:.2f}")
                st.write(f"- **Savings (20%)**: ${savings:.2f}")

                # Display categories for needs and wants
                needs_categories = ["Housing", "Groceries", "Utilities", "Healthcare", "Transportation"]
                wants_categories = ["Dining Out", "Entertainment", "Shopping", "Travel"]
                st.write("### Categories for Needs")
                st.write(", ".join(needs_categories))
                st.write("### Categories for Wants")
                st.write(", ".join(wants_categories))

    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
