import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs(resume_text, candidate_skills, jobs_df, top_n=5):
    """Rank jobs using 70% TF-IDF similarity and 30% required-skill coverage."""
    if jobs_df.empty:
        return pd.DataFrame()

    resume_text = str(resume_text or "")
    job_texts = jobs_df["job_description"].fillna("").astype(str).tolist()

    documents = [resume_text] + job_texts
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    try:
        matrix = vectorizer.fit_transform(documents)
        similarities = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    except ValueError:
        similarities = [0.0] * len(job_texts)

    candidate_set = {s.lower() for s in candidate_skills}
    scores, matched_list = [], []

    for idx, row in jobs_df.iterrows():
        required = [x.strip().lower() for x in str(row.get("required_skills", "")).split(",") if x.strip()]
        matched = [x for x in required if x in candidate_set]
        coverage = len(matched) / len(required) if required else 0.0
        text_score = float(similarities[list(jobs_df.index).index(idx)])
        final_score = (0.70 * text_score + 0.30 * coverage) * 100
        scores.append(round(final_score, 1))
        matched_list.append(", ".join(matched))

    result = jobs_df.copy()
    result["match_score"] = scores
    result["matched_skills"] = matched_list
    return result.sort_values("match_score", ascending=False).head(top_n).reset_index(drop=True)
