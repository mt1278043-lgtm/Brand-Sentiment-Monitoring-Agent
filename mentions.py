import pandas as pd
from datetime import datetime, timedelta
import random

def generate_mentions():
    base_time = datetime.now()
    data = []
    sentiments = ["positive", "neutral", "negative"]
    templates = {
        "positive": ["I love this brand!", "Excellent customer service.", "Top quality!"],
        "neutral": ["Just tried it today.", "Okay product, nothing special."],
        "negative": ["Terrible support.", "Very disappointed with the quality.", "Wouldn't recommend."]
    }

    for i in range(50):
        sentiment = random.choice(sentiments)
        text = random.choice(templates[sentiment])
        timestamp = base_time - timedelta(hours=random.randint(1, 72))
        data.append({"text": text, "timestamp": timestamp, "label": sentiment})

    return pd.DataFrame(data)
