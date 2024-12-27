import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state for navigation and categories
if "page" not in st.session_state:
    st.session_state["page"] = "housing"

# Initialize dictionaries for each category
category_dicts = {
    "housing_values": {},
    "transportation_values": {},
    "food_values": {},
    "health_values": {},
    "debt_savings_values": {},
    "personal_family_values": {},
    "entertainment_travel_values": {},
    "miscellaneous_values": {}
}

for key in category_dicts:
    if key not in st.session_state:
        st.session_state[key] = {}

# Sidebar Navigation
with st.sidebar:
    st.title("Navigation")
    if st.session_state["page"] in ["housing", "transportation", "food", "health", "debt_savings", "personal_family", "entertainment_travel", "miscellaneous"]:
        st.write("Please complete all questions to enable other sections.")
    else:
        if st.button("Chatbot"):
            st.session_state["page"] = "chatbot"
        if st.button("Suggested Budgets"):
            st.session_state["page"] = "suggested_budgets"
        if st.button("Summary"):
            st.session_state["page"] = "summary"

# Pages: Questions and Input Collection
def question_page(title, items, category_key, next_page):
    st.title(f"Budget Planner - {title}")
    st.write(f"Enter your {title} expenses below:")
    for item in items:
        st.session_state[category_key][item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=f"{category_key}_{item}")
    if st.button("Next"):
        st.session_state["page"] = next_page

if st.session_state["page"] == "housing":
    question_page("Housing & Utilities", ["Rent", "Utilities", "Property Taxes", "Cell Phone Bills", "Other Housing Expenses"], "housing_values", "transportation")
elif st.session_state["page"] == "transportation":
    question_page("Transportation", ["Car Payments & Fuel", "Public Transit", "Maintenance & Insurance"], "transportation_values", "food")
elif st.session_state["page"] == "food":
    question_page("Food & Dining", ["Groceries", "Dining Out"], "food_values", "health")
elif st.session_state["page"] == "health":
    question_page("Health & Insurance", ["Health Insurance", "Gym Membership", "Medical Bills"], "health_values", "debt_savings")
elif st.session_state["page"] == "debt_savings":
    question_page("Debt & Savings", ["Student Loans", "Credit Card Payments", "Retirement Contributions", "Savings"], "debt_savings_values", "personal_family")
elif st.session_state["page"] == "personal_family":
    question_page("Personal & Family", ["Clothing & Accessories", "Subscriptions", "Childcare or Pet Care"], "personal_family_values", "entertainment_travel")
elif st.session_state["page"] == "entertainment_travel":
    question_page("Entertainment & Travel", ["Movies, Concerts, Hobbies", "Flights & Accommodation", "Transportation"], "entertainment_travel_values", "miscellaneous")
elif st.session_state["page"] == "miscellaneous":
    question_page("Miscellaneous", ["Gifts & Donations", "Unexpected Costs"], "miscellaneous_values", "summary")

# Page: Summary
elif st.session_state["page"] == "summary":
    st.title("Budget Summary")

    # Retrieve and display stored values
    total_expenses = 0
    data = []
    for category, values in zip(
        ["Housing", "Transportation", "Food", "Health", "Debt & Savings", "Personal & Family", "Entertainment & Travel", "Miscellaneous"],
        [st.session_state[key] for key in category_dicts]
    ):
        total = sum(values.values())
        total_expenses += total
        data.append({"Category": category, "Amount": total})
        st.write(f"### {category}")
        for item, value in values.items():
            st.write(f"{item}: ${value:.2f}")

    # Display total expenses and charts
    st.write("### Total Expenses")
    st.write(f"**Total:** ${total_expenses:.2f}")

    df = pd.DataFrame(data)
    fig = px.pie(df, values='Amount', names='Category', title='Expense Distribution')
    st.plotly_chart(fig)

    plt.bar(df['Category'], df['Amount'])
    plt.title('Expense Breakdown')
    st.pyplot(plt)

# Page: Chatbot
elif st.session_state["page"] == "chatbot":
    st.title("Chatbot")
    user_input = st.text_input("Enter your message:")
    if user_input:
        st.write("Chatbot Response: I'm here to help!")

# Page: Suggested Budgets
elif st.session_state["page"] == "suggested_budgets":
    st.title("Suggested Budgets")
    st.write("Here are some budget suggestions based on your inputs.")
    # Example suggestions (you can enhance this logic)
    total_income = st.number_input("Enter your total income:", min_value=0.0, step=0.01)
    if total_income:
        savings_target = 0.2 * total_income
        st.write(f"Suggested Savings: ${savings_target:.2f}")
        for category, amount in zip(df['Category'], df['Amount']):
            percentage = (amount / total_expenses) * 100 if total_expenses else 0
            st.write(f"{category}: {percentage:.2f}% of total expenses")

