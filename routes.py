from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.helpers import get_all_todos, add_todo, toggle_todo, delete_todo
from app.models import Todo

@app.route("/")
def home():
    todos = get_all_todos()
    return render_template("base.html", todo_list=todos)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if not add_todo(title):
        flash("Invalid input: Task title cannot be empty.")
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    toggle_todo(todo_id)
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for("home"))
