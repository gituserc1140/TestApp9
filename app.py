import streamlit as st
import os
from openai import OpenAI

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog(topic):
    """
    Generates a blog post using OpenAI's GPT-3.5-turbo model.

    Args:
        topic (str): The topic for the blog post.

    Returns:
        str: The generated blog content or None if an error occurs.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes blog posts."},
                {"role": "user", "content": f"Write a blog post about {topic}."}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Failed to generate blog post: {str(e)}")
        return None

st.title("AI-Powered Blog Writer")

# Input for blog topic with validation
topic = st.text_input("Enter a topic for your blog post:")

if st.button("Generate Blog"):
    if topic and 5 <= len(topic) <= 100:
        with st.spinner("Generating blog post..."):
            blog_content = generate_blog(topic)
            if blog_content:
                st.subheader("Generated Blog Post")
                st.write(blog_content)
    else:
        st.warning("Please enter a valid topic (5-100 characters).")
