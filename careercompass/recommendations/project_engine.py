import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "multi_domain_repos.csv")

df = pd.read_csv(DATA_PATH)

# normalize column names
df.columns = df.columns.str.lower()

def recommend_projects(skill):

    filtered = df[df["language"].str.contains(skill, case=False, na=False)]

    # sort by popularity
    projects = filtered.sort_values("stars", ascending=False).head(5)

    result = []

    for _, row in projects.iterrows():
        result.append({
            "title": row["repo"],
            "owner": row["owner"],
            "language": row["language"],
            "stars": row["stars"],
            "url": row["url"]
        })

    return result