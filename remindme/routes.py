from remindme import app
from flask import render_template, request, redirect, url_for, flash
from remindme.models import Task, User
from remindme.forms import RegisterForm, LoginForm, CreateTask, EditTask, DeleteTask, EditDoneTask
from remindme import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/task", methods=["GET", "POST"])
@login_required
def task_page():
    task_list = Task.query.filter_by(owner=current_user.id)
    edit_form = EditTask()
    edit_done_form = EditDoneTask()
    delete_form = DeleteTask()
    if request.method == "POST":
        #Delete Task
        deleted_task = request.form.get("deleted_task")
        d_task_object = Task.query.filter_by(id=deleted_task).first()
        if d_task_object:
            Task.query.filter_by(id=deleted_task).delete()
            db.session.commit()
            return redirect(url_for("task_page"))
        #Edit Task
        edited_task = request.form.get("edited_task")
        e_task_object = Task.query.filter_by(id=edited_task).first()
        if e_task_object:
            e_task_object = Task.query.filter_by(id=edited_task).first()
            e_task_object.task_name = edit_form.task_name.data
            e_task_object.description = edit_form.description.data
            db.session.add(e_task_object)
            db.session.commit()
            flash(f"Tarefa editada com sucesso.", category="success")
            return redirect(url_for("task_page"))
        #Edit Done Task
        edited_task_done = request.form.get("done_task")
        ed_task_object = Task.query.filter_by(id=edited_task_done).first()
        if ed_task_object:
            if ed_task_object.done == True:
                ed_task_object.done = False
            else:
                ed_task_object.done = True
            db.session.commit()
            return redirect(url_for("task_page"))

    

    if request.method == "GET":
        return render_template("task.html", task_list=task_list, edit_form=edit_form, delete_form=delete_form, edit_done_form=edit_done_form)   

@app.route("/add", methods=["GET", "POST"])
@login_required
def add_task_page():
    form = CreateTask()
    if form.validate_on_submit():
        new_task = Task(task_name=form.task_name.data, 
                        description=form.description.data,
                        owner=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("task_page"))
    else:
        for err_msg in form.errors.values():
                print(f"Houve um erro ao criar tarefa: {err_msg}.")

    return render_template("task_create.html", form=form)

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
        flash(f"Conta criada com sucesso! Olá {user_to_create.username}.", category="success")
        return redirect(url_for("task_page"))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f"Houve um erro ao criar a conta, tente novamente! {err_msg}", category="danger")

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
            flash(f"Conectado! Olá {attempted_user.username}.", category="success")
            return redirect(url_for("task_page"))
        else:
            flash("Houve um erro! Verifique seu Usuario e Senha e tente novamente.", category="danger")

    return render_template("login.html", form=form)

@app.route("/logout")
def logout_page():
    logout_user()
    flash("Você desconectou!", category="info")
    return redirect(url_for("home_page"))