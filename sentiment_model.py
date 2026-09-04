from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    try:
        result = sentiment_pipeline(text)[0]
        label = result['label'].lower()
        # Map POSITIVE/NEGATIVE to positive/negative
        if label == 'positive':
            return 'positive'
        elif label == 'negative':
            return 'negative'
        else:
            return 'neutral'
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 'neutral'
