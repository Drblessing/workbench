from flask import Flask, render_template, request, redirect, url_for
import re
from dataclasses import dataclass
from typing import Literal


@dataclass
class Task:
    """A simple dataclass to represent a task"""

    task: str
    priority: str = "low"
    email: str | None = None
    done: bool = False


app = Flask(__name__)

# This will be our in-memory tasks list
tasks: list[Task] = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        task_priority = request.form.get("priority", "low")
        task_email = request.form.get("email")

        task = Task(
            task=task_content,
            priority=task_priority,
            email=task_email,
            done=False,
        )

        tasks.append(task)
        return redirect(url_for("index"))
    else:
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    try:
        tasks.pop(task_id)
    except IndexError:
        pass  # Handle the error if we try to delete a non-existent task
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=4999, debug=True)
