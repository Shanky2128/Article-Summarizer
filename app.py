import streamlit as st

# Import functions from your backend files
from test import get_article_content
from main import summarize_article


# Page configuration
st.set_page_config(
    page_title="AI Article Summarizer",
    page_icon="📰",
    layout="centered"
)

# Title
st.title("📰 AI Article Summarizer")

st.write(
    "Paste any article link and get an AI-generated summary using Gemini."
)

# Input box for URL
article_url = st.text_input(
    "Enter Article URL"
)

# Button
if st.button("Generate Summary"):

    if article_url == "":
        st.warning("Please enter a valid article URL")
    else:
        with st.spinner("Extracting article and generating summary..."):

            try:
                # Step 1: Extract article content
                article_text = get_article_content(article_url)

                # Step 2: Summarize article
                summary = summarize_article(article_text)

                # Display result
                st.success("Summary Generated Successfully!")

                st.subheader("📄 Summary")
                st.write(summary)

            except Exception as e:
                st.error(f"Error: {str(e)}")