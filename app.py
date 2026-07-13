from flask import Flask, render_template, request
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

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        return f"""
        <h2>Resume Text</h2>
        <pre>{text}</pre>
        """

    return "No file selected"

if __name__ == "__main__":
    app.run(debug=True)