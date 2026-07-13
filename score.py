def calculate_score(skills):
    total_skills = 19

    score = int((len(skills) / total_skills) * 100)

    if score > 100:
        score = 100

    return score