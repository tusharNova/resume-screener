import spacy
from fuzzywuzzy import fuzzz

npl = spacy.load("en_core_web_sm")


COMMON_SKILLS = [
    "python""python", "django", "flask", "fastapi", "sql", "mysql", "postgresql", "git", "docker",
    "rest", "api", "html", "css", "javascript", "react", "linux", "aws"
]


def extract_keywords(text : str):
    doc = npl(text.lower)
    words = set([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])
    matched = [skill for skill in COMMON_SKILLS if skill in words]
    return matched

def compare_resume_to_jd(resume_text: str, jd_text: str):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = list(set(resume_keywords) & set(jd_keywords))
    missing = list(set(jd_keywords) - set(resume_keywords))

    # Calculate match score (basic: ratio of matched)
    match_score = int(len(matched) / max(1, len(jd_keywords)) * 100)

    return {
        "match_score": match_score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "suggestions": f"Consider adding: {', '.join(missing)}" if missing else "Great match!"
    }