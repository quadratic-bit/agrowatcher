from datetime import datetime

from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from app.models.database import db, lm


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String, unique=True, nullable=False, index=True)
    hashed_password = db.Column(db.String, nullable=False)

    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)

    created_date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"<User {self.name} ({self.email})>"


class LoginForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


@lm.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(user_id)
