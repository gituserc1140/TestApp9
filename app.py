import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets['openai_api_key'])

def generate_blog(topic):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes blog posts."},
            {"role": "user", "content": f"Write a blog post about {topic}."}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

st.title("AI-Powered Blog Writer")

# Input for blog topic
topic = st.text_input("Enter a topic for your blog post:")

if st.button("Generate Blog"):
    if topic:
        with st.spinner("Generating blog post..."):
            blog_content = generate_blog(topic)
            st.subheader("Generated Blog Post")
            st.write(blog_content)
    else:
        st.warning("Please enter a topic.")
