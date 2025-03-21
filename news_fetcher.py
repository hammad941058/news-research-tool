# news_fetcher.py

# news_fetcher.py

import requests
from config import NEWS_API_KEY

import requests
from config import NEWS_API_KEY

def fetch_news(query):
    """Fetch news articles based on a query."""
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    # Debugging information
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text[:500]}")  # Print the first 500 characters of the response

    if response.status_code == 200:
        data = response.json()
        return data.get("articles", [])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return []

if __name__ == "__main__":
    topic = "AI"
    news_articles = fetch_news(topic)

    for idx, article in enumerate(news_articles, start=1):
        print(f"{idx}. {article['title']} - {article['source']['name']}")
        print(article['url'])
        print()