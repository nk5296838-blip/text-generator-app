import streamlit as st
from transformers import pipeline
st.set_page_config(page_title="GPT-2 Text Generator", page_icon="robot", layout="centered")
st.title("GPT-2 Text Generator")
st.write("Enter a prompt below and let the AI generate text for you!")
@st.cache_resource
def load_generator():
      return pipeline("text-generation", model="gpt2")

generator = load_generator()
with st.form("generation_form"):
      prompt = st.text_area("Enter your prompt:", "AI is ")
      col1, col2 = st.columns(2)
      with col1:
                max_length = st.slider("Max Length", min_value=10, max_value=250, value=50)
                temperature = st.slider("Temperature", min_value=0.1, max_value=2.0, value=0.7, step=0.1)
            with col2:
          top_k = st.slider("Top K", min_value=1, max_value=100, value=50)
                      top_p = st.slider("Top P", min_value=0.1, max_value=1.0, value=0.95, step=0.05)
    num_return_sequences = st.number_input("Number of Output Sequences", min_value=1, max_value=5, value=3)
    submit = st.form_submit_button("Generate Text")
if submit:
      if prompt.strip() == "":
                st.warning("Please enter a prompt.")
else:
        with st.spinner("Generating text..."):
                      try:
                                        results = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences, temperature=temperature, top_k=top_k, top_p=top_p)
                                        st.success("Text generated successfully!")
                                        for i, output in enumerate(results):
                                                              st.subheader(f"Output {i+1}")
                                                              st.info(output['generated_text'])
                      except Exception as e:
                                        st.error(f"Error generating text: {e}")
                        
