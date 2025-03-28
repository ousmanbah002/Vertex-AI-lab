
import streamlit as st
import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# Load environment variable
load_dotenv()
project_id = os.environ.get("PROJECT_ID")

# Init Vertex AI
vertexai.init(project=project_id, location="us-central1")
model = GenerativeModel("gemini-2.0-flash-lite-001")

st.title("Find your neighboring states")
users_state = st.text_input("Enter your state")

def get_neighboring_states_from_gemini(state_name):
    prompt = f"What are the neighboring states of {state_name} in the US?"
    response = model.generate_content(prompt)
    return response.text

if users_state:
    answer = get_neighboring_states_from_gemini(users_state)
    st.write("The neighboring states are:")
    st.write(answer)
