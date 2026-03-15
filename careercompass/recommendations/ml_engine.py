import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "career_recommendation_dataset_v2.csv")


def load_dataset():
    df = pd.read_csv(DATA_PATH)

    # combine useful columns for ML
    df["combined"] = (
        df["Focus Area"].astype(str) + " " +
        df["Best Languages/Tools"].astype(str) + " " +
        df["Job Opportunity"].astype(str)
    )

    return df


def recommend_career(user_input):

    df = load_dataset()

    corpus = df["combined"].tolist()
    corpus.append(user_input)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    top_indices = similarity[0].argsort()[-3:][::-1]

    recommendations = df.iloc[top_indices]["Job Opportunity"].tolist()

    return recommendations