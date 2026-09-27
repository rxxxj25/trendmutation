import re
import pandas as pd
from collections import Counter

# Load cleaned dataset
df = pd.read_parquet("data/cleaned_trend_data.parquet")

# Words we don't want in the dashboard
stopwords = {
    'the', 'and', 'or', 'but', 'you', 'your', 'i', "i'm",
    'a', 'an', 'to', 'of', 'in', 'on', 'for', 'with',
    'is', 'it', 'this', 'that', 'was', 'were', 'are',
    'be', 'been', 'has', 'have', 'had', 'as', 'at',
    'by', 'from', 'they', 'he', 'she', 'we', 'them',
    'his', 'her', 'their', 'our', 'my', 'me', 'do',
    'does', 'did', 'not', 'no', 'so', 'if', 'just',
    'can', 'will', 'would', 'could', 'about',
    'people', 'time', 'good', 'make', 'love', 'day',
    'back', 'years', 'work', 'today', 'world', 'great',
    'year', 'life', 'thing', 'lot', 'made', 'man',
    'home', 'things', 'give', 'bad', 'feel', 'long',
    'put', 'real', 'big', 'live', 'end', 'person',
    'find', 'stop', 'house', 'all', 'how', 'new',
    'part', 'point', 'times', 'guy', 'don'
}

results = []

for topic in df['primary_theme'].dropna().unique():

    topic_df = df[df['primary_theme'] == topic]

    words = []

    for keywords in topic_df['english_keywords'].dropna():

        for word in keywords.split(','):

            word = word.strip().lower()
            word = re.sub(r"[^a-z0-9\s\-']", "", word)

            if len(word) > 2 and word not in stopwords:
                words.append(word)

    counts = Counter(words)

    for keyword, count in counts.most_common(10):

        results.append({
            "topic": topic,
            "keyword": keyword,
            "count": count
        })

# Create dataframe
keyword_df = pd.DataFrame(results)

# Save CSV
keyword_df.to_csv(
    "data/topic_keywords.csv",
    index=False
)

print("\nTopic keyword file created successfully!")
print(keyword_df.head(20))
print("\nTotal rows:", len(keyword_df))
