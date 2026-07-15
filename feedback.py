def generate_feedback(score, missing_skills):

    feedback = []

    if score < 60:
        feedback.append(
            "Your ATS score is low. Add more technical skills and projects."
        )

    elif score < 80:
        feedback.append(
            "Your ATS score is good but can be improved."
        )

    else:
        feedback.append(
            "Excellent ATS score."
        )

    if len(missing_skills) > 0:
        feedback.append(
            "Consider learning these missing skills:"
        )

        for skill in missing_skills:
            feedback.append(skill)

    feedback.append(
        "Add measurable achievements in your projects."
    )

    feedback.append(
        "Keep your resume within one page."
    )

    feedback.append(
        "Include your GitHub and LinkedIn profile."
    )

    return feedback