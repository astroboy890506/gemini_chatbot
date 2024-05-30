import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
# Set up Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyANo6NLWBI6cfq5-GR1XQ9W2jZkHyUWnKU"

# Initialize Google AI model
llm = ChatGoogleGenerativeAI(model="gemini-pro", max_output_tokens=1000)

# Streamlit UI
st.title("Google Gemini Chatbot")

# User input text area
user_input = st.text_area("Enter your query here:")

# Function to get response from Google Gemini API
def get_response(query):
    response = llm.invoke(query)
    return response.content

# Function to display conversation
def display_conversation(query, response):
    st.write("User: ", query)
    st.write("Chatbot: ", response)

# Handling user interaction
if st.button("Send"):
    if user_input.strip() == "":
        st.error("Please enter a query!")
    else:
        response = get_response(user_input)
        display_conversation(user_input, response)
