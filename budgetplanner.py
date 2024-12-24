import matplotlib.pyplot as plt
import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "income"

if "income_values" not in st.session_state:
    st.session_state["income_values"] = {}

if "bills_values" not in st.session_state:
    st.session_state["bills_values"] = {}

if "insurance_values" not in st.session_state:
    st.session_state["insurance_values"] = {}

# Page: Income
if st.session_state["page"] == "income":
    st.title("Budget Planner - Income")
    
    # Sample list of income items
    income_items = ["Monthly Salary", "Other Monthly Income"]
    st.write("Enter your Monthly Income below:")
    
    for item in income_items:
        st.session_state["income_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"income_{item}"
        )
    
    if st.button("Next", key="income_next"):
        st.session_state["page"] = "bills"

# Page: Bills
elif st.session_state["page"] == "bills":
    st.title("Budget Planner - Bills")
    
    # Sample list of bill items
    bills_items = ["Rent", "Utilities", "Property Taxes", "Cell Phone Bills", "Other Bills"]
    st.write("Enter your Monthly Bills below:")
    
    for item in bills_items:
        st.session_state["bills_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"bills_{item}"
        )
    
    if st.button("Next", key="bills_next"):
        st.session_state["page"] = "insurance"

# Page: Insurance
elif st.session_state["page"] == "insurance":
    st.title("Budget Planner - Health & Insurance")
    
    # Sample list of insurance items
    insurance_items = ["Health Insurance", "Renters/Homeowners Insurance", 
                       "Auto Insurance", "Life Insurance", "Other Insurance"]
    st.write("Enter your Monthly Insurance Expenses below:")
    
    for item in insurance_items:
        st.session_state["insurance_values"][item] = st.number_input(
            f"{item}:", min_value=0.0, step=0.01, key=f"insurance_{item}"
        )
    
    if st.button("Next", key="insurance_next"):
        st.session_state["page"] = "summary"

# Page: Summary
elif st.session_state["page"] == "summary":
    st.title("Budget Summary")
    
    # Retrieve stored values
    income_values = st.session_state["income_values"]
    bills_values = st.session_state["bills_values"]
    insurance_values = st.session_state["insurance_values"]
    
    st.write("### Income")
    for item, value in income_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    st.write("### Monthly Bills")
    for item, value in bills_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    st.write("### Insurance Expenses")
    for item, value in insurance_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    # Calculations
    total_income = sum(income_values.values())
    total_expenses = sum(bills_values.values()) + sum(insurance_values.values())
    budget_left = total_income - total_expenses
    
    st.write("### Total Income")
    st.write(f"**Total:** ${total_income:.2f}")
    
    st.write("### Total Expenses")
    st.write(f"**Total:** ${total_expenses:.2f}")
    
    st.write("### Budget Remaining")
    st.write(f"**Total:** ${budget_left:.2f}")



# Example Pie Chart Code
categories = ["Rent", "Utilities", "Insurance", "Other Bills", "Savings"]
values = [1000, 300, 200, 500, 500]  # Example data

fig, ax = plt.subplots()
ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.

st.pyplot(fig)

    
    if st.button("Restart", key="restart"):
        st.session_state["page"] = "income"
        st.session_state["income_values"] = {}
        st.session_state["bills_values"] = {}
        st.session_state["insurance_values"] = {}
