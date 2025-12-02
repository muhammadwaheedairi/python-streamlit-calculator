# Streamlit Calculator

This is a simple calculator application built with Python and the Streamlit library. It provides a clean and user-friendly web interface for performing basic and some advanced arithmetic operations.

**This project was created using [Gemini CLI](https://github.com/google/gemini-cli), an AI-powered command line tool, to generate the code and structure.**

Check out the live app here: [https://calculator-demo-app.streamlit.app/](https://calculator-demo-app.streamlit.app/)

---

## Features

* **Standard Operations**:

  * Addition (+)
  * Subtraction (-)
  * Multiplication (*)
  * Division (/)
* **Additional Operations**:

  * Power (**)
  * Modulo (%)
* **Session History**: The calculator keeps a history of all calculations you perform during a session. The history is displayed below the calculator.
* **Dynamic Updates**: The result is updated instantly as you change the numbers or the selected operation.
* **User-Friendly UI**: The interface is organized with columns for clarity, separating the number inputs from the operation selection.

---

## Dependencies

The only required dependency is Streamlit. You can install it using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

---

## How to Run the Calculator

1. **Navigate to the project directory**:
   Open your terminal or command prompt and change your directory to `streamlit_calculator`.

   ```bash
   cd path/to/streamlit_calculator
   ```

2. **Install the dependencies**:
   If you haven't installed the dependencies yet, run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

   Streamlit will start a local server and open the calculator in your default web browser.

---

## How to Use

1. **Enter Numbers**: Use the number input fields on the left to enter the two numbers for your calculation.
2. **Select Operation**: Use the dropdown menu on the right to select the desired arithmetic operation.
3. **View Result**: The result of the calculation will be displayed dynamically below the input fields.
4. **View History**: A log of your calculations for the current session is shown at the bottom of the page.
