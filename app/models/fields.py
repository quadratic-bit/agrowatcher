from datetime import datetime
from app.models.database import db


class Field(db.Model):
    __tablename__ = "field"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    polygon = db.Column(db.String, nullable=False)
    area = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
