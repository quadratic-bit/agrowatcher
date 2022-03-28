from datetime import datetime

from flask_login import UserMixin
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired

from app.models.database import db, lm


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String, unique=True, nullable=False, index=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=True)

    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now)

    hashed_password = db.Column(db.String, nullable=True)

    def set_password(self, plain_password: str) -> None:
        self.hashed_password = generate_password_hash(plain_password)

    def check_password(self, plain_password: str) -> bool:
        return check_password_hash(self.hashed_password, plain_password)

    def __repr__(self) -> str:
        return f"<User {self.name} ({self.email})>"


class LoginForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    email = EmailField("Почта", validators=[DataRequired()])
    name = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password_again = PasswordField("Повторите пароль", validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Зарегистрироваться")


@lm.user_loader
def load_user(user_id: int) -> User:
    return User.query.get(user_id)
