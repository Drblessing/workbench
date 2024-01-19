from flask import Flask, request, redirect, render_template, flash
import re

app = Flask(__name__)

task_list = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
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
        return redirect("/to_do_list")

    return render_template("index.html")


@app.route("/to_do_list")
def to_do_list():
    return render_template("to_do_list.html", task_list=task_list)


@app.route("/clear", methods=["POST"])
def clear():
    task_list.clear()
    return redirect("/to_do_list")


if __name__ == "__main__":
    app.run()
