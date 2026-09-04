# 🧠 Brand Sentiment Monitoring Agent

A real-time brand sentiment monitoring system that analyzes brand mentions across channels using AI-powered sentiment analysis and provides actionable insights.

## 📋 Overview

This agent continuously tracks brand sentiment by:
- Simulating or ingesting brand mentions with text content
- Performing sentiment analysis using transformer models
- Visualizing sentiment trends over time
- Summarizing insights using GPT

## 🧰 Tech Stack

- **Python** - Core language
- **Pandas** - Data manipulation
- **Matplotlib** - Data visualization
- **Transformers (HuggingFace)** - Pre-trained sentiment analysis
- **Streamlit** - Web dashboard
- **LangChain** - LLM integration
- **OpenAI GPT** - Insight generation

## 🚀 Quick Start

### 1. Environment Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the Application

```bash
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`

## 🔧 Components

### `mentions.py`
Generates simulated brand mentions with timestamps and predefined sentiments.

### `sentiment_model.py`
Performs sentiment analysis using DistilBERT, a lightweight transformer model.

### `summary_prompt.py`
Defines the LangChain prompt template for GPT-based analysis.

### `app.py`
Streamlit dashboard that:
- Generates 50 random brand mentions
- Performs sentiment analysis
- Displays sentiment distribution via pie chart
- Shows mention data in a table
- Provides GPT-based insights (requires OPENAI_API_KEY)

## 🔑 Configuration

Set the OpenAI API key for GPT-based insights:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

Or create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

## 📊 Features

- **Real-time Analysis**: Analyze brand mentions as they come in
- **Sentiment Visualization**: Interactive pie charts and trend analysis
- **Automated Insights**: GPT-powered summary and recommendations
- **Warning Detection**: Identify spikes in negative feedback
- **Action Recommendations**: Get 2 specific actions to improve brand reputation

## 📈 Example Output

The dashboard provides:
1. **Sentiment Breakdown** - Pie chart showing positive/neutral/negative distribution
2. **Mention Data Table** - Complete list of analyzed mentions with timestamps
3. **GPT Summary** - AI-generated insights including:
   - Overall sentiment assessment
   - Warning signs and red flags
   - 2 recommended actions for improvement

## 📝 License

This project is part of the AI Agent Lab series.
