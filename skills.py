SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Flask",
    "Django",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Pandas",
    "NumPy",
    "Git",
    "GitHub",
    "AWS",
    "Docker"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills