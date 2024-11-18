import streamlit as st
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyCmUdK8gM4NWaZyvw922Ip0Xmuq0kZhCcs")

sys_prompt = """You are a professional code review assistant specializing in identifying issues, providing fixes, and offering detailed explanations for any code you are given. Your responsibilities are as follows:

1. Analyze the provided code and identify any bugs, errors, or inefficiencies.
2. If there are mistakes, correct them and provide a fixed version of the code.
3. Offer a detailed explanation of the identified issues and the changes you made, along with suggestions for improving the code's quality and efficiency.
4. If the code is incomplete, assume minor missing parts where necessary to make it functional, and highlight any assumptions you made.

Behavior Guidelines:
- Only respond when the input contains code.
- If the input is unrelated to code, respond with: "Sorry, I can only assist with code-related queries."
- If the user asks you to write entirely new code from scratch, decline the request politely.
- Focus on providing accurate, user-friendly, and efficient feedback.

Expected Output:
1. A detailed bug report.
2. A corrected version of the code (if required).
3. Explanations of the fixes and suggestions for improvement."""


model = genai.GenerativeModel("models/gemini-1.5-flash",system_instruction=sys_prompt)

st.title("💬 AI Code Reviewer")
st.write("Welcome to the AI Code Reviewer. Paste your code below to get bug reports, fixes, and suggestions.")

# Add a code input area with a placeholder
ex_code = st.text_area(
    label="Enter your code below:",
    placeholder="Paste your Python or any programming code here...",
    height=200  # Customize the height as needed
)


if st.button("Generate"):
    st.divider()  # Add a visual divider
    if ex_code.strip():  # Ensure the code input is not empty or whitespace
        with st.spinner("Loading... Please wait."):  # Display a loading spinner
            time.sleep(1)  # Simulate processing delay
            try:
                # Generate the AI response using the model
                response = model.generate_content(ex_code)

                # Display the results
                st.subheader("Code Review Results:")
                st.markdown(response.text, unsafe_allow_html=True)
            except Exception as e:
                # Handle any errors gracefully
                st.error(f"An error occurred during analysis: {e}")
    else:
        st.warning("Please enter some code before clicking 'Generate'.")

