# from google import genai
# import os
# from dotenv import load_dotenv

# # Load variables from .env
# load_dotenv()

# # Get API key
# api_key = os.getenv("GEMINI_API_KEY")

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Explain interpolation in mathamatics.in 100 words"
# )
# print(response.text)

# from google import genai
# import os
# from dotenv import load_dotenv

# # Import article extractor function
# from test import get_article_content

# # Load environment variables
# load_dotenv()

# # Get Gemini API key
# api_key = os.getenv("GEMINI_API_KEY")

# # Initialize Gemini client
# client = genai.Client(api_key=api_key)


# def summarize_article(article_text):
#     """
#     Sends article text to Gemini and returns summary.
#     """

#     prompt = f"""
#     Summarize the following article in 150 words.

#     Article:
#     {article_text}
#     """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt
#     )

#     return response.text


# if __name__ == "__main__":

#     # Article URL to summarize
#     article_url = "https://medium.com/sharing-food/i-ate-my-way-through-singapore-and-absolutely-loved-it-part-1-36c2f0296a55"

#     # Step 1: Fetch article content
#     article_text = get_article_content(article_url)

#     print("\n Article content fetched successfully\n")

#     # Step 2: Send to Gemini for summarization
#     summary = summarize_article(article_text)

#     # Step 3: Print summary
#     print("===== ARTICLE SUMMARY =====\n")
#     print(summary)

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