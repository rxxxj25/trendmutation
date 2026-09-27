import pandas as pd

# Load cleaned dataset
df = pd.read_parquet("data/cleaned_trend_data.parquet")

# Count emotions
emotion_summary = (
    df["main_emotion"]
    .value_counts()
    .reset_index()
)

emotion_summary.columns = [
    "emotion",
    "mentions"
]

# Save summary
emotion_summary.to_csv(
    "data/emotion_summary.csv",
    index=False
)

print("\nEmotion summary created successfully!")
print(emotion_summary)
