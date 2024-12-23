import streamlit as st

# Sample list of bill items
bill_items = ["Rent", "Groceries", "Utilities", "Transportation", "Entertainment"]

# Create a dictionary to store bill values
bill_values = {}

st.title("Budget Planner")

# Display input fields
st.write("Enter your bills below:")
for item in bill_items:
    bill_values[item] = st.number_input(f"{item}:", min_value=0.0, step=0.01)

# Submit button
if st.button("Submit"):
    st.write("Here are your entered bills:")
    for item, value in bill_values.items():
        st.write(f"{item}: ${value:.2f}")
