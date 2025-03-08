import os
import streamlit as st
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment variables
default_api_key = os.environ.get("OpenAI_API_KEY", "")

# Setting the title of the Streamlit application
st.title("Simple LLM App 🤖")

# Allow overriding the API key, but pre-fill with the one from .env if available
openai_api_key = st.sidebar.text_input('OpenAI API Key', 
                                       value=default_api_key,
                                       type='password')

# Defining a function to generate a response
def generate_response(input_text):
    # Use the key from the sidebar if provided, otherwise fall back to .env
    key_to_use = openai_api_key if openai_api_key else default_api_key
    
    if not key_to_use or not key_to_use.startswith('sk-'):
        st.error('Valid OpenAI API key required!')
        return
        
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=key_to_use)
        st.info(llm(input_text))
    except Exception as e:
        if "insufficient_quota" in str(e):
            st.error("OpenAI API quota exceeded. Please check your billing details or use a different API key.")
        else:
            st.error(f"An error occurred: {str(e)}")    


# Creating a form in the Streamlit app for user input
with st.form('my_form'):
    # Adding a text area for user input
    text = st.text_area('Enter text:' '')
    # Adding a submit button for the form
    submitted = st.form_submit_button('Submit')
    # Displaying a warning uf the entered API key does not start with 'sk-'
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API!', icon="⚠️")
    # If the form is submitted and the API key is valid, generate a response
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)