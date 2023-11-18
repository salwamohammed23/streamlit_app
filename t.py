import streamlit as st
import requests
from PIL import Image
import io
from transformers import pipeline
import matplotlib.pyplot as plt

API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
HEADERS = {"Authorization": f"Bearer {'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'}"}

# Streamlit UI
st.title("Image and Text Generation App")



# Split the page into two columns
col1, col2, col3 = st.columns(3)

# Image Inference Section
with col1:
    st.header("Image Inference")
    
    image_url = st.text_input("Enter your image_key_word:")
    if st.button("Generate Image Inference"):
        # API Query
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": image_url})
        image_bytes = response.content

        # Display Image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Inferred Image", use_column_width=True)

# Text Generation Section
with col2:
    for i in range(100):
        print("**")


with col3:    
    st.header("Text Generation")
   
    keyword = st.text_input("Enter your keyword:")
    if st.button("Generate Text"):
        # Text Generation Pipeline
        generator = pipeline('text-generation', model='gpt2')
        generated_text = generator(keyword, max_length=100, num_return_sequences=1)[0]['generated_text']
        st.write(generated_text)


