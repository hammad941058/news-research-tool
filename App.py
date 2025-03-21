import streamlit as st
from news_fetcher import fetch_news
from text_analysis import analyze_text

st.title("📰 News Research Tool")

query = st.text_input("Enter a topic to search for news:")

if st.button("Search"):
    st.write(f"Debug: Query entered: {query}")
    articles = fetch_news(query)
    st.write(f"Debug: Number of articles fetched: {len(articles)}")
    if articles:
        for article in articles:
            st.subheader(article['title'])
            st.write(article['description'])
            st.write(f"[Read More]({article['url']})")
            
            sentiment = analyze_text(article['description'])
            st.write(f"Sentiment: {sentiment}")
    else:
        st.write("No articles found.")

