import streamlit as st
from openai import OpenAI

# Read API key from file
with open(r"C:\Users\91998\OneDrive\Desktop\Internship_folder\openai_handson\openai key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.markdown("<h1 style='color:pink;'>Python Code Review with OpenAI</h1>", unsafe_allow_html=True)

# User input section
st.markdown("<h2 style='color:green;'>Enter Your Python Code</h2>", unsafe_allow_html=True)
prompt = st.text_area("Enter your Python code here:", height=200)

# Button to trigger code review
if st.button("Review the Code"):
    st.markdown("<h2 style='color:blue;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    st.write(generated_text)
