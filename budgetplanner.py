pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "income"

# Page: Income and Bills
if st.session_state["page"] == "income":
    st.title("Budget Planner - Income and Bills")
    
    # Sample list of income/bill items
    bill_items = ["Rent", "Groceries", "Utilities", "Transportation", "Entertainment"]
    bill_values = {}
    
    st.write("Enter your bills below:")
    for item in bill_items:
        bill_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=item)
    
    # Submit button
    if st.button("Submit"):
        st.session_state["bill_values"] = bill_values  # Save bill data to session state
        st.session_state["page"] = "expenses"  # Navigate to next page

# Page: Additional Expenses
elif st.session_state["page"] == "expenses":
    st.title("Budget Planner - Additional Expenses")
    
    # Sample list of additional expense items
    expense_items = ["Subscriptions", "Dining Out", "Shopping", "Travel"]
    expense_values = {}
    
    st.write("Enter additional expenses below:")
    for item in expense_items:
        expense_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01, key=item)
    
    # Show summary
    if st.button("Show Summary"):
        st.session_state["expense_values"] = expense_values
        st.session_state["page"] = "summary"

# Page: Summary
elif st.session_state["page"] == "summary":
    st.title("Budget Summary")
    
    # Retrieve stored values
    bill_values = st.session_state.get("bill_values", {})
    expense_values = st.session_state.get("expense_values", {})
    
    st.write("### Income and Bills")
    for item, value in bill_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    st.write("### Additional Expenses")
    for item, value in expense_values.items():
        st.write(f"{item}: ${value:.2f}")
    
    # Calculate total expenses
    total_expenses = sum(bill_values.values()) + sum(expense_values.values())
    st.write("### Total Expenses")
    st.write(f"**Total:** ${total_expenses:.2f}")
    
    # Data for visualization
    data = {**bill_values, **expense_values}
    df = pd.DataFrame(list(data.items()), columns=["Category", "Amount"])
    
    # Plotting a bar chart
    st.write("### Expense Breakdown")
    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["Amount"], color="skyblue")
    ax.set_title("Expense Breakdown")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Option to restart
    if st.button("Restart"):
        st.session_state["page"] = "income"
