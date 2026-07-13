from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match(resume, jd):

    text = [resume, jd]

    cv = CountVectorizer()

    matrix = cv.fit_transform(text)

    similarity = cosine_similarity(matrix)[0][1]

    return round(similarity * 100, 2)