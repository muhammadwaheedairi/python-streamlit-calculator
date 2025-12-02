# Import the Streamlit library, which is used to create the web app
import streamlit as st

# Set the title of the web app
st.title("Simple Calculator")

# Initialize session state for history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state.history = []

# Create columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    # Create a number input widget for the first number.
    # "Enter first number" is the label displayed above the input box.
    # The value is stored in the 'num1' variable.
    num1 = st.number_input("Enter first number", value=0.0)

    # Create a number input widget for the second number.
    # "Enter second number" is the label.
    # The value is stored in the 'num2' variable.
    num2 = st.number_input("Enter second number", value=0.0)

with col2:
    # Create a dropdown select box for the user to choose an operation.
    # "Operation" is the label for the dropdown.
    # The options now include 'Power' and 'Modulo'.
    # The selected option is stored in the 'operation' variable.
    operation = st.selectbox("Operation", ('Add', 'Subtract', 'Multiply', 'Divide', 'Power', 'Modulo'))

# Initialize the result variable
result = 0
calculation_done = False

# Perform the calculation based on the selected operation
if operation == 'Add':
    # If 'Add' is selected, add the two numbers
    result = num1 + num2
    calculation_done = True
elif operation == 'Subtract':
    # If 'Subtract' is selected, subtract the second number from the first
    result = num1 - num2
    calculation_done = True
elif operation == 'Multiply':
    # If 'Multiply' is selected, multiply the two numbers
    result = num1 * num2
    calculation_done = True
elif operation == 'Divide':
    # If 'Divide' is selected, check for division by zero
    if num2 != 0:
        # If the denominator is not zero, perform the division
        result = num1 / num2
        calculation_done = True
    else:
        # If the denominator is zero, display an error message
        st.error("Division by zero is not allowed.")
        result = "Not defined"
elif operation == 'Power':
    # If 'Power' is selected, calculate num1 to the power of num2
    result = num1 ** num2
    calculation_done = True
elif operation == 'Modulo':
    # If 'Modulo' is selected, check for division by zero
    if num2 != 0:
        # If the denominator is not zero, perform the modulo operation
        result = num1 % num2
        calculation_done = True
    else:
        # If the denominator is zero, display an error message
        st.error("Modulo by zero is not allowed.")
        result = "Not defined"

# Display the result and update history
if calculation_done:
    # Display the result of the calculation in a styled success box.
    # The 'f-string' is used to format the string with the calculated result.
    st.success(f"The result is: {result}")
    
    # Create the history entry string
    history_entry = f"{num1} {operation} {num2} = {result}"
    
    # Add the current calculation to the beginning of the history list
    # and avoid duplicate consecutive calculations
    if not st.session_state.history or st.session_state.history[0] != history_entry:
        st.session_state.history.insert(0, history_entry)

# Display the calculation history
st.subheader("Calculation History")
if not st.session_state.history:
    st.write("No calculations yet.")
else:
    # Display each calculation from the history
    for entry in st.session_state.history:
        st.write(entry)