from skills import SKILLS

def find_missing_skills(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    missing = []

    for skill in SKILLS:

        if skill.lower() in job_description and skill.lower() not in resume_text:
            missing.append(skill)

    return missing