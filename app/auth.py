from flask import Blueprint, render_template, redirect, Response
from flask_login import login_user, current_user

from app.models.database import db
from app.models.users import RegisterForm, User, LoginForm

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login", methods=["GET", "POST"])
def login() -> str | Response:
    if current_user.is_authenticated:
        return redirect("/dashboard")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/dashboard")
        return render_template("auth/login.html", form=form, message="Неверный логин или пароль")
    return render_template("auth/login.html", form=form)


@bp_auth.route("/signup", methods=["GET", "POST"])
def signup() -> str | Response:
    if current_user.is_authenticated:
        return redirect("/dashboard")
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("auth/signup.html", form=form, message="Пароли не совпадают")
        if User.query.filter_by(email=form.email.data).first():
            return render_template("auth/signup.html", form=form,
                                   message="Такой пользователь уже существует")
        user = User(email=form.email.data, name=form.name.data)  # noqa
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=False)
        return redirect("/dashboard")
    return render_template("auth/signup.html", form=form)
