import re
from collections import Counter
import pandas as pd

df = pd.read_parquet("data/cleaned_trend_data.parquet")

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

topics = df['primary_theme'].dropna().unique()

print("\nTOP KEYWORDS BY TOPIC")
print("=" * 50)

for topic in topics:

    topic_df = df[df['primary_theme'] == topic]

    words = []

    for keywords in topic_df['english_keywords'].dropna():
        for word in keywords.split(','):
            word = word.strip().lower()
            word = re.sub(r"[^a-z0-9\s\-']", "", word)

            if len(word) > 2 and word not in stopwords:
                words.append(word)

    counts = Counter(words)

    print("\n" + topic)
    print("-" * 30)
    print(counts.most_common(10))
