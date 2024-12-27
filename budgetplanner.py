import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state for navigation and categories
if "page" not in st.session_state:
    st.session_state["page"] = "housing"

# Initialize dictionaries for each category
category_dicts = {
    "housing_values": {"Rent": 0.0, "Utilities": 0.0, "Property Taxes": 0.0, "Cell Phone Bills": 0.0, "Other Housing Expenses": 0.0},
    "transportation_values": {"Car Payments & Fuel": 0.0, "Public Transit": 0.0, "Maintenance & Insurance": 0.0},
    "food_values": {"Groceries": 0.0, "Dining Out": 0.0},
    "health_values": {"Health Insurance": 0.0, "Gym Membership": 0.0, "Medical Bills": 0.0},
    "debt_savings_values": {"Student Loans": 0.0, "Credit Card Payments": 0.0, "Retirement Contributions": 0.0, "Savings": 0.0},
    "personal_family_values": {"Clothing & Accessories": 0.0, "Subscriptions": 0.0, "Childcare or Pet Care": 0.0},
    "entertainment_travel_values": {"Movies, Concerts, Hobbies": 0.0, "Flights & Accommodation": 0.0, "Transportation": 0.0},
    "miscellaneous_values": {"Gifts & Donations": 0.0, "Unexpected Costs": 0.0}
}

for key, default_values in category_dicts.items():
    if key not in st.session_state:
        st.session_state[key] = default_values

# Pages: Questions and Input Collection
def question_page(title, items, category_key, next_page):
    st.title(f"Budget Planner - {title}")
    st.write(f"Enter your {title} expenses below:")
    for item in items:
        st.session_state[category_key][item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=f"{category_key}_{item}")
    if st.button("Next"):
        st.session_state["page"] = next_page
        st.experimental_rerun()


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

# Summary Page
elif st.session_state["page"] == "summary":
    st.title("Budget Summary")
    
    # Retrieve stored values
    housing_values = st.session_state["housing_values"]
    transportation_values = st.session_state["transportation_values"]
    food_values = st.session_state["food_values"]
    health_values = st.session_state["health_values"]
    debt_savings_values = st.session_state["debt_savings_values"]
    personal_family_values = st.session_state["personal_family_values"]
    entertainment_travel_values = st.session_state["entertainment_travel_values"]
    miscellaneous_values = st.session_state["miscellaneous_values"]
    
    # Display total expenses summary
    total_expenses = sum(sum(values.values()) for values in [
        housing_values, transportation_values, food_values, health_values,
        debt_savings_values, personal_family_values, entertainment_travel_values, miscellaneous_values
    ])
    
    st.write("### Total Expenses")
    st.write(f"**Total:** ${total_expenses:.2f}")
    
    # Add buttons for navigation
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Expense Breakdown"):
            st.session_state["page"] = "expense_breakdown"
    with col2:
        if st.button("Chatbot"):
            st.session_state["page"] = "chatbot"
    with col3:
        if st.button("Suggested Budgets"):
            st.session_state["page"] = "suggested_budgets"
    with col4:
        if st.button("Savings Tracker"):
            st.session_state["page"] = "savings_tracker"

# Expense Breakdown Page
elif st.session_state["page"] == "expense_breakdown":
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

    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"

# Chatbot Page
elif st.session_state["page"] == "chatbot":
    st.title("Budget Chatbot")
    st.write("Ask any questions about budgeting, categories, or financial advice.")
    user_input = st.text_input("You:")
    if user_input:
        st.write("Chatbot: Here's a response to your question!")  # Replace with chatbot logic
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"

# Suggested Budgets Page
elif st.session_state["page"] == "suggested_budgets":
    st.title("Suggested Budgets")
    st.write("Here are some suggested budgets based on your expenses:")
    st.write("- **50/30/20 Rule:** Allocate 50% to needs, 30% to wants, and 20% to savings.")
    st.write("- **Dynamic Adjustments:** Recommendations based on your entered data.")
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"

# Savings Tracker Page
elif st.session_state["page"] == "savings_tracker":
    st.title("Savings Tracker")
    savings_goal = st.number_input("Set your savings goal:", min_value=0.0, step=100.0)
    current_savings = st.number_input("Enter your current savings:", min_value=0.0, step=100.0)
    
    if savings_goal > 0:
        progress = min(current_savings / savings_goal, 1.0)
        st.progress(progress)
        if progress >= 1.0:
            st.success("Congratulations! You've reached your savings goal.")
        else:
            st.info(f"You've saved {progress * 100:.2f}% of your goal.")

    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
