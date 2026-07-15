from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_report(score, match, skills, missing, suggestions):

    filename = "Resume_Report.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Resume Analyzer Report</b>", styles["Heading1"]))
    story.append(Paragraph(f"ATS Score: {score}/100", styles["Normal"]))
    story.append(Paragraph(f"Resume Match: {match}%", styles["Normal"]))

    story.append(Paragraph("<b>Detected Skills</b>", styles["Heading2"]))
    for skill in skills:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))
    for skill in missing:
        story.append(Paragraph(skill, styles["Normal"]))

    story.append(Paragraph("<b>Suggestions</b>", styles["Heading2"]))
    for suggestion in suggestions:
        story.append(Paragraph(suggestion, styles["Normal"]))

    doc.build(story)

    return filename