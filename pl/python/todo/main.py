from flask import Flask, request, redirect, render_template, flash
import re


app = Flask(__name__)

task_one = {"task": "Walk my dog.", "email": "example@gmail.com", "priority": "low"}
task_two = {
    "task": "Write some code.",
    "email": "example@gmail.com",
    "priority": "medium",
}

task_list = [task_one, task_two]
# Clear task_list for real tasks
task_list = []


@app.route("/")
def index():
    return render_template("to_do_list_sample.html", task_list=task_list)


@app.route("/submit", methods=["POST"])
def submit():
    task = request.form["task"]
    email = request.form["email"]
    priority = request.form["priority"]

    # validate email
    if not re.match(r"[\w.+-]+@[\w-]+\.[\w.-]+", email):
        flash("Invalid email")
        return redirect("/")

    # validate priority
    if priority not in ["Low", "Medium", "High"]:
        flash("Invalid choice")
        return redirect("/")

    task_list.append({"task": task, "email": email, "priority": priority})
    return redirect("/")


if __name__ == "__main__":
    app.run(port=4999)
