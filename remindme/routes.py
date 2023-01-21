from remindme import app
from flask import render_template, request, redirect, url_for, flash, get_flashed_messages, request
from remindme.models import Task, User
from remindme.forms import RegisterForm, LoginForm
from remindme import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/task", methods=["GET", "POST"])
@login_required
def task_page():
        return render_template("task.html")
    

@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created! You were logged in as {user_to_create.username}", category="success")
        return redirect(url_for("home_page"))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f"There was an error with creating a user: {err_msg}", category="danger")

    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f"Logged as {attempted_user.username}", category="success")
            return render_template("task.html")
        else:
            flash("Something is wrong! Check the username and password", category="danger")



    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("home_page"))