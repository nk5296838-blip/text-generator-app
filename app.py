import streamlit as st
from transformers import pipeline
st.set_page_config(page_title="GPT-2 Text Generator", page_icon="robot")
st.title("GPT-2 Text Generator")
@st.cache_resource
def load_model():
              return pipeline("text-generation", model="gpt2")

generator = load_model()
prompt = st.text_area("Enter your prompt:", "AI is ")
max_len = st.slider("Max Length", 10, 250, 50)
temperatu
