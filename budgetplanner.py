import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "income"

# Page: Income and Bills
if st.session_state["page"] == "income":
    st.title("Budget Planner - Income")
    
    # Sample list of income/bill items
    income_items = ["Monthly Salary", "Other Monthly Income"]
    income_values = {}
    
    st.write("Enter your Monthly Income below:")
    for item in income_items:
        income_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=item)
    
    # Submit button
    if st.button("Submit"):
        st.session_state["income_values"] = income_values  # Save bill data to session state
        st.session_state["page"] = "bills"  # Navigate to next page

# Page: Additional Expenses
elif st.session_state["page"] == "bills":
    st.title("Budget Planner - Bills")
    
    # Sample list of additional expense items
    bills_items = ["Rent", "Utility", "Property Taxes (if applicable)", "Cell Phone Bills", "Other Bills"]
    bills_values = {}
    
    st.write("Enter monthly bills below:")
    for item in bills_items:
        bills_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=item)

if st.button("Submit"):
        st.session_state["bills_values"] = bills_values  # Save bill data to session state
        st.session_state["page"] = "bills"
         
    # Show summary
if st.button("Show Summary"):
        st.session_state["bills_values"] = bills_values
        st.session_state["page"] = "Heatlh & Insurance"

# Heatlh & Insurance
elif st.session_state["page"] == "Heatlh & Insurance":
    st.title("Budget Planner - Heatlh & Insurance")
    
    # Sample list of additional expense items
    insurance_items = ["Health Insurance", "Renters/Homeowners Insurance", "Auto Insurance", "Life Insurance", "Other Insurance"]
    insurance_values = {}
    
    st.write("Enter monthly bills below:")
    for item in insurance_items:
        insurance_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=item)


    # Show summary
     if st.button("Submit"):
        st.session_state["bills_values"] = insurance_values  # Save bill data to session state
        st.session_state["page"] = "summary"
         
   

# Page: Summary
elif st.session_state["page"] == "summary":
    st.title("Budget Summary")
    
    # Retrieve stored values
    income_values = st.session_state.get("income_values", {})
    bills_values = st.session_state.get("bills_values", {})
    bills_values = st.session_state.get("insurance_values", {})
    
    
    st.write("### Income")
    for item, value in income_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    st.write("### Monthly Bills")
    for item, value in bills_values.items():
        st.write(f"{item}: ${value:.2f}")

     st.write("### Insurance Expenses")
    for item, value in insurance_values.items():
        st.write(f"{item}: ${value:.2f}")

    st.write("### Total Income")
    total_income = sum(income_values.values())
    st.write(f"**Total:** ${total_income:.2f}")

    st.write("### Total Expenses")
    total_expenses = sum(bills_values.values()) + sum(insurance_values.values())
    st.write(f"**Total:** ${total_expenses:.2f}")

    st.write("### Budget Remaining")
    budget_left = total_income - total_expenses
    st.write(f"**Total:** ${budget_left:.2f}")
    # Option to restart
    if st.button("Restart"):
        st.session_state["page"] = "income"
