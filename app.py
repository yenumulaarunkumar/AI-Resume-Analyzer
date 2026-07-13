from flask import Flask, render_template, request
from skills import extract_skills
from score import calculate_score
from matcher import calculate_match
from missing_skills import find_missing_skills
import pdfplumber

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    if file:
        text = ""

        # Extract text from PDF
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # Extract skills
        skills = extract_skills(text)

        # Calculate ATS score
        score = calculate_score(skills)

        # Get Job Description
        job_description = request.form["job_description"]

        # Calculate Resume Match Percentage
        match_percentage = calculate_match(text, job_description)

        # Find Missing Skills
        missing_skills = find_missing_skills(text, job_description)

        return render_template(
            "result.html",
            skills=skills,
            text=text,
            score=score,
            match=match_percentage,
            missing=missing_skills
        )

    return "No file selected"


if __name__ == "__main__":
    app.run(debug=True)