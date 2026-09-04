from transformers import pipeline

sentiment_pipeline = None

def _load_model():
    global sentiment_pipeline
    if sentiment_pipeline is None:
        try:
            sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        except Exception as e:
            print(f"Warning: Could not load sentiment model: {e}")
            print("Using rule-based sentiment analysis as fallback")
            sentiment_pipeline = False

def analyze_sentiment(text):
    _load_model()

    if sentiment_pipeline is False:
        return _rule_based_sentiment(text)

    try:
        result = sentiment_pipeline(text)[0]
        label = result['label'].lower()
        if label == 'positive':
            return 'positive'
        elif label == 'negative':
            return 'negative'
        else:
            return 'neutral'
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return _rule_based_sentiment(text)

def _rule_based_sentiment(text):
    positive_words = ['love', 'excellent', 'great', 'good', 'amazing', 'wonderful', 'fantastic', 'awesome', 'top', 'quality', 'best']
    negative_words = ['terrible', 'bad', 'disappointed', 'hate', 'awful', 'poor', 'worst', "wouldn't", "don't like", 'disappointing']

    text_lower = text.lower()
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)

    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'
