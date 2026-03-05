
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)


def summarize_article(article_text):
    """
    Sends article text to Gemini and returns a summary.
    """

    prompt = f"""
    Summarize the following article in around 150 words:

    {article_text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text