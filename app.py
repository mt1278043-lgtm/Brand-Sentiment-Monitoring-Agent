import streamlit as st
import matplotlib.pyplot as plt
from mentions import generate_mentions
from sentiment_model import analyze_sentiment
from summary_prompt import summary_prompt
import os

try:
    try:
        from langchain_openai import ChatOpenAI
    except ImportError:
        from langchain.chat_models import ChatOpenAI
except ImportError:
    ChatOpenAI = None

st.title("🧠 Brand Sentiment Monitoring Agent")
st.write("Real-time sentiment monitoring system for brand mentions across channels")

if st.button("Run Sentiment Analysis"):
    with st.spinner("Analyzing brand mentions..."):
        # Generate mentions
        df = generate_mentions()

        # Analyze sentiment
        df["Sentiment"] = df["text"].apply(analyze_sentiment)
        sentiment_counts = df["Sentiment"].value_counts()

        # Pie chart
        st.subheader("🔎 Sentiment Breakdown")
        fig, ax = plt.subplots(figsize=(8, 6))
        colors = ['#2ecc71', '#95a5a6', '#e74c3c']  # green, gray, red
        ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", colors=colors, startangle=90)
        ax.set_title(f"Sentiment Distribution ({len(df)} mentions)")
        st.pyplot(fig)

        # Display sentiment data
        st.subheader("📊 Sentiment Data")
        display_df = df[["text", "timestamp", "Sentiment"]].sort_values("timestamp", ascending=False).copy()
        display_df["timestamp"] = display_df["timestamp"].dt.strftime("%Y-%m-%d %H:%M")
        st.dataframe(display_df, use_container_width=True)

        # Summary Statistics
        st.subheader("📈 Summary Statistics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Mentions", len(df))
        with col2:
            positive_pct = (sentiment_counts.get('positive', 0) / len(df) * 100)
            st.metric("Positive %", f"{positive_pct:.1f}%")
        with col3:
            neutral_pct = (sentiment_counts.get('neutral', 0) / len(df) * 100)
            st.metric("Neutral %", f"{neutral_pct:.1f}%")
        with col4:
            negative_pct = (sentiment_counts.get('negative', 0) / len(df) * 100)
            st.metric("Negative %", f"{negative_pct:.1f}%")

        # GPT Summary
        summary_text = df["Sentiment"].value_counts().to_string()

        # Check if OpenAI API key is available
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key and ChatOpenAI:
            try:
                llm = ChatOpenAI(temperature=0.4, api_key=api_key)
                gpt_summary = llm.predict(summary_prompt.format(sentiment_data=summary_text))

                st.subheader("🧠 GPT Summary & Recommendations")
                st.text_area("Insights", gpt_summary, height=300)
            except Exception as e:
                st.warning(f"Could not generate GPT summary: {e}")
                st.info("Showing rule-based summary below.")
                st.subheader("📈 Sentiment Summary")
                st.text(f"Total mentions analyzed: {len(df)}\n\n{summary_text}")
        else:
            if not ChatOpenAI:
                st.info("ℹ️ LangChain integration not available in this environment.")
            else:
                st.info("ℹ️ To enable GPT-based insights, set the OPENAI_API_KEY environment variable.")
            st.subheader("📈 Sentiment Summary")
            st.text(f"Total mentions analyzed: {len(df)}\n\n{summary_text}")
