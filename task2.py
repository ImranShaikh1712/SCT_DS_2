import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

titles = [
    "Red Notice", "Extraction", "The Gray Man", "Bird Box", "Army of the Dead",
    "The Irishman", "The Kissing Booth", "6 Underground", "Enola Holmes", "Murder Mystery",
    "Triple Frontier", "The Old Guard", "Don't Look Up", "Project Power", "The Platform",
    "Outside the Wire", "The King", "Kate", "The Midnight Sky", "Spiderhead"
]

genres = ["Action", "Thriller", "Comedy", "Drama", "Sci-Fi", "Romance", "Horror"]
countries = ["USA", "UK", "India", "Canada", "Germany", "South Korea", "France"]
languages = ["English", "Hindi", "Korean", "Spanish", "French"]
platforms = ["Netflix"]

data = {
    "Title": titles,
    "Genre": [random.choice(genres) for _ in titles],
    "Release_Year": [random.randint(2015, 2023) for _ in titles],
    "Rating": [round(random.uniform(4.5, 9.5), 1) for _ in titles],
    "Runtime": [random.randint(80, 150) for _ in titles],
    "Country": [random.choice(countries) for _ in titles],
    "Language": [random.choice(languages) for _ in titles],
    "Views": [round(random.uniform(5, 150), 1) for _ in titles],
    "Platform": ["Netflix"] * len(titles)
}

df = pd.DataFrame(data)

sns.set_theme(style='darkgrid')

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Genre', order=df['Genre'].value_counts().index, palette='Set2')
plt.title('Genre Distribution')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=10, kde=True, color='crimson')
plt.title('Rating Distribution')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Genre', y='Rating', palette='coolwarm')
plt.title('Rating by Genre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Runtime', y='Rating', hue='Genre', palette='Dark2', s=100)
plt.title('Runtime vs Rating')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
top_views = df.sort_values(by='Views', ascending=False).head(10)
sns.barplot(data=top_views, x='Views', y='Title', palette='flare')
plt.title('Top 10 Movies by Views')
plt.tight_layout()
plt.show()
