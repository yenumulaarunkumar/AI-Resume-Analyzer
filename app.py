from flask import Flask, render_template, request, send_file
import pdfplumber

from database import db
from models import Resume

from skills import extract_skills
from score import calculate_score
from semantic_matcher import semantic_match
from missing_skills import find_missing_skills
from suggestions import generate_suggestions
from feedback import generate_feedback
from report_generator import generate_report

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resume.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    if not file:
        return "No file selected"

    text = ""

    # Extract text from PDF
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Extract skills
    skills = extract_skills(text)

    # ATS Score
    score = calculate_score(skills)

    # Job Description
    job_description = request.form["job_description"]

    # Semantic Match
    match_percentage = semantic_match(text, job_description)

    # Missing Skills
    missing_skills = find_missing_skills(text, job_description)

    # Suggestions
    suggestions = generate_suggestions(missing_skills)

    # Feedback
    feedback = generate_feedback(score, missing_skills)

    # Generate PDF Report
    generate_report(
        score,
        match_percentage,
        skills,
        missing_skills,
        suggestions
    )

    # Save to Database
    resume_record = Resume(
        filename=file.filename,
        ats_score=score,
        resume_match=match_percentage
    )

    db.session.add(resume_record)
    db.session.commit()

    return render_template(
        "result.html",
        skills=skills,
        text=text,
        score=score,
        match=match_percentage,
        missing=missing_skills,
        suggestions=suggestions,
        feedback=feedback
    )


@app.route("/download")
def download():
    return send_file(
        "Resume_Report.pdf",
        as_attachment=True
    )


@app.route("/history")
def history():
    resumes = Resume.query.all()
    return render_template(
        "history.html",
        resumes=resumes
    )


if __name__ == "__main__":
    app.run(debug=True)