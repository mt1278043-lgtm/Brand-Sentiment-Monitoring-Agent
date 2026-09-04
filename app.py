import streamlit as st
import matplotlib.pyplot as plt
from mentions import generate_mentions
from sentiment_model import analyze_sentiment
from summary_prompt import summary_prompt
from langchain.chat_models import ChatOpenAI
import os

st.title("🧠 Brand Sentiment Monitoring Agent")

if st.button("Run Sentiment Analysis"):
    # Generate mentions
    df = generate_mentions()

    # Analyze sentiment
    df["Sentiment"] = df["text"].apply(analyze_sentiment)
    sentiment_counts = df["Sentiment"].value_counts()

    # Pie chart
    st.subheader("🔎 Sentiment Breakdown")
    fig, ax = plt.subplots()
    colors = ['#2ecc71', '#95a5a6', '#e74c3c']  # green, gray, red
    ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=colors)
    st.pyplot(fig)

    # Display sentiment data
    st.subheader("📊 Sentiment Data")
    st.dataframe(df[["text", "timestamp", "Sentiment"]].sort_values("timestamp", ascending=False))

    # GPT Summary
    summary_text = df["Sentiment"].value_counts().to_string()

    # Check if OpenAI API key is available
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            llm = ChatOpenAI(temperature=0.4, api_key=api_key)
            gpt_summary = llm.predict(summary_prompt.format(sentiment_data=summary_text))

            st.subheader("🧠 GPT Summary & Recommendations")
            st.text_area("Insights", gpt_summary, height=300)
        except Exception as e:
            st.warning(f"Could not generate GPT summary: {e}")
            st.info("Please ensure OPENAI_API_KEY is set in your environment.")
    else:
        st.info("To enable GPT-based insights, please set the OPENAI_API_KEY environment variable.")
        st.subheader("📈 Sentiment Summary")
        st.text(f"Total mentions analyzed: {len(df)}\n\n{summary_text}")
