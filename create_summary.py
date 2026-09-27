import pandas as pd

# Load cleaned dataset
df = pd.read_parquet("data/cleaned_trend_data.parquet")

# Create topic summary
topic_summary = (
    df.groupby("primary_theme")
    .agg(
        mentions=("primary_theme", "size"),
        average_sentiment=("sentiment", "mean")
    )
    .reset_index()
)

# Find the most common non-neutral emotion for each topic
non_neutral = df[df["main_emotion"] != "neutral"]

top_emotions = (
    non_neutral.groupby(["primary_theme", "main_emotion"])
    .size()
    .reset_index(name="count")
)

top_emotions = top_emotions.loc[
    top_emotions.groupby("primary_theme")["count"].idxmax()
]

top_emotions = top_emotions[
    ["primary_theme", "main_emotion"]
].rename(
    columns={"main_emotion": "top_emotion"}
)

# Combine topic summary and emotion
trend_summary = topic_summary.merge(
    top_emotions,
    on="primary_theme",
    how="left"
)

# Sort by number of mentions
trend_summary = trend_summary.sort_values(
    "mentions",
    ascending=False
)

# Save result
trend_summary.to_csv(
    "data/trend_summary.csv",
    index=False
)

print("\nTrend summary created successfully!")
print(trend_summary)
