import streamlit as st
import matplotlib.pyplot as plt

def render_budget_goals():
    st.title("Customizable Budget Goals")
    
    # User inputs
    st.subheader("Set Your Budget Goal")
    goal = st.number_input("Enter your savings goal ($):", min_value=0.0, step=100.0)
    current_savings = st.number_input("Enter your current savings ($):", min_value=0.0, step=100.0)
    
    # Calculate progress
    if goal > 0:
        progress = (current_savings / goal) * 100
        st.write(f"Progress: {progress:.2f}%")
        
        # Display progress bar
        st.progress(min(progress / 100, 1.0))
        
        # Plot progress
        fig, ax = plt.subplots()
        ax.barh(["Progress"], [progress], color='green')
        ax.set_xlim(0, 100)
        ax.set_title("Budget Progress")
        ax.set_xlabel("Percentage Complete")
        st.pyplot(fig)
    else:
        st.write("Enter a goal to calculate progress.")
    
    # Back button
    if st.button("Back to Summary"):
        st.session_state["page"] = "summary"
