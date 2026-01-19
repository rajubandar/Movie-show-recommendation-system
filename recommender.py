import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# Get project root (DATA/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to CSV
CSV_PATH = os.path.join(BASE_DIR, "netflix_titles.csv")

# Load dataset
df = pd.read_csv(CSV_PATH)
df.fillna("", inplace=True)






def recommend(age, preferred_genres, content_type):
    df_filtered = df.copy()

    # 1️⃣ Content type filter
    df_filtered = df_filtered[df_filtered["type"] == content_type]

    # 2️⃣ Age-based rating filter
    if age < 13:
        allowed = ["G", "PG"]
    elif age < 18:
        allowed = ["PG-13", "TV-14", "PG"]
    else:
        allowed = df_filtered["rating"].unique()

    df_filtered = df_filtered[df_filtered["rating"].isin(allowed)]

    # 3️⃣ GENRE MATCH (substring-based, not exact)
    def genre_match(row):
        for g in preferred_genres:
            if g.lower() in row.lower():
                return True
        return False

    df_filtered = df_filtered[
        df_filtered["listed_in"].apply(genre_match)
    ]

    # 4️⃣ If still empty, fallback (IMPORTANT)
    if df_filtered.empty:
        df_filtered = df[df["type"] == content_type].head(5)

    # 5️⃣ Return top titles
    return df_filtered[["title", "listed_in", "rating"]].head(5)
