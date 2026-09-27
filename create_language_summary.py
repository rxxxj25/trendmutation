import pandas as pd

# Load cleaned dataset
df = pd.read_parquet("data/cleaned_trend_data.parquet")

# Count records by language
language_summary = (
    df.groupby("language")
    .size()
    .reset_index(name="mentions")
    .sort_values("mentions", ascending=False)
)

# Save summary
language_summary.to_csv(
    "data/language_summary.csv",
    index=False
)

print("\nLanguage summary created successfully!")
print(language_summary.head(20))
