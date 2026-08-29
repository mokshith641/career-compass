import os
import pandas as pd
import random

# LOAD DATASET
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "datasets", "multi_domain_repos.csv")
df = pd.read_csv(DATA_PATH)

def recommend_projects(user_input):

    projects = []

    # convert user input into keywords
    keywords = []

    for word in user_input.split(","):

        word = word.strip().lower()

        if word:
            keywords.append(word)

    # ADD EXTRA TECH KEYWORDS
    extra_keywords = {

        "vlsi": ["verilog", "fpga", "chip", "rtl", "hdl"],

        "ai": ["machine learning", "deep learning", "tensorflow"],

        "web": ["django", "react", "frontend"],

        "cybersecurity": ["security", "hacking", "network"],

        "data science": ["pandas", "numpy", "analysis"]

    }

    expanded_keywords = keywords.copy()

    for key in keywords:

        if key in extra_keywords:

            expanded_keywords.extend(extra_keywords[key])

    # MATCH PROJECTS

    for _, row in df.iterrows():

        row_text = " ".join(
            [str(v).lower() for v in row.values]
        )

        score = 0

        for keyword in expanded_keywords:

            if keyword in row_text:
                score += 1

        if score > 0:

            projects.append({

                "title": row["Repo"],

                "owner": row["Owner"],

                "language": row["Language"],

                "stars": row["Stars"],

                "url": row["URL"],

                "score": score

            })

    # SORT BY BEST SCORE
    projects = sorted(
        projects,
        key=lambda x: x["score"],
        reverse=True
    )

    # RETURN TOP 3 IF FOUND
    if projects:
        return projects[:3]

    # FALLBACK RANDOM PROJECTS
    fallback_projects = []

    random_rows = df.sample(min(3, len(df)))

    for _, row in random_rows.iterrows():

        fallback_projects.append({

            "title": row["Repo"],

            "owner": row["Owner"],

            "language": row["Language"],

            "stars": row["Stars"],

            "url": row["URL"]

        })

    return fallback_projects