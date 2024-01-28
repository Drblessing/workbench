from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = Task()
        task.task = request.form["task"]
        task.email = request.form["email"]
        task.priority = request.form["priority"]
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("index"))
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<id>")
def delete(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("index"))
