import streamlit as st
from news_fetcher import fetch_news
from text_analysis import summarize_text

st.title("📰 News Research Tool")

query = st.text_input("Enter a topic:")
if st.button("Fetch News"):
    articles = fetch_news(query)
    
    if "error" in articles:
        st.error("Failed to fetch news!")
    else:
        for article in articles[:5]:  # Display top 5 articles
            st.subheader(article["title"])
            st.write(article["description"])
            summary = summarize_text(article["content"][:500])  # Limit text length
            st.write(f"**Summary:** {summary}")
            st.write(f"[Read More]({article['url']})")
            st.write("---")
else:
    st.info("Enter a topic and click 'Fetch News' to get started!")
    
