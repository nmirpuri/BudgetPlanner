import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state
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

# Page: Housing
if st.session_state["page"] == "housing":
    st.title("Budget Planner - Housing & Utilities")
    
    housing_items = ["Rent", "Utilities", "Property Taxes", "Cell Phone Bills", "Other Housing Expenses"]
    st.write("Enter your Housing & Utilities expenses below:")

    for item in housing_items:
        st.session_state["housing_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"housing_{item}"
        )

    if st.button("Next", key="housing_next"):
        st.session_state["page"] = "transportation"

# Page: Transportation
elif st.session_state["page"] == "transportation":
    st.title("Budget Planner - Transportation")
    
    transportation_items = ["Car Payments & Fuel", "Public Transit", "Maintenance & Insurance"]
    st.write("Enter your Transportation expenses below:")

    for item in transportation_items:
        st.session_state["transportation_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"transportation_{item}"
        )

    if st.button("Next", key="transportation_next"):
        st.session_state["page"] = "food"

# Page: Food & Dining
elif st.session_state["page"] == "food":
    st.title("Budget Planner - Food & Dining")
    
    food_items = ["Groceries", "Dining Out"]
    st.write("Enter your Food & Dining expenses below:")

    for item in food_items:
        st.session_state["food_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"food_{item}"
        )

    if st.button("Next", key="food_next"):
        st.session_state["page"] = "health"

# Page: Health & Insurance
elif st.session_state["page"] == "health":
    st.title("Budget Planner - Health & Insurance")
    
    health_items = ["Health Insurance", "Gym Membership", "Medical Bills"]
    st.write("Enter your Health & Insurance expenses below:")

    for item in health_items:
        st.session_state["health_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"health_{item}"
        )

    if st.button("Next", key="health_next"):
        st.session_state["page"] = "debt_savings"

# Page: Debt & Savings
elif st.session_state["page"] == "debt_savings":
    st.title("Budget Planner - Debt & Savings")
    
    debt_savings_items = ["Student Loans", "Credit Card Payments", "Retirement Contributions", "Savings"]
    st.write("Enter your Debt & Savings expenses below:")

    for item in debt_savings_items:
        st.session_state["debt_savings_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"debt_savings_{item}"
        )

    if st.button("Next", key="debt_savings_next"):
        st.session_state["page"] = "personal_family"

# Page: Personal & Family
elif st.session_state["page"] == "personal_family":
    st.title("Budget Planner - Personal & Family")
    
    personal_family_items = ["Clothing & Accessories", "Subscriptions", "Childcare or Pet Care"]
    st.write("Enter your Personal & Family expenses below:")

    for item in personal_family_items:
        st.session_state["personal_family_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"personal_family_{item}"
        )

    if st.button("Next", key="personal_family_next"):
        st.session_state["page"] = "entertainment_travel"

# Page: Entertainment & Travel
elif st.session_state["page"] == "entertainment_travel":
    st.title("Budget Planner - Entertainment & Travel")
    
    entertainment_travel_items = ["Movies, Concerts, Hobbies", "Flights & Accommodation", "Transportation"]
    st.write("Enter your Entertainment & Travel expenses below:")

    for item in entertainment_travel_items:
        st.session_state["entertainment_travel_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"entertainment_travel_{item}"
        )

    if st.button("Next", key="entertainment_travel_next"):
        st.session_state["page"] = "miscellaneous"

# Page: Miscellaneous
elif st.session_state["page"] == "miscellaneous":
    st.title("Budget Planner - Miscellaneous")
    
    miscellaneous_items = ["Gifts & Donations", "Unexpected Costs"]
    st.write("Enter your Miscellaneous expenses below:")

    for item in miscellaneous_items:
        st.session_state["miscellaneous_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"miscellaneous_{item}"
        )

    if st.button("Next", key="miscellaneous_next"):
        st.session_state["page"] = "summary"

# Page: Summary
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
    
    # Display all categories and their values
    for category, values in zip(
        ["Housing & Utilities", "Transportation", "Food & Dining", "Health & Insurance", 
         "Debt & Savings", "Personal & Family", "Entertainment & Travel", "Miscellaneous"],
        [housing_values, transportation_values, food_values, health_values, 
         debt_savings_values, personal_family_values, entertainment_travel_values, miscellaneous_values]
    ):
        st.write(f"### {category}")
        for item, value in values.items():
            st.write(f"{item}: ${value:.2f}")
    
    # Calculations
    total_expenses = sum(sum(values.values()) for values in [
        housing_values, transportation_values, food_values, health_values,
        debt_savings_values, personal_family_values, entertainment_travel_values, miscellaneous_values
    ])
    
    st.write("### Total Expenses")
    st.write(f"**Total:** ${total_expenses:.2f}")

    # Pie and Bar Charts
    data = {
        'Category': ['Housing', 'Transportation', 'Food', 'Health', 'Debt & Savings', 'Personal & Family', 'Entertainment & Travel', 'Miscellaneous'],
        'Amount': [
            sum(housing_values.values()),
            sum(transportation_values.values()),
            sum(food_values.values()),
            sum(health_values.values()),
            sum(debt_savings_values.values()),
            sum(personal_family_values.values()),
            sum(entertainment_travel_values.values()),
            sum(miscellaneous_values.values())
        ]
    }
    df = pd.DataFrame(data)

    st.title("Expense Distribution")

    # Display Pie Chart using Plotly
    fig = px.pie(df, values='Amount', names='Category', title='Expense Distribution')
    st.plotly_chart(fig)

    # Display Bar Chart using Matplotlib
    plt.bar(df['Category'], df['Amount'])
    plt.title('Expense Breakdown')
    st.pyplot(plt)

    if st.button("Restart", key="restart"):
        st.session_state["page"] = "housing"
        for key in category_dicts:
            st.session_state[key] = {}
