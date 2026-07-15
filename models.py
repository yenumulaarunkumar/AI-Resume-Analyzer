from database import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200))
    ats_score = db.Column(db.Integer)
    resume_match = db.Column(db.Float)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )