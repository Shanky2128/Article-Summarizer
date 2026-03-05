# import requests
# import os
# from dotenv import load_dotenv

# # Load variables from .env
# load_dotenv()

# # Get API key
# api_key = os.getenv("RAPID_API_KEY")

# url = "https://article-extractor2.p.rapidapi.com/article/parse"

# querystring = {"url":"https://medium.com/sharing-food/i-ate-my-way-through-singapore-and-absolutely-loved-it-part-1-36c2f0296a55","region":"eu"}


# headers = {
# 	"x-rapidapi-key": api_key,
# 	"x-rapidapi-host": "article-extractor2.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get RapidAPI key
api_key = os.getenv("RAPID_API_KEY")


def get_article_content(article_url):
    """
    Fetch article content using RapidAPI article extractor.
    Returns the article content as text.
    """

    url = "https://article-extractor2.p.rapidapi.com/article/parse"

    # Parameters sent to API
    querystring = {
        "url": article_url,
        "region": "eu"
    }

    # API headers
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "article-extractor2.p.rapidapi.com"
    }

    # Send GET request
    response = requests.get(url, headers=headers, params=querystring)

    # Convert response to JSON
    data = response.json()

    # Extract only article content
    if data["error"] == 0:
        article_content = data["data"]["content"]
        return article_content
    else:
        raise Exception("Failed to extract article")