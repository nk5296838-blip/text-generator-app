import streamlit as st
from transformers import pipeline
import torch

st.set_page_config(page_title="GPT-2 Text Generator", page_icon="robot")
st.title("robot GPT-2 Text Generator")

@st.cache_resource
def load_model():
      return pipeline("text-generation", model="gpt2")

generator = load_model()

prompt = st.text_area("Enter your prompt:", "AI is ")
max_len = st.slider("Max Length", 10, 250, 50)
temp = st.slider("Temperature", 0.1, 2.0, 0.7, 0.1)
top_k = st.slider("Top K", 1, 100, 50)
top_p = st.slider("Top P", 0.1, 1.0, 0.95, 0.05)
num_seq = st.number_input("Output Sequences", 1, 5, 3)

if st.button("Generate Text"):
      with st.spinner("Generating..."):
                results = generator(
                              prompt,
                              max_length=max_len,
                              num_return_sequences=num_seq,
                              temperature=temp,
                              top_k=top_k,
                              top_p=top_p
                )
                st.success("Success!")
                for i, res in enumerate(results):
                              st.info(f"Output {i+1}:\n" + res['generated_text'])
                  
