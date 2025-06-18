import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Load CSV with a 'title' column
csv_path = input("Enter path to CSV with YouTube titles: ").strip()
df = pd.read_csv(csv_path)

# Combine all titles into one string, clean text
text = " ".join(df['title'].astype(str))
text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
text = text.lower()

# Generate word cloud
wc = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.title("YouTube Titles Word Cloud")
plt.show()