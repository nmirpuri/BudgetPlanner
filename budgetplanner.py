import streamlit as st

# Title of the app
st.title("Personal Budget Planner")

# Categories for fixed expenses
categories = ["Housing & Utilities", "Transportation", "Personal & Family", "Debt & Savings"]

# Dictionary to store user inputs
expenses = {}

# Input fields for each category
for category in categories:
    st.subheader(category)
    if category == "Housing & Utilities":
        rent = st.number_input("Enter Rent/Mortgage", min_value=0.0, step=50.0)
        utilities = st.number_input("Enter Utilities (Electricity, Gas, etc.)", min_value=0.0, step=50.0)
        internet_phone = st.number_input("Enter Internet/Phone Bills", min_value=0.0, step=50.0)
        expenses[category] = rent + utilities + internet_phone
    elif category == "Transportation":
        car_payment = st.number_input("Enter Car Payment", min_value=0.0, step=50.0)
        insurance = st.number_input("Enter Car Insurance", min_value=0.0, step=50.0)
        fuel = st.number_input("Enter Fuel Expenses", min_value=0.0, step=50.0)
        public_transport = st.number_input("Enter Public Transport Fees", min_value=0.0, step=50.0)
        parking_tolls = st.number_input("Enter Parking/Toll Fees", min_value=0.0, step=50.0)
        expenses[category] = car_payment + insurance + fuel + public_transport + parking_tolls
    elif category == "Personal & Family":
        health_insurance = st.number_input("Enter Health Insurance", min_value=0.0, step=50.0)
        childcare_education = st.number_input("Enter Childcare/Schooling Expenses", min_value=0.0, step=50.0)
        groceries = st.number_input("Enter Grocery Expenses", min_value=0.0, step=50.0)
        subscriptions = st.number_input("Enter Subscriptions (Gym, Streaming, etc.)", min_value=0.0, step=50.0)
        personal_insurance = st.number_input("Enter Personal Insurance (Life, Disability)", min_value=0.0, step=50.0)
        expenses[category] = health_insurance + childcare_education + groceries + subscriptions + personal_insurance
    elif category == "Debt & Savings":
        loan_payments = st.number_input("Enter Loan Payments (Student, Car, etc.)", min_value=0.0, step=50.0)
        credit_card = st.number_input("Enter Credit Card Minimum Payments", min_value=0.0, step=50.0)
        retirement_savings = st.number_input("Enter Retirement Contributions", min_value=0.0, step=50.0)
        emergency_fund = st.number_input("Enter Emergency Savings Fund", min_value=0.0, step=50.0)
        expenses[category] = loan_payments + credit_card + retirement_savings + emergency_fund

# Display the total expenses
total_expenses = sum(expenses.values())
st.subheader("Total Expenses")
st.write(f"Your total expenses are: ${total_expenses:.2f}")

# Option to submit and show breakdown of expenses
if st.button('Submit'):
    st.write("### Expense Breakdown by Category")
    for category, amount in expenses.items():
        st.write(f"{category}: ${amount:.2f}")

    # Show a simple bar chart
    st.bar_chart(expenses)
