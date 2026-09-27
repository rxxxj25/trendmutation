import pandas as pd

# Load cleaned dataset
df = pd.read_parquet("data/cleaned_trend_data.parquet")

# Create sentiment categories
def sentiment_category(score):
    if score < -0.1:
        return "Negative"
    elif score > 0.1:
        return "Positive"
    else:
        return "Neutral"

df["sentiment_category"] = df["sentiment"].apply(
    sentiment_category
)

# Count each sentiment category
sentiment_summary = (
    df["sentiment_category"]
    .value_counts()
    .reset_index()
)

sentiment_summary.columns = [
    "sentiment",
    "mentions"
]

# Save summary
sentiment_summary.to_csv(
    "data/sentiment_summary.csv",
    index=False
)

print("\nSentiment summary created successfully!")
print(sentiment_summary)
