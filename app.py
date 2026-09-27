import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="TrendMutation",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load data
# -----------------------------

summary = pd.read_csv("data/trend_summary.csv")
keywords = pd.read_csv("data/topic_keywords.csv")
languages = pd.read_csv("data/language_summary.csv")
sentiments = pd.read_csv("data/sentiment_summary.csv")
emotions = pd.read_csv("data/emotion_summary.csv")

# -----------------------------
# Title
# -----------------------------

st.title("📊 TrendMutation")
st.subheader("Multilingual Trend & Sentiment Analytics")

st.write(
    "Explore topic popularity, sentiment, emotions and keywords "
    "from a large multilingual dataset."
)

# -----------------------------
# Overview metrics
# -----------------------------

total_mentions = summary["mentions"].sum()
total_topics = summary["primary_theme"].nunique()
overall_sentiment = summary["average_sentiment"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "📦 Total Records",
        f"{total_mentions:,}"
    )

with col2:
    st.metric(
        "📚 Topics",
        total_topics
    )

with col3:
    st.metric(
        "🌍 Languages",
        languages["language"].nunique()
    )

with col4:
    st.metric(
        "👍 Positive",
        f"{sentiments[sentiments['sentiment'] == 'Positive']['mentions'].iloc[0]:,}"
    )

with col5:
    st.metric(
        "👎 Negative",
        f"{sentiments[sentiments['sentiment'] == 'Negative']['mentions'].iloc[0]:,}"
    )

st.divider()

# -----------------------------
# Topic popularity
# -----------------------------

st.header("🔥 Topic Popularity")

popularity = summary.sort_values(
    "mentions",
    ascending=True
)

st.bar_chart(
    popularity.set_index("primary_theme")["mentions"]
)

# -----------------------------
# Sentiment by topic
# -----------------------------

st.header("😊 Sentiment by Topic")

sentiment_data = summary.sort_values(
    "average_sentiment"
)

st.bar_chart(
    sentiment_data.set_index("primary_theme")[
        "average_sentiment"
    ]
)

# -----------------------------
# Topic explorer
# -----------------------------

st.header("🔎 Topic Explorer")

selected_topic = st.selectbox(
    "Select a topic",
    summary["primary_theme"].tolist()
)

selected_summary = summary[
    summary["primary_theme"] == selected_topic
].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Mentions",
        f"{selected_summary['mentions']:,}"
    )

with col2:
    st.metric(
        "Average Sentiment",
        f"{selected_summary['average_sentiment']:.3f}"
    )

with col3:
    st.metric(
        "Top Emotion",
        selected_summary["top_emotion"]
    )

# -----------------------------
# Keywords for selected topic
# -----------------------------

st.subheader(f"🔑 Top Keywords — {selected_topic}")

selected_keywords = keywords[
    keywords["topic"] == selected_topic
].copy()

selected_keywords = selected_keywords.sort_values(
    "count",
    ascending=False
)

st.dataframe(
    selected_keywords,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Footer
# -----------------------------


# -----------------------------
# Language Analysis
# -----------------------------

st.header("🌍 Language Distribution")

language_chart = languages.head(15).sort_values(
    "mentions",
    ascending=True
)

st.bar_chart(
    language_chart.set_index("language")["mentions"]
)
# -----------------------------
# Sentiment Distribution
# -----------------------------

st.header("😊 Sentiment Distribution")

st.bar_chart(
    sentiments.set_index("sentiment")["mentions"]
)
# -----------------------------
# Emotion Analysis
# -----------------------------

st.header("🎭 Emotion Analysis")

emotion_chart = emotions.head(15).sort_values(
    "mentions",
    ascending=True
)

st.bar_chart(
    emotion_chart.set_index("emotion")["mentions"]
)

# -----------------------------
# Key Insights
# -----------------------------

st.header("💡 Key Insights")

most_discussed = summary.loc[
    summary["mentions"].idxmax(),
    "primary_theme"
]

most_positive = summary.loc[
    summary["average_sentiment"].idxmax(),
    "primary_theme"
]

most_negative = summary.loc[
    summary["average_sentiment"].idxmin(),
    "primary_theme"
]

most_common_emotion = emotions.iloc[0]["emotion"]

most_common_language = {
    "en": "English",
    "ja": "Japanese",
    "es": "Spanish",
    "pt": "Portuguese",
    "ar": "Arabic",
    "fr": "French",
    "zh": "Chinese",
    "de": "German",
    "hi": "Hindi",
    "ru": "Russian",
    "ko": "Korean",
    "it": "Italian"
}.get(
    languages.iloc[0]["language"],
    languages.iloc[0]["language"]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔥 Most Discussed", most_discussed)

with col2:
    st.metric("😊 Most Positive", most_positive)

with col3:
    st.metric("😐 Most Common Emotion", most_common_emotion)

col4, col5 = st.columns(2)

with col4:
    st.metric("🌍 Most Common Language", most_common_language)

with col5:
    st.metric("📉 Most Negative", most_negative)
st.divider()

st.caption(
    "TrendMutation | Multilingual Trend & Sentiment Analytics"
)
