from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

news_api_key = os.getenv('news_api_key')
newsapi = NewsApiClient(api_key=news_api_key)

def get_top_news_from_india():
    # Fetch all articles related to the topic from Indian news sources
    # Add more Indian news domains as necessary
    indian_news_domains = 'thehindu.com,indiatimes.com,ndtv.com,indiatoday.in,hindustantimes.com,economictimes.indiatimes.com'
    all_articles = newsapi.get_everything(language='en', domains=indian_news_domains, page_size=50)
    # Check if the API call was successful and return the top stories
    if all_articles['status'] == 'ok':
        return all_articles['articles']
    else:
        print("Error fetching news:", all_articles.get('message'))
        return []
