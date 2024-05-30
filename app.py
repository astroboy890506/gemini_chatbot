# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Ensure the API key is set in the environment before running the script
# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     st.error("Google API key not found in environment variables.")
#     st.stop()

# # Initialize Google AI model
# llm = ChatGoogleGenerativeAI(model="gemini-pro", max_output_tokens=1000, api_key=api_key)

# # Streamlit UI
# st.title("Google Gemini Chatbot")

# # User input text area
# user_input = st.text_area("Enter your query here:")

# # Function to get response from Google Gemini API
# def get_response(query):
#     try:
#         response = llm.invoke(query)
#         return response.content
#     except Exception as e:
#         st.error(f"Error invoking Google Gemini API: {e}")
#         return None

# # Function to display conversation
# def display_conversation(query, response):
#     st.write("User: ", query)
#     st.write("Chatbot: ", response)

# # Handling user interaction
# if st.button("Send"):
#     if user_input.strip() == "":
#         st.error("Please enter a query!")
#     else:
#         response = get_response(user_input)
#         if response:
#             display_conversation(user_input, response)
#         else:
#             st.error("Failed to get a response from the chatbot.")


#========================================add spinner function=============
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the API key is set in the environment before running the script
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Google API key not found in environment variables.")
    st.stop()

# Initialize Google AI model
llm = ChatGoogleGenerativeAI(model="gemini-pro", max_output_tokens=1000, api_key=api_key)

# Streamlit UI
st.title("Google Gemini Chatbot")

# User input text area
user_input = st.text_area("Enter your query here:")

# Function to get response from Google Gemini API
def get_response(query):
    try:
        response = llm.invoke(query)
        return response.content
    except Exception as e:
        st.error(f"Error invoking Google Gemini API: {e}")
        return None

# Function to display conversation
def display_conversation(query, response):
    st.write("User: ", query)
    st.write("Chatbot: ", response)

# Handling user interaction
if st.button("Send"):
    if user_input.strip() == "":
        st.error("Please enter a query!")
    else:
        with st.spinner("Please wait..."):
            response = get_response(user_input)
        if response:
            display_conversation(user_input, response)
        else:
            st.error("Failed to get a response from the chatbot.")
