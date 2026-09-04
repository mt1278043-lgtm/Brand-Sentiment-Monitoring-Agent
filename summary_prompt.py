from langchain_core.prompts import PromptTemplate

summary_prompt = PromptTemplate.from_template("""
You are a brand analyst AI.

Given this sentiment breakdown:
{sentiment_data}

1. What is the overall brand sentiment?
2. Are there warning signs (e.g., recent spikes in negativity)?
3. Recommend 2 actions for brand reputation improvement.

Respond in 3 short paragraphs.
""")
